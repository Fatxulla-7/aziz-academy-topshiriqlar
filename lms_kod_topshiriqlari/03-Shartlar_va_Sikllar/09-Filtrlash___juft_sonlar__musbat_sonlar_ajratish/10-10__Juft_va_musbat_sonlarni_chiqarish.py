n = int(input())
numbers = list(map(int, input().split()))

for num in numbers:
    if num > 0 and num % 2 == 0:
        print(num)