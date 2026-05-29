n = int(input())
sonlar = list(map(int, input().split()))

yigindi = 0
for son in sonlar:
    yigindi += son
    
ortacha = yigindi / n 

count = 0
for son in sonlar:
    if son > ortacha:
        count += 1
        
print(count)