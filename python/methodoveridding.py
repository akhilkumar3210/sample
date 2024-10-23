class Bank:
    def __init__(self):
        print('''
              STATE BANK OF INDIA (SBI)
              -------------------------
              BRANCH::ERNAKULAM
              IFSC::SBIN000145
              LOCATION::MG ROAD,ERNAKULAM,KERALA,INDIA
                    ''')
    def depo(self):
        print('Amount Added')
    
    
class Users(Bank):
    def __init__(self):
        super().__init__()
        self.Name=input("Enter ur Name ::")
        self.Email=input("Enter ur Email ::")
    def users_dtls(self):
        print(self.Name,self.Email)

Athul=Users()
Athul.depo()