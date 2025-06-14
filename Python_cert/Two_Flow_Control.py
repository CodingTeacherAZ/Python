'''
2. Flow Control with Decisions and Loops 
2.1 Construct and analyze code segments that use branching statements 
• if, elif, else, nested and compound conditional expressions 


'''

#### if, elif, else
# Constants
pounds_to_kg = 0.453592
inches_to_meters = 0.0254

# Given information
height_feet = int(input("Enter the feet part of your height : "))
height_inches = int(input("Enter the inches part of your height : "))
weight_pounds = int(input("Enter your weight in pounds : "))
age = int(input("Enter your age : "))
# Convert height to meters
height_meters = (height_feet * 12 + height_inches) * inches_to_meters

# Convert weight to kilograms
weight_kg = weight_pounds * pounds_to_kg

# Calculate BMI
bmi = weight_kg / (height_meters ** 2)

print(f"Your BMI is: {bmi:.2f}")

young = age < 45
slim = bmi < 22.0

if young and slim:
    risk = "low"
elif (young and not slim) or (not young and slim):
    risk = 'medium'
else:
    risk = 'high'
print(f"Your heart attack risk is {risk}")

######## nested if, elif, else
value = input("Enter the pH level between 0 and 14: ")
if len(value) > 0:
    ph = float(value)
    if ph < 7.0:
        print(ph, ' is acidic.')
    elif ph > 7.p:
        print(ph, ' is basic.')
    else:
        print(ph, ' is neutral')
else:
    print('No pH value was given!')




