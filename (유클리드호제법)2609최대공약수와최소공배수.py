a, b = map(int, input().split())
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        res = gcd(b, a % b)
        return res
#a와 b의 최대공약수는, b와 r의 최대공약수와 같다
#이를 이용해 재귀로 들어가면됨
#a와 b의 최소공배수는, a와 b를 곱한것을 a와 b의 최대공약수로 나누면 된다.
r = gcd(a, b)
print(r)
print(int((a*b)/r))
#https://www.acmicpc.net/problem/2609