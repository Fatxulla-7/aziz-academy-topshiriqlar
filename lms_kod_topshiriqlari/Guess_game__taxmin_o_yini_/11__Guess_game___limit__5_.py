secret = 10
tries = 5

for i in range(tries):
    guess = int(input())
    if guess == secret:
        print()
        break
else:
    print("You lost")