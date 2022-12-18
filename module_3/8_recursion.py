def count_to_100(start=0):
    print(start)
    while start < 100:
        return count_to_100(start+25)


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))  # 5! = 120

