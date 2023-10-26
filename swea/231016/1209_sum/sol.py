import sys
sys.stdin = open('input.txt')

T = 10
N = int(input())
for tc in range(1, N+1):
    l = [list(map(int, input().split())) for _ in range(10)]
    print(l)
    # lst1 = []
    # lst2 = []
    # lst3 = []

    # for i in range(0, 10):
    #     lst1.append(l[i][i])
        
    # lst_sum = sum(lst)



T = 10

for tc in range(1, T+1):
    tc = int(input())

    matrix = []

    # i, j, a 반복문들 돌리는 변수를 지정
    # _ => 변수를 활용하지 않은 예정
    for _ in range(100):
        numbers = list(map(int, input().split()))
        matrix.append(numbers)

    max_total = 0

    for row in range(len(matrix)):
        total = 0
        for col in range(len(matrix[0])):
            total += matrix[row][col]

        if max_total < total:
            max_total = total:

    for col in range(100):
        total = 0
        for row in range(100):
            total += matrix[row][col]
        
        if max_total < total:
            max_total = total

    # 좌상단 => 우하단 대각서
    total = 0
    for i in range(100):
        total += matrix[i][i]

    if max_total < total:
        max_total = total

    # 우상단 => 좌하단 대각선
    total = 0
    for i in range(100):
        total += matrix[i][99-i]

    if max_total < total:
        max_total = total

    print(max_total)