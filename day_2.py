#1. Adding the individual numbers of the input togther.

num = (input("enter a two digit number? \n"))
print(int(num[0]) + int(num[1]))

#2. Calculating body BMI and printing output as a whole number instead of a float

height = float(input("enter you height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / (height**2))
print(bmi)


#3. Calculating your life in weeks.

age = input("What is your current age? ")
age_value = 90  - int(age)
weeks = age_value * 52
days = age_value * 365
months = age_value* 12
message = f"Well there, if you get to live till 90, you still have {days} days, {weeks} weeks and {months} months to live. Go crush those dreams! "
print(message)


#4. Simple tip calculator
bill = float(input("how much is your bill?($) "))
tip_percent = float(input("How many percent is the tip?(%) 10, 12 or 15?"))
no_of_people = int(input("How many people are sharing the bill? "))

tip_amount = bill * (tip_percent / 100)
total_bill = tip_amount + bill
bill_per_person = round((total_bill / no_of_people), 2)

message = f"Each person should pay {bill_per_person} "
print(message)




