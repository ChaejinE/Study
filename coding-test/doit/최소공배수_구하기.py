T = int(input())


def gcd(a, b):
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
