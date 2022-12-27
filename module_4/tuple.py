baz = 10
foo = -1

baz, foo, *rest = foo, baz, 100, 40

print(baz, foo)
print(rest)

# actions with tuple

my_tuple = (1, 1, 2, 3, 5, 8, 13, 21, 7, 5, 100)

print(my_tuple[3])

print(my_tuple[3:])

print(list(my_tuple))