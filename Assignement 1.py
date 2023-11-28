print("")
x=input("Melanie Dental Clinic")
print("",x)
print("____________________")
print("")

name = input("Patient's name: ")
print("My name is",name)
visited_before = input("Has the patient been here before? (Yes/No): ")
print("",visited_before)
last_visit = input("How many days since your last vist:")
print(last_visit,"days")
height = int(input("What is the patient’s height (in cm)?: "))
print(height,"cm")
current_weight = float(input("What is the patient’s weight (in kg)?: "))
print("The patient's weight is",current_weight, "kg")
last_weighed = input("When was the patient last weighed in (1/1/2000 if never weighed)?: ")
print("The patient's was last weighed on",last_weighed)
previous_weight = float(input("What was the patient’s weight (in kg, -1 if never weighed)?: "))
print("The patient's previous weight was", previous_weight, "kg")
practitioner_assessment = int(input("Practitioner’s overall assessment of the patient’s health (-5 to +5)?: "))
print("Practitioner's assessment:", practitioner_assessment)


y=input("Return Report")
print("",y)
print("____________________")

print("")
x=input("Melanie Dental Clinic")
print("",x)
print("____________________")

BMI = round(current_weight/ (height*2)) *100

if BMI > 30:
    intermediate_score = 0
elif 25 <= BMI <= 29.9:
    intermediate_score = 3
elif 18.5 <= BMI <= 24.9:
    intermediate_score = 5
else:
    intermediate_score = 3


if previous_weight == -1:
    weight_change = 'NEW'
    last_visit = 'First visit'
else:
    weight_change = current_weight - previous_weight


final_score = intermediate_score + practitioner_assessment


if final_score > 5:
    health_condition = 'Great condition!'
elif 3 <= final_score <= 5:
    health_condition = 'Need a little work'
elif 1 <= final_score < 3:
    health_condition = 'Need a lot of work'
else:
    health_condition = 'At risk!'


print("Receipt for patient name:", name,)
print("patient weight:", current_weight)
print("Weight Change since last visit:", weight_change)
print("Days since last visit:", last_visit)
print("")
print("------------------------------")
print("")
print("BMI:", BMI)
print("Intermediate Health Score:", intermediate_score)
print("Practitioner's Assessment of Health:", practitioner_assessment)
print("")
print("------------------------------")
print("")
print("Final Score:", final_score)
print("Health Condition:", health_condition)