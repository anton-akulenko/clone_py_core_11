chars = {'a': 1, 'b': 2}
chars_copy = chars.copy()
chars_copy == chars
chars_copy is chars

# example of deepcopy
import copy

# change value
my_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
md_copy = my_dict.copy()
my_dict['a'] = 34
md_copy['a']

# change value inside mutable list
my_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
md_copy = my_dict.copy()
my_dict['a'][0] = 34
md_copy['a'][0]

my_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
md_copy = copy.deepcopy(my_dict)
my_dict['a'][0] = 34
md_copy['a'][0]