def solution(n, k):
    
    s = n // 10
    answer = 12000 * n + 2000 * (k - s)
        
    return answer

    # 2
def solution(n, k):
    return 12000 * n + 2000 * (k - n // 10)