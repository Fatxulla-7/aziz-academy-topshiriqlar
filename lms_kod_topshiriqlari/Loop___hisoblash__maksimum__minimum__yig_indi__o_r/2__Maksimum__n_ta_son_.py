n = int(input())
sonlar = list(map(int, input().split()))

maks = sonlar[0]
for x in sonlar:
    if x > maks:
        maks = x
        
print(maks)