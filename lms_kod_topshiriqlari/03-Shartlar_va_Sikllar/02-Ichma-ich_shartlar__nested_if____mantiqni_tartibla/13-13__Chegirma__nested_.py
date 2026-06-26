price = float(input())

if price >= 100:
    if price >= 500:
        price *= 0.8 
    else:
        price *= 0.9 
        
print(price)