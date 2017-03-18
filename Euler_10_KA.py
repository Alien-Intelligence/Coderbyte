# 프로젝트 오일러 10번 // 이백만 이하 소수의 합


def sosu(s):
    for i in range(2,int(s**(1/2))+1):
        if s % i ==0:
            return "아님"
    return "소수"
sum = 0
for j in range(2,2000000):
    if sosu(j) == "소수":
        sum = sum+ j

print (sum)