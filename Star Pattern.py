a = int(input("Enter no. of rows you want to print\n"))
b = int(input("Enter 1 or 0\n"))
new = bool(b)
if new == True:
    for i in range(1, a + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

elif new == False:
    for i in range(a, 0, -1):
        for j in range(1, i + 1):
            print("*", end="")
        print()