groupmates = [
    {
        "name": "Хаджи-Мурад",
        "surname": "Ханов",
        "exams": ["РКПО", "ОС", "СП"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Никита",
        "surname": "Демин",
        "exams": ["ВИТ", "Компьютерные сети", "Web"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Роман",
        "surname": "Кириллов",
        "exams": ["Компьютерные сети", "ВИТ", "РКПО"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Григорий",
        "surname": "Тимонин",
        "exams": ["Web", "СП", "Сетевые технологии"],
        "marks": [3, 5, 3]
    }
]


def print_students(students):
    print(
        u"Имя".ljust(15), u"Фамилия".ljust(10),
        u"Экзамены".ljust(40), u"Оценки".ljust(20)
    )
    for student in students:
        print(
            student["name"].ljust(15),
            student["surname"].ljust(10),
            str(student["exams"]).ljust(40),
            str(student["marks"]).ljust(20)
        )


print_students(groupmates)
