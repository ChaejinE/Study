N = 30

check_list = [True] * (N + 1)
for i in range(2, N + 1):
    if check_list[i] == False:
        continue

    for j in range(i + 1, N + 1):
        if check_list[j] and j % i == 0:
            check_list[j] = False

check_list[0] = False
check_list[1] = False
for idx, check in enumerate(check_list):
    if check:
        print(idx, end=" ")
