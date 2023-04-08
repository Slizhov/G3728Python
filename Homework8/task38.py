# Урок 8. Работа с файлами
# Задача 38: 
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных
# 1. Открыть файл; # 2. Сохранить файл; # 3. Посмотреть все контакты
# 4. Создать контакт; # 5. Найти контакт; # 6. Изменить контакт
# 7. Удалить контакт; # 8. Выход


phonebook = {}
phonebook_last_id = 0

def create(db: dict, id: int, surname: str, name: str, phone: str, discription: str) -> tuple:           #data_base
    db[id] = {"surname": surname, 'name': name, 'phone': phone, 'discription': discription}
    id += 1
    return db, id

fio = {1: {'surname': "Иванов", 'name': "Иван", 'number': "89234145", 'discription': "работник"}}
def read(db: dict, surname_filter: str) -> int:
    for _id in db:
        if surname_filter.lower() in db[_id]['surname'].lower():
            return _id
 
def print_record(db: dict, _id: int):
    if _id is not None:
        print(f'{"="*30}\n{db[_id]}\n{"="*30}\n')
    else:
        print(f'{"="*30}\nЗапись не найдена!\n{"="*30}\n')

 
def get_user_data() -> tuple:
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите номер: ")
    discription = input("Введите описание: ")
    return surname, name, phone, discription
 
def get_surname() -> str:
    surname = input("Введите искомую фамилию: ")
    return surname
 
def print_data(db: dict) -> None:
    for _id, data in db.items():
        print(f"[{_id}: {data['surname']} | {data['name']} | {data['phone']} | {data['discription']} ]")
 
# 3) экспорт данных в текстовый файл формата csv
def export_db(db: dict, filepath: str, delimeter: str = '#') -> None:
    with open(filepath, "w", encoding='utf-8') as file:
        for _id, data in db.items():
            file.write(f"{data['surname']}{delimeter}{data['name']}{delimeter}{data['phone']}{delimeter}{data['discription']}\n")
 
def get_file_name() -> str:
    return input("Введите имя файла: ")
 
# 4) импорт данных из текстового файла формата csv
def import_db(db: dict, last_id: int, filepath: str, delimeter: str = '#') -> tuple:
    with open(filepath, "r", encoding='utf-8') as file:
        for line in file:
            # data['surname']},{data['name']},{data['phone']},{data['discription']}
            _data = line.strip().split(delimeter)
            db[last_id] = {"surname": _data[0], 'name': _data[1], 'phone': _data[2], 'discription': _data[3]}
            last_id += 1
    return db, last_id
def menu(db: dict, last_id: int) -> None:
    while True:
        print("Возможные действия: ")
        print("1. Создать запись")
        print("2. Вывести имеющиеся данные")
        print("3. Экспортировть данные в файл")
        print("4. Импортировать данные из файла")
        print("5. Найти контакт")
        print("6. Выход")
        user_input = input("Введите действие > ")
        if user_input == "1":
            record = get_user_data()
            db, last_id = create(db, last_id, *record)
        elif user_input == "2":
            print_data(db)
        elif user_input == "3":
            export_db(db, get_file_name())
        elif user_input == "4":
            db, last_id = import_db(db, last_id, get_file_name())
            # db, last_id = import_db(db, last_id, 'data08_1.txt')
        elif user_input == "5":
            found_id = read(db, get_surname())
            try:
                print_record(db, found_id)
            except KeyError:
                print(f'\n{"="*30}\nЗапись не найдена!\n{"="*30}\n')
        else:
            break
 
menu(phonebook, phonebook_last_id)