# 프로젝트 오일러 2번 // 피보나치 수열 중 짝수이면서 4백만 이하인 모든항을 더한 값
sum = 0
p1 = 1
p2 = 2
p3 = 3


while p3 <=4000000:
    if p3 % 2 == 0 :
        sum = sum + p3
    p1 = p2
    p2 = p3
    p3 = p1 + p2

sum = sum +2
print(sum)




