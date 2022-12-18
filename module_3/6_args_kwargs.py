def first(size, *args):
    print(f"size: {size}")
    print(f"args: {args} len is {len(args)}")


result = first(12, 2, 3, 4, 5, 'Hello', 27)


def second(size, **kwargs):
    print(f"size: {size}")
    print(f"args: {kwargs} len is {len(kwargs)}")


result = second(12, foo=3, baz="hi")


def third(size, *args, **kwargs):
    print(f"size: {size}")
    print(f"args: {args} len is {len(args)}")
    print(f"args: {kwargs} len is {len(kwargs)}")


third(12, 2, 3, 4, 5, 'Hello', 27, foo=3, baz="hi")

# iter over args

def sum(start, *args):
    sum = start
    for el in args:
        sum = sum + el
    return sum


result = sum(2, 3, 5, 1)
print(result)
result = sum(2, 3, 5, 1, 3, 5, 1)
print(result)

# interact with kwargs

def greetins(**kwargs):
    print(kwargs)
    name = kwargs.get("name", "Noname")
    age = kwargs.get("age", None)
    return f"Hello {name} - {age} age"


result = greetins()
print(result)

result = greetins(name="Rob", age=34, baz=12, bar="foo")
print(result)

# interact with kwargs 2

def greetins(**kwargs):
    print(kwargs)
    print("baz is: " + str(kwargs["baz"]))
    r = kwargs.get("ott")
    print(r)
    name = kwargs.get("name", "Noname")
    age = kwargs.get("age", None)
    return f"Hello {name} - {age} age"


result = greetins(name="Rob", age=34, baz=12, bar="foo")
print(result)