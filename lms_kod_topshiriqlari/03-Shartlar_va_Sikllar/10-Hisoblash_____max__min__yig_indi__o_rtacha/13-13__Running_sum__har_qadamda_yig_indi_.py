n = int(input())
sonlar = list(map(int, input().split()))

yigindi = 0
for son in sonlar:
    yigindi += son
    print(yigindi)