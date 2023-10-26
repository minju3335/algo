def solution(array, n):
    answer = 0

    for num in range(0, len(array)):
        if array[num] == n:
            answer += 1

    return answer

print(solution([1, 1, 2, 3, 4, 5], 1))

# 2
def solution(array, n):
    return array.count(n)
