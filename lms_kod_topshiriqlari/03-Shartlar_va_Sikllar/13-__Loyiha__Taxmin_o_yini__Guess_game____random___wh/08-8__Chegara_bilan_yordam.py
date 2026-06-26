secret = 15

while True:
    x = int(input())
    
    if x == secret:
        print("Correct")
        break
    elif abs(x - secret) > 5:
        print("Far")
    else:
        print("Close")