class Mentor:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []
  
class Lecturer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.grades = {}

  def average_grade(self):
    sum_grades = 0
    for grade in self.grades.values():
      sum_grades += sum(grade)
    return round((sum_grades) / len(self.grades),1)
    # return round(sum_grades / len(self.grades), 1)

  def __gt__(self, other):
    if not isinstance(other, Lecturer):
      return "Ошибка"
    return self.average_grade() > other.average_grade()
  
  def __str__(self):
    return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'
    
class Reviewer(Mentor):
  def rate_student(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in student.grades:
        student.grades[course] += [grade]
      else:
        student.grades[course] = [grade]
    else:
      return 'Ошибка'

  def __str__(self):
    return f'Имя: {self.name}\nФамилия: {self.surname}'
  
class Student:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}
   
  def rate_lecturer(self, lecturer, course, grade):
    if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]
      else:
        lecturer.grades[course] = [grade]
    else:
      return 'Ошибка'
  
  def average_grade(self):
    sum_grades = 0
    for grade in self.grades.values():
      sum_grades += sum(grade)
    return round((sum_grades) / len(self.grades),1) 

  def __gt__(self, other):
    if not isinstance(other, Student):
      print('Ошибка')
    return self.average_grade() > other.average_grade()
  
  def __str__(self):
    return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python','Git']

lecturer = Lecturer('Some', 'Buddy')
lecturer.courses_attached += ['Python','Git']

student = Student('Ruoy', 'Eman', 'your_gender')
student.courses_in_progress += ['Python','Git']
student.finished_courses += ['Введение в программирование']

reviewer.rate_student(student, 'Python', 10)
reviewer.rate_student(student, 'Git', 9.9)

student.rate_lecturer(lecturer, 'Python', 10)
student.rate_lecturer(lecturer, 'Git', 9.9)

reviewer_other = Reviewer('Leo', 'Di')
reviewer_other.courses_attached += ['Python','Git']

lecturer_other = Lecturer('Mat', 'Mak')
lecturer_other.courses_attached += ['Python','Git']

student_other = Student('Dej', 'Sid', 'your_gender')
student_other.courses_in_progress += ['Python','Git']
student_other.finished_courses += ['Введение в программирование']

reviewer.rate_student(student_other, 'Python', 10)
reviewer.rate_student(student_other, 'Git', 8)

student_other.rate_lecturer(lecturer_other, 'Python', 7)
student_other.rate_lecturer(lecturer_other, 'Git', 9.9)

students_average_grade = [student.average_grade(), student_other.average_grade()]

lecturers_average_grade = [lecturer.average_grade(), lecturer_other.average_grade()]

print(reviewer)
print(lecturer)
print(student)
print(reviewer_other)
print(lecturer_other)
print(student_other)
print(student > student_other)
print(lecturer > lecturer_other)
print(students_average_grade)
print(lecturers_average_grade)
def average_grade_students(students_list, course):
  sum_grades = 0
  for student in students_list:
    if course in student.grades:
      sum_grades += sum(student.grades[course])
  return round((sum_grades) / len(students_list),1)
print(average_grade_students([student, student_other], 'Python'))

def average_grade_lecturers(lecturers_list, course):
  sum_grades = 0
  for lecturer in lecturers_list:
    if course in lecturer.grades:
      sum_grades += sum(lecturer.grades[course])
  return round((sum_grades) / len(lecturers_list),1)
print(average_grade_lecturers([lecturer, lecturer_other], 'Python'))