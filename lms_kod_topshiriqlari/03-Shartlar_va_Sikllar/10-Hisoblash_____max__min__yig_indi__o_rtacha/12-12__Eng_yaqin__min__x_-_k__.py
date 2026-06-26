n = int(input())
sonlar = list(map(int, input().split()))
k = int(input())

eng_yaxshi = sonlar[0]
eng_masofa = abs(sonlar[0] - k)

for son in sonlar:
    masofa = abs(son - k)
    if masofa < eng_masofa:
        eng_masofa = masofa
        eng_yaxshi = son
    elif masofa == eng_masofa:
        if son < eng_yaxshi:
            eng_yaxshi = son
            
            
print(eng_yaxshi)