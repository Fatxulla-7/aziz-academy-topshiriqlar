n = int(input())

sonlar = list(map(int, input().split()))

yigindi = 0

for i in range(n):
    yigindi += sonlar[i]
    
print(yigindi)