n = int(input())

sonlar = []
while len(sonlar) < n:
    sonlar.extend(map(int, input().split()))

maks = sonlar[0]
mini = sonlar[0]

for x in sonlar:
    if x > maks:
        maks = x
    if x < mini:
        mini = x
        
        
print(maks - mini)