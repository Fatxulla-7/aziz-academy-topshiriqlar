role = input()

if role == "admin":
    print("Full access")
elif role == "user":
    print("Limited")
else:
    print("Guest")