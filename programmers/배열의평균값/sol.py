def solution(numbers):

    sum = 0
    length = len(numbers)
    for i in numbers:
        sum += i
    
    answer = sum / length
    return answer


print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))