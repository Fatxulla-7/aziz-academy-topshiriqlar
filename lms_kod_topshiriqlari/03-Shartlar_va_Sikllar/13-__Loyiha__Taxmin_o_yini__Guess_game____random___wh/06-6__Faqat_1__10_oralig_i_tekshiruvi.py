secret = 6

while True:
    guess = int(input())
    
    if guess < 1 or guess > 10:
        print("Invalid")
        continue
        
    if guess == secret:
        print("Correct")
        break