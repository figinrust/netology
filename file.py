class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_on_course(self, name_course, all_students):
        all_grades = []
        for student in all_students:
            if isinstance(student, Student) and name_course in student.courses_in_progress and name_course in student.grades:
                all_grades += student.grades[name_course]
        for grade in all_grades:
            if all_grades:
                return round(sum(all_grades) / len(all_grades), 1)
            else:
                return 'Ошибка'

    def get_average(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if all_grades:
            return round(sum(all_grades) / len(all_grades), 1)
        return 'Ошибка'

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.get_average() > other.get_average()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.get_average() < other.get_average()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.get_average() == other.get_average()

    def __str__(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if all_grades:
            average = round(sum(all_grades) / len(all_grades), 1)
        else:
            average = 0
        return f"Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_on_course(self, name_course, all_lecturers):
        all_grades = []
        for lecturer in all_lecturers:
            if isinstance(lecturer, Lecturer) and name_course in lecturer.courses_attached and name_course in lecturer.grades:
                all_grades += student.grades[name_course]
        for grade in all_grades:
            if all_grades:
                return round(sum(all_grades) / len(all_grades), 1)
            else:
                return 'Ошибка'

    def get_average(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if all_grades:
            return round(sum(all_grades) / len(all_grades), 1)
        return 0
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.get_average() > other.get_average()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.get_average() < other.get_average()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.get_average() == other.get_average()

    def __str__(self):
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        if all_grades:
            average = round(sum(all_grades) / len(all_grades), 1)
        else:
            average = 0
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average}"

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"

all_students = []
all_mentors = []
all_lecturers = []
all_reviewers = []

student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python', 'Java', 'C++', 'Git']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Алёхина', 'Ольга', 'Ж')
student2.courses_in_progress += ['Python', 'Java', 'C++']
student2.finished_courses += ['Введение в ООП']

mentor1 = Mentor('Some', 'Buddy')
mentor1.courses_attached += ['Python', 'Java', 'C++']
mentor1.rate_hw(student1, 'Python', 10)
mentor1.rate_hw(student1, 'Python', 5)
mentor1.rate_hw(student1, 'Python', 10)
mentor1.rate_hw(student2, 'Java', 10)
mentor1.rate_hw(student2, 'Python', 2)
mentor1.rate_hw(student2, 'C++', 2)
mentor1.rate_hw(student1, 'C++', 3)

mentor2 = Mentor('Джон', 'Уик')
mentor2.courses_attached += ['Java', 'C++']
mentor2.rate_hw(student1, 'Java', 8)
mentor2.rate_hw(student1, 'C++', 2)
mentor2.rate_hw(student1, 'Java', 2)
mentor2.rate_hw(student2, 'C++', 10)

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer1.courses_attached += ['Python', 'Java', 'C++']

lecturer2 = Lecturer('Игорь', 'Сергеев')
lecturer2.courses_attached += ['Java', 'C++']

reviewer1 = Reviewer('Пётр', 'Петров')
reviewer1.courses_attached += ['Python', 'C++']

reviewer2 = Reviewer('Джек', 'Воробей')
reviewer2.courses_attached += ['Java', 'C++']

print(student2.rate_lecture(lecturer1, 'Python', 7))
print(student2.rate_lecture(lecturer1, 'Python', 5))
print(student2.rate_lecture(lecturer1, 'Java', 9))
print(student2.rate_lecture(lecturer2, 'C++', 6))
print(student2.rate_lecture(lecturer1, 'Java', 8))

print(student2.rate_lecture(lecturer2, 'С++', 6))
print(student1.rate_lecture(lecturer2, 'Java', 8))
print(student1.grades)

all_students.append(student1)
all_students.append(student2)
all_mentors.append(mentor1)
all_mentors.append(mentor2)
all_lecturers.append(lecturer1)
all_lecturers.append(lecturer2)
all_reviewers.append(reviewer1)
all_reviewers.append(reviewer2)

for lecturer in all_lecturers:
    if all_lecturers:
        print('\nЛектор -------------------------------------------------------------------------\n')
        print(lecturer)
    else:
        print('Список пустой')
for reviewer in all_reviewers:
    if all_reviewers:
        print('\nРевьюер ------------------------------------------------------------------------\n')
        print(reviewer)
    else:
        print('Список пустой')
for student in all_students:
    if all_students:
        print('\nСтудент ------------------------------------------------------------------------\n')
        print(student)
        print(' ')
    else:
        print('Список пустой')

#Тесты (Задание 3)

# Для лекторов
print(lecturer1 > lecturer2)
print(lecturer1 == lecturer2)
print(lecturer1 < lecturer2)

# Для студентов
print(student1 > student2)
print(student1 < student2)

# Тесты (Задание 4)

# Для лекторов
print(student1.get_average_on_course('Python', all_students))
print(student2.get_average_on_course('C++', all_students))

# Для студентов
print(lecturer1.get_average_on_course('Python', all_lecturers))
print(lecturer2.get_average_on_course('Java', all_lecturers))