# 1
a = 'Some char'

try:
    int(a)
except Exception:
    print("Something went wrong")

# 2 handle
try:
    int(a)
except Exception as e:
    print(f"Look what you did: {e}")
    print(f"Exception type is: {type(e)}")

# 3 else
a = '3'

try:
    int(a)
except Exception as e:
    print(f"Look what you did: {e}")
else:
    print("No exception :)")


# 4 raise
raise ValueError("Wrong value")

# 5 raise if
c = 'cat'

if type(c) is not int:
    raise ValueError("Must be int")
else:
    print(c)

# 6 another exception

a = 3

try:
    a/0
except ZeroDivisionError:
    print("division by zero")
except TypeError:
    print("Must be int")