secret = -4

guess = int(input())

if guess < secret:
    print("Low")
elif guess > secret:
    print("High")
else:
    print("Correct")
    
while guess != secret:
    guess = int(input())
    
    if guess == secret:
        print("Correct")
    else:
        print("Wrong")