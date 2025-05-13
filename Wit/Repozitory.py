import json
import os
from typing import TextIO

from Commit import Commit
from WitModuls import create_folder, copy_file, copy_folder, delete_folder_contents, create_file, \
     compare_files, copy_folder_contents,filter_stage


class Repozitory:
    def __init__(self, path):
        self.__commits_list = []
        self.__current_path = path
        self.__commits_file = os.path.join(self.__current_path, '.wit', 'commits_list.json')

    def init(self):
        if not os.path.exists(os.path.join(self.__current_path , '.wit')):
            create_folder(os.path.join(self.__current_path, '.wit'))
            create_file(self.__commits_file)
            create_folder(os.path.join(self.__current_path, '.wit', 'versions'))
            create_folder(os.path.join(self.__current_path, '.wit', 'stage'))
        else:
            raise ValueError("There are already repositories in this folder.")

    def add(self, path):
        if os.path.isfile( path):
            copy_file(os.path.join(self.__current_path, path),
                      os.path.join(self.__current_path, ".wit", "stage", path))
        elif os.path.isdir(path):
            copy_folder(os.path.join(self.__current_path, path),
                        os.path.join(self.__current_path, ".wit", "stage", path))
        else:
            raise ValueError(e)

    def commit(self, message):
        new_commit = Commit(message)
        self.__commits_list.append(new_commit.to_dict())
        self.save_commits_to_file()
        create_folder(os.path.join(self.__current_path, ".wit", "versions", str(new_commit._hash_code)))
        filter_stage(os.path.join(self.__current_path, '.wit', 'stage'),self.__current_path)
        copy_folder(os.path.join(self.__current_path,'.wit', 'stage'),os.path.join(self.__current_path, '.wit', 'versions', str(new_commit._hash_code)))
        delete_folder_contents(os.path.join(self.__current_path, '.wit', 'stage'))

    def log(self):
        for commit in self.__commits_list:
            print(f"message: {commit['message']}\nhash_code: {commit['hash_code']}\ndate: {commit['date']}\n")

    def status(self):
        stage_path = os.path.join(self.__current_path, '.wit', 'stage')
        compare_files(self.__current_path, stage_path)

    def checkout(self, commit_hash):
        delete_folder_contents(self.__current_path)
        copy_folder(os.path.join(self.__current_path, '.wit', 'versions', str(commit_hash)), self.__current_path)

    def save_commits_to_file(self):
        with open(self.__commits_file, 'w') as file:
            json.dump(self.__commits_list, file, indent=4)

    def load_commits_from_file(self):
        if not os.path.exists(self.__commits_file) or os.path.getsize(self.__commits_file) == 0:
            self.__commits_list= []
        else:
            with open(self.__commits_file, 'r') as jsonfile:
                commits_data = json.load(jsonfile)
                # print(f"commits_data{commits_data}")
                commits = [data for data in commits_data]
                self.__commits_list = commits
