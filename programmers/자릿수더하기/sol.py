def solution(n):
    s = str(n)
    l = list(''.join(s))
    answer = 0

    for i in l:
        answer += int(i)
        
    return answer

print(solution(1234))
print(solution(930211))


# 2
def solution(num_list):
    answer = []
    # answer = num_list[::-1]
    num_list.reverse()
    answer = num_list
    return answer