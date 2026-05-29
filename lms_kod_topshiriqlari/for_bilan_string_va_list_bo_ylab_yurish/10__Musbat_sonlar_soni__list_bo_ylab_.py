n = int(input())
s = list(map(int, input().split()))
s1 = 0

for i in range(n):
    if s[i] > 0:
        s1 += 1
        
print(s1)