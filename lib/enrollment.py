def course_count(self):
    return len(self._enrollments)
@classmethod
def aggregate_enrollments_per_day(cls):
    enrollment_count = {}
    for enrollment in cls.all:
        date = enrollment.get_enrollment_date().date()
        enrollment_count[date] = enrollment_count.get(date, 0) + 1
    return enrollment_count

def aggregate_average_grade(self):
      # lets assume the grades are stored in a protected attribute called _grades. 
      total_grades = sum(self._grades.values())
      num_courses = len(self._grades)
      average_grade = total_grades / num_courses

      return average_grade