n = int(input())
sonlar = list(map(int, input().split()))

maks = sonlar[0]
minn = sonlar[0]

for son in sonlar:
    if son > maks:
        maks = son
    if son < minn:
        minn = son
        
print(maks, minn)