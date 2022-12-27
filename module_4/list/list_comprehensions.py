squares = []
for x in range(10):
    squares.append(x ** 2)

squares = list(map(lambda x: x ** 2, range(10)))

squares = [x ** 2 for x in range(10)]

# example 2

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
