# 프로젝트 오일러 7번 // 10001번째의 소수

def sosu(s):
    for i in range(2,int(s**(1/2))+1):
        if s % i ==0:
            return "아님"
    return "소수"
num = 0
i=2
while 1:
    if sosu(i) == "소수":
        num = num +1
    if num == 10001:
        break
    i = i+1

print (i)