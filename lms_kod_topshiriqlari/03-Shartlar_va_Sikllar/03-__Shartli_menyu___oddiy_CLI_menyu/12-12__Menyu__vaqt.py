hour = int(input())

if hour < 12:
    print("Morning")
elif hour < 18:
    print("Day")
else:
    print("Night")