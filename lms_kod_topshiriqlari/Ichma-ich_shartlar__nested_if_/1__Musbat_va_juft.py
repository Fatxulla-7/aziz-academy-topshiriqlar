a = int(input())

if a > 0:
    if a & 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Not positive")