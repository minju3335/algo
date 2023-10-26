def solution(message):
    answer = 0
    m_list = list(''.join(message))

    for i in m_list:
        answer += 1
    return answer * 2

print(solution("happy birthday!"))

# 2
def solution(message):
    return len(message) * 2

print(solution("happy birthday!"))