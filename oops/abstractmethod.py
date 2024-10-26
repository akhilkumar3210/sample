from abc import ABC,abstractmethod
class college(ABC):
    @abstractmethod
    def register(self):
        print('reg')
    def class_room(self):
        print('class room')
    def ground(self):
        print('ground')

class student(college):
    def register(self):
        name=input("Enter ur name : ")
        phno=int(input("Enter ur number :"))
        email=input("Enter ur email : ")
    def notes():
        print('notes')
class staff(college):
    def register(self):
        name=input("Enter ur name : ")
        exp=int(input("Enter ur number :"))
        sub=input("Enter ur email : ")
    def exam_papers(self):
        print('exam papers')
        
std1=student()
std1.register()


st1=staff()
st1.register()
