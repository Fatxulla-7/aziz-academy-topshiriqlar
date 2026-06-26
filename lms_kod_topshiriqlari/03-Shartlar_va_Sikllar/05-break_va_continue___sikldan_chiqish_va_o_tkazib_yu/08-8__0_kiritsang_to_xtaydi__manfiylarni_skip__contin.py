total = 0

while True:
    x = int(input())
    if x == 0:
        break
    if x < 0:
        continue
    total += x
    
print(total)