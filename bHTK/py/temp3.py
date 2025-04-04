import math

start = input("수 입력: ")
end = input("수 입력: ")
def find_perfect_squares(start, end):
    perfect_squares = []
    for i in range(math.isqrt(start), math.isqrt(end) + 1):
        square = i * i
        if square >= start and square <= end:
            perfect_squares.append(square)
    return perfect_squares

find_perfect_squares(start, end)