a, b = map(int, input().split())

ekub = 1
for i in range(1, min(a,b) + 1):
    if a % i == 0 and b % i == 0:
        ekub = i 
        
        
print(ekub)