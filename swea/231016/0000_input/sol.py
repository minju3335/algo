import syssys.stdin = open('input.txt')

TC = int(input())

for i in range(TC):
    num = int(input())

    if num % 2 == 1:
        print('홀수')
    else:
        print('짝수')

# 1차원 리스트 input 받기
# numbers = input().split()

# print(numbers)
# print(type(numbers))
# for number in numbers:
#     int_num = int(number)

#     if int_num % 2 == 1:
#         print(f'{int_num}은 홀수입니다.')


# 2차원 리스트 입력

N = int(input())
matrix = []

for i in range(N):
    numbers = list(map(int, input().split()))
    matrix.append(numbers)


# 데이터 자체를 반복하기
for row in matrix:
    for iten in row:
        print(item)

# 행우선 반복 (inded접근)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(i, j, matrix[i][j])

# 열우선 반복 (index접근)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(j, i, matrix[j][i])

