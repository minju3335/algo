def solution(num_list):
    answer = []
    length = len(num_list)

    for i in range(1, length+1):
        answer.append(num_list[-i])
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1,0,1,1,1,3,5]))




# 2
def solution(num_list):
    N = length(num_list)
    
     for i in range(N):
        answer.append(num_list[N-1-i])


# 3
def solution(num_list):
    answer = []
    # answer = num_list[::-1]
    num_list.reverse()
    answer = num_list
    return answer