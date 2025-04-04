import subprocess

def main():
    print("\033[31m\033[40m[+] BEAR Shell For Hacking")
    cmdDict = {"ifconfig":"ipconfig", "pwd": "cd ,","cat":"type","ls":"dir" }

    while True:
        cmd = input("\033[95mHacking # ")

        for c in cmdDict:
            cmd = cmd.replace(c, cmdDict[c])

        cmdList = cmd.split()
            
        if(cmd=="exit"):
            print("[+] End")
            return("\033[30m프로그램이 종료되었습니다. - Hacking TOOL")

        subprocess.run(cmdList, shell=True)
