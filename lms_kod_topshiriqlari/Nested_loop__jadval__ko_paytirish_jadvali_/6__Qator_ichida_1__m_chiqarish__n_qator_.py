n, m = map(int, input().split())

row = " ".join(str(i) for i in range(1, m + 1))
for _ in range(n):
    print(row)