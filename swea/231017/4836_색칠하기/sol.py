import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    rc = [[0 for _ in range(10)] for _ in range(10)] # 빈 행렬 만들기
    counter = 0 # 세어줄 변수 만들기
    N = int(input())

    for i in range(1, N+1):
        # 해당하는 인덱스와 색상정보 받기
        row1, col1, row2, col2, color = map(int, input().split())

        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                if color == 1: # 색상이 빨강이라면
                    if rc[row][col] == 0: # 아무색도 아닐 때
                        rc[row][col] = 1 # 빨강으로 칠해주고
                    elif rc[row][col] == 2: # 파랑색일 떄
                        rc[row][col] =3 # 보라색으로 칠해주고
                        counter += 1 # 1개를 세어준다
                else: # 색상이 파랑이라면
                    if rc[row][col] == 0: # 아무색도 아닐 때
                        rc[row][col] = 2 # 파랑으로 칠해주고
                    elif rc[row][col] == 1: # 빨강색일 때
                        rc[row][col] = 3 # 보라색으로 칠해주고
                        counter += 1 # 1개를 세어준다
    print(f'#{tc} {counter}')