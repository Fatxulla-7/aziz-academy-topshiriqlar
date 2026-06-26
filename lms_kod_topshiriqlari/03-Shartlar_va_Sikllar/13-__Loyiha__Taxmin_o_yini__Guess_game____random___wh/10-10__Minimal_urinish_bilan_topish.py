secret = 1
tries = 0

while True:
    x = int(input())
    tries += 1
    
    if x == secret:
        print("Correct")
        print(tries)
        break
    else:
        print("Try again")