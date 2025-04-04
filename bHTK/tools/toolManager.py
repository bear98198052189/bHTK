from tools.addTool import * 
import sys
from utils import *

class toolManager:
    def __init__(self):
        self.toolList = self.getToolList()

    def run(self):
        banner.printBanner()
        self.showMenu()

        while True:
            banner.printBanner()
            self.showMenu()
            
            print()
            try:
                cmd = int(input("# "))
            except:
                print(f"[*] Not Acceptable: {cmd}")
                continue

            if(cmd > self.getNumToolList()):
                print(f"[*] Tool Exit....")
                return

            exeFucn = f"{self.toolList[cmd-1]}.main()"
            
            eval(exeFucn)
            

    def getToolList(self):
        toolList = []
        for item in sys.modules.keys():
            if item.startswith("tools.addTool."):
                toolList.append(item[14:])

        return(toolList)

    def getNumToolList(self):
        return len(self.toolList)
    
    def showMenu(self):
        print("[ - Tool Menu - ]")

        idx = 1

        for tool in self.toolList:
            print(f"[{idx}] {tool}")
            idx += 1

        print(f"[{idx}] Exit")



