n = int(input())
sonlar = list(map(int, input().split()))

yigindi = 0
count = 0

for x in sonlar:
    yigindi += x
    count += 1
    
    
ortalama = yigindi / count
print(ortalama)