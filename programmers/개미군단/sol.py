def solution(hp):
    answer = 0

    a, b = divmod(hp, 5)
    hp = b
    answer += a

    a, b = divmod(hp, 3)
    hp = b
    answer += a

    answer += hp

    return answer

# 위를 줄인 것
def solution(hp):
    answer = (hp // 5) + ((hp % 5) // 3) + ((hp % 5) % 3)
    return answer