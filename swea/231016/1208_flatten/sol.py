import sys
sys.stdin = open('input.txt')


T = 10

for tc in range(1, T+1):
    dump = int(input())
    numbers = list(map(int, input().split()))
    numbers_s = numbers.sort()

    l = len(numbers)
    for j in range(0, l):
        numbers_s[j] = numbers_s[j] + 1
        numbers_s[l-j-1] = numbers_s[l-j-1] - 1

    
    max_number = 0
    min_number = 0

    for k in range(0, len(numbers)):
        if numbers_s[0] >= max_number:
            numbers_s[k] = max_number
        else:
            numbers_s[k] = min_number
    
    answer = max_number - min_number
    print(f'#{i} {answer}')



for tc in range(1, T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for i in range(dump):
        # 최대높이
        top_box = boxes[0]
        top_box_idx = 0
        # 최소높이
        down_box = boxes[0]
        down_box_idx = 0

        # 최대와 최소 높이 찾기
        for i in range(len(boxes)):
            if top_box < boxes[i]:
                top_box = boxes[i]
                top_box_idx = i

            if down_box > boxes[i]:
                down_box = boxes[i]
                down_box_idx = if
        
        # top_box = max(boxes)
        # down = min(boxes)

        # 평탄화
        boxes[top_box_idx] -= 1
        boxes[down_box_idx] += 1

        # 전체 평탄화 횟수 전에 평탄화가 완료된 경우
        if boxes[top_box_idx] - boxes[down_box_idx] < 1:
            break

        result - max(boxes) - min(boexes)

        print(f'#{tc} {result}')