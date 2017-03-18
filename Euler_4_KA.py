# 프로젝트 오일러 4번 // 세자리 수를 곱해 만들 수 있는 가장 큰 대칭수

ma = 0
for i in range(100,1000):
    for j in range(100,1000):
        mul = j*i
        m = str(mul)
        if m[::-1] == m:
            if mul > ma:
                ma = mul

print(ma)