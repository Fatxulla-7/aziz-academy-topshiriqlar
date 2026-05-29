n = int(input())
sonlar = list(map(int, input().split()))

mini = sonlar[0]
for x in sonlar:
    if x < mini:
        mini = x
        
print(mini)