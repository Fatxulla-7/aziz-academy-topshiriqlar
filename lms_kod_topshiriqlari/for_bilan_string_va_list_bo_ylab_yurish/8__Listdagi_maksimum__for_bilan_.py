n = int(input())

sonlar = list(map(int, input().split()))

eng_katta = sonlar[0]

for i in range(1, n):
    if sonlar[i] > eng_katta:
        eng_katta = sonlar[i]
        
print(eng_katta)