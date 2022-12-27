my_set = {4, 6, "Oleg", "Python", 100}
my_set.add("Daria")
print("Daria" in my_set)

my_set.remove("Daria")
my_set.discard("Daria")  # no error

# immutable
my_set = {4, 6, "Oleg", "Python", [1, 2, 3]}

# operations
list1 = [1, 2, 3, 4, 55, 13, 21, 100]
list2 = [2, 2, 2, 33, 3, 3, 5, 4]

set_1 = set(list1)
set_2 = set(list2)
print(set_1, set_2)

set_union = set_1 | set_2  # union
set_1.union(set_2)
print(list(set_union))

set_cross = set_1 & set_2  # intersection
set_cross_2 = set_1.intersection(set_2)
print(list(set_cross))


list_daria = ["Red", "Green", "Black", "White"]
list_oleg = ["Red", "White", "Black", "Yellow"]

list_only_daria = list(set(list_daria) - set(list_oleg))
print(list_only_daria)


list_u = list(set(list_daria) ^ set(list_oleg))
print(list_u)
