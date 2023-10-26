def solution(numbers):
    numbers.sort(reverse = True)
    answer = numbers[0] * numbers[1]
    return answer
print(solution([1, 2, 3, 4, 5]))


# 다른 풀이
def solution(numbers):
    answer = 0
    max = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            if max < numbers[i] * numbers[j]:
                max = numbers[i] * numbers[j]
        return max



def solution(numbers):
    answer = 0
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            multi = numbers[i] * numbers[j]

            if answer < multi:
                answer = multi
        return answer