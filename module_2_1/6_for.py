# 1
for letter in "dog":
    print("Feed a dog")

# 2
for letter in "dog":
    print(letter)

# 3

for i in 'cat':
    if i == 'a':
        continue
    print(i)


# range 1-25
sum = 0

for _ in range(1, 26):
    sum += 5

print(sum)


# nested cycle

sum = 0

for i in range(1, 6):
    print(f"Upper cycle: {i}")
    for j in range(1, 5):
        print("--")
        if sum >= 100:
            break
        sum += 10
        print(f"inner cycle: {j}")
        print("Sum now is: {}".format(sum))


print(sum)


# logic in cycle

string = input('Enter string')

count_symbols = 0
count_a = 0
count_b = 0
count_c = 0
count_space = 0

# abcddd

for ch in string:
    count_symbols += 1
    if ch == 'a':
        count_a += 1
        continue
    if ch == 'b':
        count_b += 1
        continue
    if ch == 'c':
        count_c += 1
        continue
    if ch == ' ':
        count_space += 1

print(count_symbols, count_space, count_a, count_b, count_c)
