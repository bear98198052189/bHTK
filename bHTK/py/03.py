numList = range(1, 101)

for num in numList:
    if num % 2 == 0:
        print(str(num) + ": 짝수")
    else:
        print("{}: 홀수".format(num))
