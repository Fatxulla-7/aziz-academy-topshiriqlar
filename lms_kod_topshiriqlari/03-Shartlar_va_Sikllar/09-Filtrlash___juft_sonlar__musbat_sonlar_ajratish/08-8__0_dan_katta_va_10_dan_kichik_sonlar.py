n = int(input())
numbers = list(map(int, input().split()))

for num in numbers:
    if 0 < num < 10:
        print(num)