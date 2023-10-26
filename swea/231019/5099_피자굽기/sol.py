import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    #화덕의 크기 N과 피자 개수 M
    N, M = list(map(int, input().split()))

    C = list(map(int, input().split()))

    for i in range(0, N):