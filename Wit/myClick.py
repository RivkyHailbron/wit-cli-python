import os
from logging import exception

import click
from Repozitory import Repozitory
from colorama import init, Fore

init(autoreset=True)

class Cli:
    def __init__(self, repo_path):
        self.repozitory = Repozitory(repo_path)
        #טעינת רשימת הקומיטים מהקובץ JSON
        self.repozitory.load_commits_from_file()

    def create_cli(self):

        @click.group()
        def cli():
            """Management user interface repository"""
            pass

        @cli.command()
        def init():
            try:
                self.repozitory.init()
                click.echo("Initialized repository structure.")
            except Exception as e:
                click.echo(Fore.RED+f"Error {e}")

        @cli.command()
        @click.argument("path")
        def add(path):
            try:
                self.repozitory.add(path)
                if os.path.isfile(path):
                    click.echo(f" file : {path} added successfully.")
                elif os.path.isdir(path):
                    click.echo(f" folder : {path} added successfully.")
            except Exception as e:
                click.echo(Fore.RED+f"Error {e}")

        @cli.command()
        @click.argument("message")
        def commit(message):
            try:
                self.repozitory.commit(message)
                click.echo(f"Commited {message} successfully.")
            except Exception as e:
                click.echo(Fore.RED+f"Error {e}")

        @cli.command()
        def log():
            try:
                self.repozitory.log()
            except Exception as e:
                click.echo(Fore.RED+f"Error {e}")

        @cli.command()
        def status():
            try:
                self.repozitory.status()
            except Exception as e:
                click.echo(Fore.RED+f"Error {e}")

        @cli.command()
        @click.argument("commit_hash")
        def checkout(commit_hash):
            try:
                self.repozitory.checkout(commit_hash)
            except Exception as e:
                click.echo(Fore.RED+f"Error {e}")

        return cli
