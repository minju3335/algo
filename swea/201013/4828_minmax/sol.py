import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T+1):
    N = int(input())

    numbers = list(map(int, input().split()))

    max = 0
    min = 0

    for i in range(0, len(numbers)):
        if numbers[i] >=  max:
            max = numbers[i]
        else:
            min = numbers[i]
    
    print(f'#{i} {max - min}')


# 2
# for tc in range(1, T+1):
#     N = int(input())

#     numbers = list(map(int, input().split()))

#     min_number = 1000000
#     max_number = 0

#     for number in numbers:
#         if min_number > number:
#             min_number = number
        
#         if max_number < number:
#             max_number = number
        
#         result = max_number - min_number

#     print(f'#{T} {result}')

