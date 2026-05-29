secret = 9
tries = 0

while True:
    x = int(input())
    tries += 1
    
    if x == secret:
        print("Low")
        print(f"Correct")
        break