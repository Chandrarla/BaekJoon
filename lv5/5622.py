text = input()

sum = 0
num = [0]*10
print(num)
num[1] = ''
num[2] = 'ABC'
num[3] = 'DEF'
num[4] = 'GHI'
num[5] = 'JKL'
num[6] = 'MNO'
num[7] = 'PQRS'
num[8] = 'TUV'
num[9] = 'WXYZ'

print(num)
for i in text:
    for j in range(1, 10):
        if i in num[j]:
            sum += 2*j
            print(sum)