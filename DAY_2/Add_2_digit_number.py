# Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, 
# then the output should be 3 + 5 = 8

two_digit_number = input()
# 🚨 Don't change the code above 👆

####################################

# Write your code below this line 👇

num = int(two_digit_number)
sum=0
while(num>0):
    rem=num%10
    sum+=rem
    num//=10
print(sum)

# <----------------OR------------------------------------>

print(int(two_digit_number[0]) + int(two_digit_number[1]))