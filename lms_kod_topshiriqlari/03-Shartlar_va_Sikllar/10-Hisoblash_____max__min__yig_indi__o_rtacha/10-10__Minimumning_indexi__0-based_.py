n = int(input())

sonlar = []
while len(sonlar) < n:
    sonlar.extend(map(int, input().split()))
    
mini = sonlar[0]
index = 0

for i in range(n):
    if sonlar[i] < mini:
        mini = sonlar[i]
        index = i 
        
print(index)