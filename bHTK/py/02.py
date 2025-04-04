# while(True):
#     str = input("명령어를 입력하세요: ")
#     if(str=="exit"):
#         exit()
#     elif(len(str)<10):
#         print("'" + str + "'" + "명령어를 실행했습니다.")
#     else:
#         print("잘못됐어요")

while(True):
    cmd = input(">")

    if(cmd == "exit"):
        break
    if(len(cmd)>10):
        print("잘못된 명령어입니다.")
        continue
print(cmd + "명령어를 실행했습니다.")