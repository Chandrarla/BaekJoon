alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alpha_num = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
sum = 0

num, radix = input().split()
# 진법 계산은 오른쪽부터 시작하기에 입력값 reverse 시켜주었다
num = "".join(reversed(num))

for i in range(len(num)):
    # 10진법을 넘어가서 알파벳으로 표기되는 경우를 나눈다
    if num[i] in alphabet:

        sum += alpha_num[alphabet.index(num[i])]*(int(radix)**i)
    else:
        sum += int(num[i])*(int(radix)**i)

print(sum)