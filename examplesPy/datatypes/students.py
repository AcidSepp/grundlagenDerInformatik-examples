from __future__ import annotations

# snippet: students
class Exam:
    def __init__(self,
                 name: str,
                 semester: int,
                 grade: float,
                 date: Date):
        self.date = date
        self.name = name
        self.semester = semester
        self.grade = grade

class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

if __name__ == '__main__':
    my_date: Date = Date(6,11,1995)
    my_exam: Exam = Exam("Studi McStudiface", 4, 1.7, my_date)
# snippet: /students