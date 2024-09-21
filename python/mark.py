a=input("Enter a name :")
b=float(input("Enter a score :"))

if(b<=100 and b>=90):
    print("you have passed\nExcellent\nGrade is A")
elif(b<=89 and b>=80):
    print("you have passed\n Good\n Grade is B")
elif(b<=79 and b>=70):
    print("you have passed\n Satisfactory\n Grade is C")
elif(b<=69 and b>=60):
    print("you have passed\nNeeds to improvement\n Grade is D")
elif(b<=59 and b>=0):
    print("Failed\n Needs improvement\n Grade is F")
else:
    print("score is not valid")
    


