n = int(input())

sonlar = []
while len(sonlar) < n:
    sonlar.extend(map(int, input().split()))
    
juft_sonlar = []

for x in sonlar:
    if x % 2 == 0:
        juft_sonlar.append(x)
        
if juft_sonlar:
    mini = juft_sonlar[0]
    for x in juft_sonlar:
        if x < mini:
            mini = x
    print(mini)
else:
    print("No")