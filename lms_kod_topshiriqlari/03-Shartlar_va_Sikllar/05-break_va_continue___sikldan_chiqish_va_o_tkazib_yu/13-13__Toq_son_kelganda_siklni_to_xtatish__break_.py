total = 0

while True:
    x = int(input())
    if x % 2 != 0:
        break
    total += x
    
print(total)