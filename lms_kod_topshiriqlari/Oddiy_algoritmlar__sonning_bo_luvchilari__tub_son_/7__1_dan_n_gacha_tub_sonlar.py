n = int(input())

for x in range(2, n + 1):
    is_prime = True
    for i in range(2, x):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        print(x)