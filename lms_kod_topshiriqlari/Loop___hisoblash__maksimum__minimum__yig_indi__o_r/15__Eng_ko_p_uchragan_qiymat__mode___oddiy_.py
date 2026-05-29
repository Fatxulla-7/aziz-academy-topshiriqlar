n = int(input())
sonlar = list(map(int, input().split()))

eng_chastota = 0
eng_son = sonlar[0]

for i in range(n):
    count = 0
    for j in range(n):
        if sonlar[j] == sonlar[i]:
            count+= 1
            
    if count > eng_chastota or (count == eng_chastota and sonlar[i] < eng_son):
        eng_chastota = count
        eng_son = sonlar[i]
        
print(eng_son)