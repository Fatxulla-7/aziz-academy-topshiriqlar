n = int(input())
numbers = list(map(int, input().split()))

for num in numbers:
    if num < 0:
        print(num)