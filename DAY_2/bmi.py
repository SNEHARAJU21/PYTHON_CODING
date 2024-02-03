# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# BMI = weight
#       ------
#       height^2
# You should convert the bmi to a whole number and print out a whole number

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
h=float(height)
w=float(weight)
bmi=w/(h**2)
print(int(bmi))