import json

strange_dict = {
    0: False,
    5: "5",
    "6": "Шесть",
    7: None,
    "eight": 8.0,
    9.0: "nine",
    "another_dict": {
        0: True,
        1: False,
        2: None,
        "one": "ONE",
    }
}
with open('strange_dict.json', 'w') as f_write:
    json.dump(strange_dict, f_write, ensure_ascii=False, indent=4)
# Задание 1.1 и 1.2
unordered_dict = {
    5: "Пять",
    6: "Шесть",
    9: "Девять",
    4: "Четыре",
    0: "Ноль",
    7: "Семь",
    8: "Восемь",
    42: "Сорок два",
    2: "Два",
    1: "Один",
    3: "Три",
}
with open('unordered_dict.json', 'w') as v_write:# Задание 1.4
    json.dump(unordered_dict, v_write, ensure_ascii=False, indent=4, sort_keys=True)
with open('timetable_monday.json', 'r') as f_read: # Задание 2.1
  timetable_dict = json.load(f_read)
print(timetable_dict['8l'])

"""
Модуль json использует эту таблицу преобразования
+---------------+-----------+
|     JSON      |  Python   |
+---------------+-----------+
| object        | dict      |
| array         | list      |
| string        | unicode   |
| number (int)  | int, long |
| number (real) | float     |
| true          | True      |
| false         | False     |
| null          | None      |
+---------------+-----------+

в словарях ключи могут быть только одного формата

"""
strange_dict = {
    5: "Пять",
    6: "Шесть",
    9: "Девять",
    4: "Четыре",
    0: "Ноль",
    7: "Семь",
    8: "Восемь",
    42: "Сорок два",
    2: "Два",
    1: "Один",
    3: "Три",
}
x = dict()
y = None
with open('y.json', 'w') as f_write:
    strange = json.dump(y, f_write)
print(strange)
print(x)

with open('strange_dict.json', 'w') as f_write:
  dit = json.dump(strange_dict, f_write, sort_keys=True, ensure_ascii=False, indent=4)
print(strange_dict)

