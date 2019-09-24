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
print(json.dumps(strange_dict, ensure_ascii=False, indent=4)) # Задание 1.1

