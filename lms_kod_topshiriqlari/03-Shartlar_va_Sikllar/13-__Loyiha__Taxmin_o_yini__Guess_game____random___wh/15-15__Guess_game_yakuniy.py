secret = 20
tries = 0

while True:
    guess = int(input())
    tries += 1
    
    if guess < 1 or guess > 20:
        print("Invalid")
    elif guess < secret:
        print("Low")
    elif guess > secret:
        print("High")
    else:
        print("Correct")
        print(tries)
        break