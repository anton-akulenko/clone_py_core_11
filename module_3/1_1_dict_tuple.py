def func():
    return


# unhashable
# mutable
my_dict = {}
my_dict = {"apples": 2,
           "banana": 3,
           "name": "Josh",
           "1": (1, 2, 3),
           1: "number",
           True: "it's True",
           20.5: False,
           "func": func()
           }

my_dict["apples"]  # access by key, key must be immutable
my_dict[20.5]
my_dict[1] = 1
my_dict.update({"apples": 3})

# immutable
# hasable/unhashable
my_tuple = ()
my_tuple = (1, 2, 3)
my_tuple = ("First", 2, 3)
my_tuple = (1, 2, 3, (2, 2, 3), 1, 2, 3)
my_tuple = ([4, 5, "231"], 1, 2, 3)

my_tuple[0]  # access by index
my_tuple[1]

# fulfill dict with value
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)
