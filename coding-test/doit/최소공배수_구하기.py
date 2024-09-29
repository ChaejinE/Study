T = int(input())


def gcd(a, b):
    """
    b > a 라면 ? 가령 gcd(6, 10)으로 들어온다면 a = 6, b = 10 이므로
    gcd(10, 6 % 10 = 6) 으로 자동 swap이 되기때문에 작은 수와 큰 수의 위치를 신경쓰지 않아도된다.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


results = []
for i in range(T):
    a, b = map(int, input().split())
    results.append(a * b // gcd(a, b))

for result in results:
    print(result)
