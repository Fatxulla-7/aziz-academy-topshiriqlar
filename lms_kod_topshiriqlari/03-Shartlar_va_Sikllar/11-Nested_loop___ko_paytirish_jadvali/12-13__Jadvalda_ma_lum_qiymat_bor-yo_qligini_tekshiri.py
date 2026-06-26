n, m = map(int, input().split())
x = int(input())

found = False

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i * j == x:
            found = True
            break
    if found:
        break
        
if found:
    print("Yes")
else:
    print("No")