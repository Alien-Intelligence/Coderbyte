# 프로젝트 오일러 5번 // 	1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수
s=1

while 1:
    li = []
    for i in range(1,21):
        if s % i == 0:
            li.append('o')
    if li.count('o') == 20:
        break
    else:
        s = s+1


print (s)


