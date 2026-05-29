username, age = input().split()
age = int(age)

if username == "admin":
    if age >= 18:
        print("Full access")
    else:
        print("Limited")
else:
    print("No access")