# import time
# start = time.time()

N = int(input())
numbers = [ int(num) for num in input()]

result = 0
for i in range(N):
    result += numbers[i]

print(result)
# print(f"Answer : {result}")
# print(f"Consumed time : {time.time() - start}")
