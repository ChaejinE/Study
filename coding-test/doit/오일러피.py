N = 15

check_list = list(range(0, N + 1))
check_list[1] = 1
for i in range(2, N + 1):
    if i == check_list[i]:
        for j in range(i, N + 1):
            if j % i == 0:
                check_list[j] -= check_list[j] // i

print(check_list[N])
