import random

random_num = random.randrange(1, 101)
print(f"디버그: 생성된 랜덤 숫자: {random_num}")

def calculate(num):
    if num > random_num:
        print("down!")
    elif num < random_num:
        print("up!")
    else:
        print("정답입니다!!")

while True:
    user_num = int(input("숫자를 입력하세요!: "))
    calculate(user_num)
    if user_num == random_num:
        break
