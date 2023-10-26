import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):

    # N은 큰 행렬의 크기, M은 파리채크기
    N, M = list(map(int,input().split()))

    # 파리가 존재하는 부분의 배열 만들기
    matrix = []
    for _ in range(N):
        numbers = list(map(int, input().split()))
        matrix.append(numbers)

    
    lst = [] # total을 담을 리스트 만들기
    # 파리채 만들기
    # +M을 생각해서 구간 정해주기
    for r in range(0, N - M + 1):
        for c in range(0, N - M +1):
            total = 0
            # 정해진 부분에 +M까지 반복 돌려주기
            for i in range(M):
                for j in range(M):
                    total += matrix[r+i][c+j]
            # MAX함수를 쓰기 위해 리스트에 넣기
            lst.append(total)
    
    # MAX함수로 최대한 많이 죽인 부분 구하기
    answer = max(lst)
    print(f'#{tc} {answer}')