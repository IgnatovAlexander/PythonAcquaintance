import json


def load(path):
    fname = str(path)  # открываем файл
    with open(fname, "r", encoding="utf-8") as fh:  # открываем файл на чтение
        BD_local = json.load(fh)  # загружаем из файла данные в словарь data
    # print('БД успещно загружена')
    return BD_local

def save(b, path):
    # сохранить в json
    fname = str(path)
    with open(fname, "w", encoding="utf-8") as fh:  # открываем файл на запись
        fh.write(
            json.dumps(b, ensure_ascii=False)
        )  # преобразовываем словарь data в unicode-строку и записываем в файл
    print("БД успещно сохранена")
