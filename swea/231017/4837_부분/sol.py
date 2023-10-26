import sys
sys.stdin = open('input.txt')


A = list(range(1, 13))



lst2 = []
for i in range(1<<len(A)):
    lst = []
    for j in range(len(A)):
        if i & (1<<j):
            lst.append(A[j])
    lst2.append(lst)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    
    counter = 0
    for s in lst2:
        if len(s) == N and sum(s) == K:
            counter += 1
    print(f'#{tc} {counter}')



# 다른 풀이
for tc in range(1, T+1):
    numbers = list(range(1, 13))
    N, K = list(map(int, input().split()))

    count = 0

    for i in range(1 << len(numbers)):
        temp = []
        for j in range(len(numbers)):
            if i & (1 << j):
                temp.append(numbers[j])

        if len(temp) == N and sum(temp) == K:
            count += 1

    print(count)