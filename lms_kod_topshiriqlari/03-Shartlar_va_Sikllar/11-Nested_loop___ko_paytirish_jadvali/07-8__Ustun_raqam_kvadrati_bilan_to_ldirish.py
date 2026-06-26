n, m = map(int, input().split())

row = " ".join(str(j) for j in range(1, m + 1))
for _ in range(n):
    print(row)