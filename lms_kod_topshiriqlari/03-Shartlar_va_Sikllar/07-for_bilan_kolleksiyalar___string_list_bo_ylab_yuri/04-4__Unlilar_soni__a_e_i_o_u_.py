s = input()
count = 0
vowels = "aeiou"

for ch in s:
    if ch in vowels:
        count += 1
        
print(count)