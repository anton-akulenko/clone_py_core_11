# 12
a = 0
while a < 6:
    a += 1
    if not a % 2:
        continue
    print(a)

# 13
sum = 0
a = 1

while a <= 5:
    sum += a
    a = a + 1
print(sum)

# 14
a = [2, 4, 6, 8, 3]
k = 0
for b in a:
    if k < b:
        k = b
print(k)