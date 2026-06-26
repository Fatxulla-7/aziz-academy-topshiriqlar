n = int(input())
lst = list(map(int, input().split()))
x = int(input())
index = -1

for i in range(len(lst)):
    if lst[i] == x:
        index = i 
        break
        
print(index)