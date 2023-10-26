def solution(rsp):
    answer = ''
    
    for i in rsp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        else:
            answer += '2'
    
    return answer


# 다른 풀이
def solution(rsp):
    d = {'0': '5', '2': '0', '5': '2'}
    # for char in rsp
    # answer += d[char]
    return ''.join(d[i] for i in rsp)