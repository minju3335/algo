def solution(numbers):
    answer = []

    for num in numbers:
        answer.append(num * 2)
    return answer


print(solution([1, 2, 3, 4, 5]))