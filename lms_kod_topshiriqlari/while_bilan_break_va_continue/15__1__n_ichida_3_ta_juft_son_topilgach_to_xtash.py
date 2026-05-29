n = int(input())

i = 1 
count = 0

while i <= n:
    if i % 2 == 0:
        count += 1
        if count == 3:
            print(i)
            break
            
    i += 1 
else:
    print("No")