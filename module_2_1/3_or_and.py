# using or

a = 'cat'

if a == 'cat' or a == 'dog':
    print("I'll pet it)")

b = 2

if b and b > 0:
    print("B is positive number")


a = int(input("Enter a number: "))

if not a % 2 and not a % 3:
    print("a multiple 2 and 3")

if not a % 2 and not a % 5:
    print("a multiple 2 and 5")

if a <= 10 or a >= 50:
    print("a is not near (10, 50)")  # [10, 50)

# same as if 10 < a < 50
if a > 10 and a < 50:
    print("a is near (10, 50)")
