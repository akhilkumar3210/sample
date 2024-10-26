# class university:
#     def calicut(self):
#         print('calicut  university')
#     def ktu(self):
#         print('ktu')
# class college:
#     def maharajas_clg(self):
#         print('maharajas college')
#     def cusat(self):
#         print('cusat')
# class student(university,college):
#     def books(self):
#         print('books')


# std1=student()
# std1.calicut()
# std1.cusat()
# std1.books()


class university:
    def calicut(self):
        print('calicut  university')
    def ktu(self):
        print('ktu')
class college(university):
    def maharajas_clg(self):
        print('maharajas college')
    def cusat(self):
        print('cusat')
class student(college):
    def books(self):
        print('books')


std1=student()
std1.calicut()
std1.cusat()
std1.books()