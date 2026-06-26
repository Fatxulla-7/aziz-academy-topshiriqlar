n = int(input())

sonlar = []
while len(sonlar) < n:
    sonlar.extend(map(int, input().split()))
    
maks = sonlar[0]
index = 0

for i in range(n):
    if sonlar[i] > maks:
        maks = sonlar[i]
        index = i 
        
print(index)