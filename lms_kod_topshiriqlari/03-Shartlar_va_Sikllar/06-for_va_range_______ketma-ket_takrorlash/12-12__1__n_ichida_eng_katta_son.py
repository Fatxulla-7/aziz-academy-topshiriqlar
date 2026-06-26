n = int(input())

max_num = 1
for i in range(1, n + 1):
    if i > max_num:
        max_num = i 
        
print(max_num)