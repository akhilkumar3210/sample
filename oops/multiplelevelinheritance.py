# class school:
#     def class_room(self):
#         print('school class room')
#     def exam(self):
#         print('school exams')
    
# class tuition:
#     def notes(self):
#         print('notes')

# class student(school,tuition):
#     def uniform(self):
#         print('UNIFORMS')
        
        
# std1=student()
# std1.exam()
# std1.uniform()
# std1.class_room()
# std1.notes()


class showroom:
    def cars(self):
        print('TATA,TOYOTA')
    def bikes(self):
        print('HERO,YAMAHA,BAJAJ')
class spare:
    def car_spare(self):
        print('OIL,SENSORS,CYLINDER')
    def bike_spare(self):
        print('bike spare')
class custmor(showroom,spare):
    def requirements():
        print("requirement")
        
        
cust1=custmor()
cust1.cars()
cust1.car_spare()