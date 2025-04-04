import os

banner_text = """
                                                                                                       
88           88        88  888888888888  88      a8P       888888888888                            88  
88           88        88       88       88    ,88'             88                                 88  
88           88        88       88       88  ,88"               88                                 88  
88,dPPYba,   88aaaaaaaa88       88       88,d88'                88        ,adPPYba,    ,adPPYba,   88  
88P'    "8a  88\"\"\"\"\"\"\"\"88       88       8888"88,               88       a8"     "8a  a8"     "8a  88  
88       d8  88        88       88       88P   Y8b              88       8b       d8  8b       d8  88  
88b,   ,a8\"  88        88       88       88     \"88,            88       "8a,   ,a8"  "8a,   ,a8"  88  
8Y"Ybbd8"'   88        88       88       88       Y8b           88        `"YbbdP"'    `"YbbdP"'   88  
BEAR Hacking Tool Kit Ver 0.2

Author: LJH
Contact: michinGunMan@hotmail.com
                                                                                                
"""

def printBanner():
    clearConsole()
    print(banner_text)


def clearConsole():
    cmd = 'clear'
    if os.name in ('nt', 'dos'):
        cmd = 'cls'
    os.system(cmd)