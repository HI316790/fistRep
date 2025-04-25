class Student:
    academy = 'it step'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        return f'{self.name} was born in {2025 - self.age}'

    def get_b_year(self):
        return 2025 - self.age


student_1 = Student('Катя', 52)
student_2 = Student('Настя', 14)
student_3 = Student('марк', 12)

print(student_1.academy)
print(student_1.name)
print(student_1.age)

print(student_2.academy)
print(student_2.name)
print(student_2.age)

print(student_3.academy)
print(student_3.name)
print(student_3.age)

print(student_1.show_info())
print(student_2.show_info())
print(student_3.show_info())

print(student_1.get_b_year())
print(student_2.get_b_year())
print(student_3.get_b_year())

print(f'що робе {student_1.name}?')
for hour in range(24):
    if 0 <= hour <= 6 or hour > 22:
        print(f'{hour}:00 - спить')
    elif 7 <= hour <= 8:
        print(f'{hour}:00 - прокидається та снідає')
    elif 9 <= hour <= 16:
        print(f'{hour}:00 - вчиться в академії')
    elif 17 <= hour <= 21:
        print(f'{hour}:00 - відпочиває ')
    else:
        print(f'{hour}:00 - готується до сну')