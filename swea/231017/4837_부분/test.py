numbers = ['a', 'b', 'c', 'd']

n = len(numbers)

for i in range(1<<n):
    
    temp = []
    for j in range(n):

        if i & (1<<j): # 해당 숫자가 있는지 없는지
            temp.append(numbers[j])
    print(temp)

# 모든 경우의 수를 알 수 있는 코드이다.
# 부분집합을 만드는 가장 쉬운 코드이긴 함.