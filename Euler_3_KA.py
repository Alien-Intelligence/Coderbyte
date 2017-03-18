# 프로젝트 오일러 3번 // 가장 큰 소인수 구하기

def sosu(s):
    for i in range(2, int(s**(1/2)+1)):
        if s % i == 0:
            return 0
    return 1
num = 600851475143
for j in range(1, 10000):
    if num % j ==0:
        if sosu(j) == 1:
            sol = j

num = num / sol

for j in range(1, int(num)):
    if num % j ==0:
        if sosu(j) == 1:
            solu = j

if solu >sol:
    print (solu)
else:
    print(sol)




