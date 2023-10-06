import sys
sys.stdin = open('input.txt') # standard input

TC = int(input()) # test case

for i in range(TC):
    num = int(input())

    if num % 2 == 1:
        print('홀수')
    else:
        print('짝수') # 단일 숫자 데이터를 가져오는 방법



# 1차원 리스트 input 받기
# 1
# numbers = input().split()

# 리스트로 바꿔주기
# print(numbers)
# print(type(numbers))

# for number in numbers:
#     int_num = int(number)

#     if int_num % 2 == 1:
#         print(f'{int_num}은 홀수입니다.')


# 2
numbers = list(map(int, input().split()))

for number in numbers:
    if number % 2 == 1:
        print(f'{number}은 홀수입니다.')