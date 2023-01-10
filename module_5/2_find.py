string = "Виключити із строки підсторки [з такими символами] з, [розташовані між] скобками [, ]."

start_index = string.find('[')
end_index = string.find(']')
new_string = string[:start_index] + string[end_index + 1:]
print(new_string)

def exclude_substrings(string):
    new_string = string[:]
    while True:
        start_index = new_string.find('[')
        end_index = new_string.find(']')
        if start_index == -1:
            break
        new_string = new_string[:start_index] + new_string[end_index + 1:]
    return new_string



s = 'Some words'
s.rfind('o')  # 6

s = 'Some words'
s.rindex('o')  # 6
s.rindex('a')


print(exclude_substrings(string))