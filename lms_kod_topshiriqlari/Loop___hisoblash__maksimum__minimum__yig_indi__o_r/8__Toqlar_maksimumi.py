n = int(input())

sonlar = []
while len(sonlar) < n:
    sonlar.extend(map(int, input().split()))
    
toq_sonlar= []

for x in sonlar:
    if x % 2 != 0:
        toq_sonlar.append(x)
        
if toq_sonlar:
    maks = toq_sonlar[0]
    for x in toq_sonlar:
        if x > maks:
            maks = x
    print(maks)
else:
    print("No")