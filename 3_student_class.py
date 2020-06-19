import array as arr
class Students:
    """Calculate students CGPA"""
    earned_credit = arr.array("f", [0.0, 0.0, 0.0, 0.0])
    earned_grade_points = arr.array("f", [0.0, 0.0, 0.0, 0.0])
    def __init__(self, earned_credit, earned_grade_points, i):
        self.earned_credit[i] = earned_credit
        self.earned_grade_points[i] = earned_grade_points

    def calculate_CGPA(self):
        sum_credit = 0
        sum_grade = 0
        for j in range(4):
            sum_credit = sum_credit + self.earned_credit[j]
            sum_grade = sum_grade + self.earned_grade_points[j]
        CGPA = sum_grade / sum_credit
        return CGPA

c5 = float(input("Enter the earned credit in sem 5: "))
g5 = float(input("Enter the earned grade points in sem 5: "))
c6 = float(input("Enter the earned credit in sem 6: "))
g6 = float(input("Enter the earned grade points in sem 6: "))
c7 = float(input("Enter the earned credit in sem 7: "))
g7 = float(input("Enter the earned grade points in sem 7: "))
c8 = float(input("Enter the earned credit in sem 8: "))
g8 = float(input("Enter the earned grade points in sem 8: "))
obj1 = Students(c5, g5, 0)
obj2 = Students(c6, g6, 1)
obj3 = Students(c7, g7, 2)
obj4 = Students(c8, g8, 3)
CGPA = obj4.calculate_CGPA()
print("CGPA = " + str(CGPA))
