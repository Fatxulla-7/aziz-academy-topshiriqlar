n = int(input())

if n < 2:
    print("No")
else:
    found = False
    
    for i in range(2, n + 1):
        tub = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                tub = False
                break
                
        if tub:
            print(i)
            found = True
            break
            
    if not found:
        print("No")