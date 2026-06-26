n = int(input())

s = list(map(int, input().split()))

ek = s[0]

for i in range(1, n):
    if s[i] < ek:
        ek = s[i]
        
print(ek)