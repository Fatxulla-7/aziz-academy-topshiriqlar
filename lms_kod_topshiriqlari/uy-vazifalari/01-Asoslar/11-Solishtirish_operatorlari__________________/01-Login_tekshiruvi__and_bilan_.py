n = input()
m = input()
if n == "admin" and m == "secret":
    print("True")
elif n == "admin" and m == "123":
    print("False")
else:
    print("False")