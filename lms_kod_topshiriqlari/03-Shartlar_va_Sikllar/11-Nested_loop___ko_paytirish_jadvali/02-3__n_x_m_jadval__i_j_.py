n, m = map(int, input().split())

for i in range(1, n + 1):
    row = []
    for j in range(1, m + 1):
        row.append(str(i * j))
    print(" ".join(row))
