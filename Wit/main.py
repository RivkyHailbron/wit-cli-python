# from Repozitory import Repozitory
# print("hello")
# rep = Repozitory(r'C:\Users\user1\Documents\לימודים\PYTHON\project\tryWit')
# rep.init()
# rep.add("example.docx")
# rep.commit("4 commit")
# rep.log()
# rep.status()
# rep.checkout(4106073414087558925)
#
#
#
from myClick import Cli
import subprocess
import os

if __name__ == "__main__":
    current_directory = os.getcwd()  # קבלת הנתיב הנוכחי
    # print(f"current_directory ============{current_directory}")
    ui = Cli(current_directory)
    cli = ui.create_cli()
    cli()
