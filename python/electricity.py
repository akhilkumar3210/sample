unit=int(input("Enter a unit : "))
amount=0
if unit<100:
    print("no charge ")
elif unit<200:
    amount=(unit-100)*5
    print(amount)
else:
    amount=(100*5)+(unit-200)*10
    print(amount)