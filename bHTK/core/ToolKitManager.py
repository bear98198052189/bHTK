from utils import *
from tools import *
class Manager:
    def __init__(self):
        self.toolList = []
        self.toolmanager = toolManager.toolManager()

    def run(self):


        while True:
            banner.printBanner()
            self.showMenu()
            print()
            cmd = input("# ")

            if cmd == "1":
                banner.clearConsole()
                self.toolmanager.run()
            elif cmd == "2":
                banner.clearConsole()
                BearShell.main()
            elif cmd == "3":
                banner.clearConsole()
                exit("[-] Good Bye")
            else:
                banner.clearConsole()
                print(f"[*] Not Acceptable: {cmd}")

    def showMenu(self):
        print("[ - Menu - ]")
        print(f"[1] Tools: {self.toolmanager.getNumToolList()} Available")
        print("[2] Shell")
        print("[3] Exit")


