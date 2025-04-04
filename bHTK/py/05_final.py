# 가위바위보 게임
# 생명, 베팅코인
# 0 = 가위 1 = 바위 2 = 보

import random as r




def gababo_cal(user_choice, dealer_choice, default_user_coin, user_life):
    if user_choice == dealer_choice:
        print("딜러: {} 무승부입니다! 현재코인: {:.0f} 현재 체력: {}".format(dealer_choice, default_user_coin, user_life))
    elif (user_choice == 0 and dealer_choice == 2) or (user_choice == 1 and dealer_choice == 0) or (user_choice == 2 and dealer_choice == 1):
        default_user_coin += default_user_coin  # 코인 2배 지급
        print("딜러: {} 승리하였습니다! 코인 2배 지급! 현재코인: {:.2f} 현재 체력: {}".format(dealer_choice, default_user_coin, user_life))
    else:
        reduction = default_user_coin * 0.02
        default_user_coin -= reduction
        user_life -= 1
        print("딜러: {} 패배하였습니다!! 생명 -1 현재코인: {:.0f} 현재 체력: {}".format(dealer_choice, default_user_coin, user_life))
    return default_user_coin, user_life

user_life = 10 # 유저 생명
default_user_coin = 100 # 기본 지급 코인
while True:
    start = input("가위바위보 게임을 시작하시겠습니까?(Y or N ㅣ 현재 상태보기 S): ")

    if(start == "Y" or start == "y"):
        dealer_choice = r.randrange(0,3)
        user_bet = int(input("베팅해주세요.(1~{}): ".format(default_user_coin)))

        if user_bet > default_user_coin or user_bet <= 0: 
            print("베팅을 잘 못하셨습니다")
            continue

        user_choice = str(input("가위 바위 보 중 선택하세요: "))
        if user_choice == "가위" or user_choice == "바위" or user_choice == "보":
            gababo_cal(user_choice, dealer_choice, default_user_coin, user_life)
        else:
            print("다시 입력하세요")
            continue

    elif(start == "s"):
        print("현재코인: {:.0f} 현재 체력: {}".format(default_user_coin, user_life))
    else:
        print("프로그램을 종료합니다.")
        exit()


user_life = 10 # 유저 생명
default_user_coin = 100 # 기본 지급 코인