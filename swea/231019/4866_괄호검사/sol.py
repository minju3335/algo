import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    text = input()
    stack = []
    result = 0

    for i in range(len(text)):

        if text[i] == "(" or text[i] == "{":
            stack.append(text[i])
        elif text[i] == ")" or text[i] == "}":
            if len(stack) == 0:
                stack = [text[i]]
                break
            elif (text[i] == "}" and stack[-1] != "{") or (text[i] == ")" and stack[-1] != "("):
                stack = [text[i]]
            else:
                stack.pop()

    if len(stack) == 0:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}') 