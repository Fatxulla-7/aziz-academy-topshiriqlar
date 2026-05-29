role, active = input().split()
active = int(active)

if role == "admin":
    if active == 1:
        print("Admin active")
    else:
        print("Admin inactive")
else:
    print("User")