import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    # 문자열 입력받기
    text = list(input())
    # 중복되지 않은 문자 받을 리스트 작성
    stack = []

    # 입력받은 문자열 내에서 하나씩 꺼내기
    for i in text:
        
        # stack리스트가 비었다면 추가
        if len(stack) == 0:
            stack.append(i)

        # 비어있지 않다면 밑의 조건을 따져야 함함    
        else:
            # 만약 stack의 마지막 인자와 i가 같다면 삭제
            if i == stack[-1]:
                stack.pop()
            # 같지 않다면 추가
            else:
                stack.append(i)
    
    # text의 끝까지 반복 끝내면 길이가 개수일테니 구해준다
    answer = len(stack)

    print(f'#{tc} {answer}')