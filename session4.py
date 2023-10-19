patient_age = int(input("Enter your age: "))
if patient_age < 18:
  print("we recommend a high carbohydrate diet")
elif patient_age > 18 < 35:
  print("we recommend a high protein and lowwe carbohydrate diet")
elif patient_age > 35:
  print ("wwe recmmend a low sugar diet")


patient_height = float(input("Enter your height in meters: "))
patient_weight = float(input("Enter your weight in kilograms: "))
patient_physicalactvity = float(input("Enter your activity level (sedentary,moderate,active)"))
if patient_physicalactvity == "sedentary" or "moderate" and patient_age > 18 < 30:
  print ("You meed aerobic exercises.")
  
patient_bmi = patient_weight / (patient_height ** 2)
print("your bmi is:")
print(patient_bmi)

if patient_bmi < 18 and patient_physicalactvity == "sedentary":
  print ("You need to consult a nutritionist and increase your physical activities")

elif patient_bmi < 18 > 25 and patient_physicalactvity == "moderate":
  print ("You need to consult a nutritionist and increase your physical activities")
  
elif patient_bmi > 25 and patient_physicalactvity == "sedentary":
  print ("You need to consult a nutritionist and increase your physical activitie and reduce your weight")
