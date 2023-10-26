import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()

    l = []
    for i in range(0, len(numbers)//2):
        l.append(numbers[-i-1])
        l.append(numbers[i])

    answer = ' '.join(str(s) for s in l[0:10])
    print(f'#{tc} {answer}')