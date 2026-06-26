n = int(input())
s = list(map(int, input().split()))

for i in range(n):
    if s[i] % 2 == 0:
        print(s[i])