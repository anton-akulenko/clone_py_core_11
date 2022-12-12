# comparing also give bool
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if first > second:
    print("The first number is greater than the second number.")
elif first == second:
    print("The first number is equal to the second number.")
else:
    print("The second number is greater than the first number.")

if first % 2:
    print("The first number is odd.")
else:
    print("The first number is even.")

# can be more complex
num = int(input("Enter the first number: "))
print(num)
length = len(str(num))

if length == 2 and num % 2 == 0:
    print("Even two-digit number")
else:
    print("Nope")

# text is True
a = "Work"

if a:
    print("Yep, it's something")
else:
    print("Ups, i did it again)")

# empty string is False
a = ""

if a:
    print("Yep, it's something")
else:
    print("Ups, i did it again)")

# 0 string is False
a = 0

if a:
    print("Yep, it's something")
else:
    print("Ups, i did it again)")


# None is False
a = None

if a:
    print("Yep, it's something")
else:
    print("Ups, i did it again)")

# changing variables inside condition

a = "cat"
result = None

if a == 'cat':
    result = "My cat is best"
    print("This is, yes")
else:
    result = "Ehhm, no cat("
    print("This is, no")

print("I'm done")
print("result: " + result)
