# 프로젝트 오일러 9번 // a + b + c = 1000 이 되는 피타고라스 수


for a in range(1,1000):
    for b in range(1,1000):
        for c in range(1,1000):
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print("a = %d, a = %d, a = %d, a*b*c = %d" % (a,b,c,a*b*c))