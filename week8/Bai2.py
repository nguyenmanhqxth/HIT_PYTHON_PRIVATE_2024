class Person:
    def __init__(self, name: str, yob: int):
        self.name = name
        self.yob = yob

    def describe(self):
        pass  


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print("Student:")
        print("  Name:", self.name)
        print("  YoB:", self.yob)
        print("  Grade:", self.grade)


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print("Teacher:")
        print("  Name:", self.name)
        print("  YoB:", self.yob)
        print("  Subject:", self.subject)


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialty: str):
        super().__init__(name, yob)
        self.specialty = specialty

    def describe(self):
        print("Doctor:")
        print("  Name:", self.name)
        print("  YoB:", self.yob)
        print("  Specialty:", self.specialty)


class Ward:
    def __init__(self, name: str):
        self.name = name
        self.people = []

    def add_person(self, person: Person):
        self.people.append(person)

    def describe(self):
        print("Ward Name:", self.name)
        for person in self.people:
            person.describe()

    def count_doctors(self) -> int:
        return sum(1 for person in self.people if isinstance(person, Doctor))

    def sort_by_age(self):
        self.people.sort(key=lambda person: person.yob)

    def average_teacher_yob(self) -> float:
        teachers = [person for person in self.people if isinstance(person, Teacher)]
        if not teachers:
            return 0.0
        return sum(teacher.yob for teacher in teachers) / len(teachers)


student1 = Student(name="studentA", yob=2010, grade="7")
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor1 = Doctor(name="doctorA", yob=1945, specialty="Endocrinologists")
doctor2 = Doctor(name="doctorB", yob=1975, specialty="Cardiologists")

ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

ward1.describe()
print("Number of doctors:", ward1.count_doctors())
ward1.sort_by_age()
print("After sorting by age:")
ward1.describe()
print("Average YoB for Teachers:", ward1.average_teacher_yob())
