"""
Є 2 списку телефонів: перший – список усіх реєстрацій, другий – тих, хто підключився до гри.
Визначити список телефонів тих, хто зареєструвався, але не розпочав роботу на сайті.
["380669640547", "0637306465",
"380961935171", "632643973", "508325200", "000000000", "48730283918", "986223575", "375297947963"]
["380669640547", "0637306465" "632643973", "508325200", "48730283918", "986223575"]
"""

from strip_5_replace_etc import isvalid_phone

registration = ["380669640547", "0637306465",
                "380961935171", "632643973", "508325200", "000000000", "48730283918", "986223575", "375297947963"]
connect = ["380669640547", "0637306465" "632643973",
           "508325200", "48730283918", "986223575"]

valid_registration = []
for phone in registration:
    if isvalid_phone(phone):
        valid_registration.append(phone)


valid_connect = []
for phone in connect:
    if isvalid_phone(phone):
        valid_connect.append(phone)



if __name__ == '__main__':
    result = list(set(valid_registration) & set(valid_connect))
    print(f"Результат: {result}")