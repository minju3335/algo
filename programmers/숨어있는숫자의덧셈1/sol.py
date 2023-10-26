def solution(my_string):

    answer = 0

    for n in my_string:
        if n.isdigit(): # 숫자라면 true
            answer += int(n)

    return answer

print(solution("aAb1B2cC34oOp"))


# 2
def solution(my_string):
    answer = 0
    for i in my_string:
        try:
            answer = answer + int(i)
        except: # 예외가 발생하면
            continue # 다음으로 넘어간다
    return answer
    
# 3
def solution(my_string):
    answer = 0
    for char in my_string:
        if ord('A') <= ord(char) <= ord('z'):
            an swer += int(char)

        return answer
