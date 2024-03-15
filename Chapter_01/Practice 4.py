# 연습문제 1장 4번
# 유클리드 알고리즘(알고리즘1.7)에 중간과정을 나타내는 코드를 추가한 프로그램
# 학번 202110075 권준영
def gcd(a, b):
    print("gcd", (a, b))
    while b != 0 :
        r = a % b
        print("gcd", (b, r))
        a = b
        b = r
    return a
print("60과 28의 최대공약수 =", gcd(60,28))