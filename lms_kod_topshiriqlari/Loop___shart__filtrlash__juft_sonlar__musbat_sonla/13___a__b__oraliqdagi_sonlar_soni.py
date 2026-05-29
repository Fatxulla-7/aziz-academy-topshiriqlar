n = int(input())
numbers = list(map(int, input().split()))
a, b = map(int, input().split())

count = 0
for num in numbers:
    if a <= num <= b:
        count += 1
        
print(count)