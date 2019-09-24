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
with open('unordered_dict.json', 'w') as v_write:
    json.dump(strange_dict, v_write, ensure_ascii=False, indent=4, sort_keys=True)

