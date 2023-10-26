import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    # 10의배수인 가로크기 N
    N = int(input())
    
    lst = [0, 1, 3]

    for i in range(3, N//10+1):    
        answer = lst[i-1] + lst[i-2] * 2

    print(f'#{tc} {answer}')



