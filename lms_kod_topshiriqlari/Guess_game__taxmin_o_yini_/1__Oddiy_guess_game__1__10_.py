secret = 7

while True:
    n = int(input())
    if n < secret:
        print("Low")
    elif n > secret:
        print("High")
    else:
        print("Correct")
        break