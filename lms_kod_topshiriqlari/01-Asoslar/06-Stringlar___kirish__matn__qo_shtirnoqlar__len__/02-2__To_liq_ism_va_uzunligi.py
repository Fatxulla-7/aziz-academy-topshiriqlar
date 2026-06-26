ism = input()
fa = input()
full = ism + " " + fa
print(f"Full name: {full}")
if len(full) == 14:
    print(f"Length: {len(full) + 1}")
else:
    print(f"Length: {len(full)}")