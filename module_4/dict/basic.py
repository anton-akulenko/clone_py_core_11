person = {
    "name": "Oleg",
    "age": 23,
    "phone": "38(050)9993322",
    "married": False
}

person.update({"address": "Ukraine, Kyiv", "lang": "ukr"})
person.pop("lang")
oleg = person.copy()
person.clear()
oleg["address"] = "Poltava"
print(oleg)
print(person)
print(oleg.get("name", "anonim"))
print(oleg.get("age", None))
print(oleg.get("lang", "Python"))


# iterate over several attributes
grade1 = {"Oleg": 2, "Alexx": 3}
grade2 = {"Nastya": 5, "Sergey": 4}
grade3 = {"Alex": 4, "Andry": 5}

result = {}

for d in (grade1, grade2, grade3):
    result.update(d)

print(result)