import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    # 정수 개수 N, 구간 개수 M 받기
    N, M = list(map(int, input().split()))
    # N개의 정수 받기
    num = list(map(int, input().split()))

    lst = []
    for i in range(0, N - M +1):
        # N개의 정수 중에 M개의 구간 슬라이싱
        number = num[i:i+M]
        # 슬라이싱한 구간의 합 구해서 리스트에 넣기
        s = sum(number)
        lst.append(s)

    #구한 합의 리스트 중에 max, min 구해서 차를 구하기
    max_num = max(lst)
    min_num = min(lst)
    answer = max_num - min_num

    print(f'#{tc} {answer}')
