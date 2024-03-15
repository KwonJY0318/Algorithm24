# 연습문제 1장 26번
# 집합의 A와B가 진부분집합인지 검사하는 프로그램
# 학번 20110075 권준영

Alist = {1,2,4,5,7}
Blist = {1,2,4,5,7,11,12}

print("A = ", Alist)
print("B = ", Blist)
print("진부분집합인가?")

if Blist > Alist:
    print("true")
else :
    print("fales")