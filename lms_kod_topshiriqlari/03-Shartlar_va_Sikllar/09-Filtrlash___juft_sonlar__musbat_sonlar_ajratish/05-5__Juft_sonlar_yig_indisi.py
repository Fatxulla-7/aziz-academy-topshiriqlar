n = int(input())
numbers = list(map(int, input().split()))

sum_even = 0
for num in numbers:
    if num % 2 == 0:
        sum_even += num
        
print(sum_even)