def identity(x):
    return x


lambda x: x

(lambda x: x + 1)(2)

add_one = lambda x: x + 1
add_one(2)

full_name = lambda first, last: f'Full name: {first.upper()} {last.upper()}'
print(full_name('guido', 'van rossum'))

(lambda x, y: x + y)(2, 3)
(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)

(lambda x:
 (x % 2 and 'odd' or 'even'))(3)


numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))