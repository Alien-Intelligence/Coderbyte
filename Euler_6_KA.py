# 프로젝트 오일러 6번 // 1부터 100까지 "제곱의 합"과 "합의 제곱"의 차는?

num1 = 0
num2 = 0

for i in range(1,101):
    num1 = num1+ i**2
    num2 = num2 +i

num2 = num2**2

sol = num2 - num1

print (sol)