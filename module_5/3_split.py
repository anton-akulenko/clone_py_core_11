string = "Я дуже хочу вивчити пайтон"
transform_to_list = string.split(' ')
print(transform_to_list)
restore_string = ' '.join(transform_to_list)
print(restore_string)

# Парсимо url

url_query = "https://hard.rozetka.com.ua/computers/c80095/producer=apple;21414=64-gb/"
cleaned_url = url_query[:url_query.rfind('/')]
cleaned_url = cleaned_url[cleaned_url.rfind('/') + 1:]
query = cleaned_url.split(';')
print(query)

obj_query = {}
for el in query:
    key, value = el.split('=')
    obj_query.update({key: value})

print(obj_query)

# Зворотня операція

prepare = []
for key in obj_query:
    prepare.append(key + '=' + obj_query[key])

print(';'.join(prepare))

# Парсимо url з google

url_search = "https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"

_, query = url_search.split('?')

print(query)

obj_query = {}
for el in query.split('&'):
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})

print(obj_query)
