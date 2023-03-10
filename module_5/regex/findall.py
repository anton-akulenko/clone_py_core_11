'''
Метод: findall
'''

import re

string = "Нільс Бор народився в родині професора фізіології Копенгагенського університету Християна Бора " \
         "(1858—1911) й Еллен Адлер (1860—1930). Батьки Бора одружилися 1881 року. Батька Нільса Бора двічі" \
         " висували кандидатом на Нобелівську премію з фізіології або медицини[11]. Мати була донькою впливового" \
         " та вельми заможного єврейського банкіра і парламентаря-ліберала Давида Баруха Адлера[da] (1826—1878)" \
         " і Дженні Рафаел (1830—1902) із британської єврейської банкірської династії Raphael Raphael & sons[en][12]."

# Знайти всі цифри та кількість
result = re.findall(r'\d', string)
print(result)
print(len(result))

# Знайти всі числа та їх кількість
result = re.findall(r'\d+', string)
print(result)
print(len(result))

# Знайти усі роки
result = re.findall(r'\d{4}', string)
print(result)
print(len(result))