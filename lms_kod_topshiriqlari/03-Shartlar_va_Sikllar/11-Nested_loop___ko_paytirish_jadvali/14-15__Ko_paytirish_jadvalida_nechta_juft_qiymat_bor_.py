n, m = map(int, input().split())

count = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (i * j) % 2 == 0:
            count += 1
            
print(count)