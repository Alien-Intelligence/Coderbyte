# 프로젝트 오일러 1번 // 1000미만의 자연수 중 3 또는 5의 배수를 모두 더한 값 구하기
sum = 0
for i in range(1,1000):
    if i % 3 == 0:
        sum = sum+i
    elif i%5 == 0:
        sum = sum+i

print (sum)