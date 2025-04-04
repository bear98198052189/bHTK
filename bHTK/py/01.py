# 성적 관리 프로그램
# 학생 점수 입력 받고 점수에 따라 컨설팅
try:
    score = int(input("점수를 입력해주세요: "))
    
    if(score==100):
        print("잘했어요~")
    elif(score>=80):
        print("괜찮아요~")
    elif(score>=40):
        print("노력해요~")
    else:
        print("공부 안 했니?")
except:
    print("점수는 숫자를 입력해야합니다.")
    exit()

