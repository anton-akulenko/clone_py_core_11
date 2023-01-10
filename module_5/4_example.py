"""
Метод: isdigit
----
1. Знайти кількість цифр в строці
2. Знайти кількість чисел в строці
"""

string = "Файли програми CorelDraw мають розширення .cdr." \
         " Формат cdr кожної нової версії несумісний із старішими версіями, що означає, наприклад," \
         " файл, збережений у версії CorelDraw 9 може бути відкритий в більш новій версії програми" \
         " (CorelDraw 10, 11, 12 і т. д.), але не може бути відкритий в старій версії програми" \
         " (CorelDraw 8, 7, 6 і т. д.)."


def count_digits(string):
    count = 0
    for el in string:
        if el.isdigit():
            count += 1
    return count


print(count_digits(string))
print(count_digits(''))


def count_numbers(string):
    count = 0
    pos = 0
    nums = []
    while pos < len(string):
        if string[pos].isdigit():
            num = ''
            while pos < len(string) and string[pos].isdigit():
                num = num + string[pos]
                pos = pos + 1
            nums.append(num)
            count = count + 1
        else:
            pos = pos + 1

    return count, nums


print(count_numbers(string))
print(count_numbers(''))