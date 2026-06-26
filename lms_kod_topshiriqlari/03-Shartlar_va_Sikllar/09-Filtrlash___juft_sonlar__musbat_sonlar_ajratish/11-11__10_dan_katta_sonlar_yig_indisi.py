n = int(input())
numbers = list(map(int, input().split()))

sum_gt10 = 0
for num in numbers:
    if num > 10:
        sum_gt10 += num
        
print(sum_gt10)