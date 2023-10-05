import sys
sys.stdin = open('input.txt')

char = input()

if char.isalpha():
        
    # 소문자인 경우
    if char.islower():
        result = char.upper()

    # 대문자인 경우
    else:
        result = char.lower()

    print(f'{char}(ASCII: {ord(char)}) => {result}(ASCII: {ord(result)})')

else:
    print(char)