class college:
    def cusat(self):
        print('cuast')
class sports(college):
    def indoor(self):
        print('indoor')
    def outdoor(self):
        print('outdoor')
class staff(college,sports):
    def staffs(self):
        print('Staffs')
class football(sports):
    def football(self):
        print('football')
class batminton(sports):
    def batminton(self):
        print('batminton')
    
    
ply1=batminton()
ply1.indoor()
ply1.cusat()

staf1=staff