a, b, c = map(int, input().split())

result = (a % 2 == 0 and b % 2 == 0) or (c == 0)
print(result)