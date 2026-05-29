n = int(input())
numbers = list(map(int, input().split()))

sum_odd = 0
for num in numbers:
    if num % 2 != 0:
        sum_odd += num
        
print(sum_odd)