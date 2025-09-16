class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age}, {self.gender}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, {self.record_book}'

class GroupOverflowError(Exception):
    def __init__(self, message="Група переповнена. Неможливо додати більше студентів."):
        self.message = message
        super().__init__(self.message)


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupOverflowError
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_remove = self.find_student(last_name)
        if student_to_remove:
            self.group.remove(student_to_remove)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n '.join(str(student) for student in self.group)
        return f'Number:{self.number}\\n {all_students} '

# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
# print(gr)
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
#
# gr.delete_student('Taylor')
# print(gr)  # Only one student
#
# gr.delete_student('Taylor')  # No error!
gr = Group('PD1')
try:

    for i in range(10):
        gr.add_student(Student('Male', 20 + i, f'Student{i + 1}', f'Lastname{i + 1}', f'AN{100 + i}'))

    print(f"Додано 10 студентів. Кількість: {len(gr.group)}")


    print("Спроба додати 11-го студента...")
    gr.add_student(Student('Female', 25, 'Student11', 'Lastname11', 'AN111'))

except GroupOverflowError as e:
    print(f"Помилка: {e}")
