a = 64
result = None

if a:
    if a > 30:
        result = "More then 30"
    elif a == 30:
        result = "It's 30"
    else:
        result = "Less then 30"
else:
    result = "No value"


# check type

a = "Fake"

if type(a) == int:
    if a > 30:
        result = "More then 30"
    elif a == 30:
        result = "It's 30"
    else:
        result = "Less then 30"
else:
    result = "No value"


a = 34

if type(a) is int:
    if a > 30:
        result = "More then 30"
    elif a == 30:
        result = "It's 30"
    else:
        result = "Less then 30"
else:
    result = "No value"
