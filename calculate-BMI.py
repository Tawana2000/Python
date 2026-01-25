#Given the height and weight of a person, calculate the BMI and alert the user about what they should do next.
#BMI is a number that tells how fit the human body is. It depends on height and weight.  #Your program should print the given string if the BMI is less than 18.5 - Underweight
#18.5 to 24.9 - Normal Weight
#25.0 to 29.9 - Overweight
#30.0 or more - Obese


def bmi_rate(weight, height):

    bmi = weight / (height **2)

    if bmi < 18.5:
        return 'Underweight'
    
    elif 18.5 <= bmi <= 24.9:
        return 'Normal Weight'
    
    elif  25.0 <= bmi <= 29.9:
        return 'Overweight'
    
    elif bmi >= 30.0:
        return 'Obese'
    
weight = float(input())
height = float(input())
print(bmi_rate(weight, height))
