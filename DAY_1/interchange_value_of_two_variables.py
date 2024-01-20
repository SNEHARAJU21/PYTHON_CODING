# A program to intechange the values of two variable and print the results
# ex : a = 10
#      b = 20
# O/P ---> a = 20 and b = 10


a = input()
b = input()
temp = a
a = b
b = temp
print("a: "+a)
print("b: "+b)

#  <----- WITHOUT USING TEMPORARY VARIABLE ----->
a = int(input())
b = int(input())
a = a + b
b = a - b
a = a - b
print ("a: "+str(a))
print ("b: "+str(b))

# <----- * / ----->
a = int(input())
b = int(input())
a = a * b
b = a / b
a = a / b
print("a: "+str(a))
print("b: "+str(b))

# <----- EXOR ----->
a = int(input())
b = int(input())
a = a ^ b
b = a ^ b
a = a ^ b
print("a: "+str(a))
print("b: "+str(b))

# <----- bitwise and + ----->
a = int(input())
b = int(input())
a = (a & b) + (a | b)
b = a + (~b) + 1
a = a + (~b) + 1
print("a: "+str(a))
print("b: "+str(b))

# <----- one line code ----->
a = int(input())
b = int(input())
a = (a + b) - (b := a)
print("a: "+str(a))
print("b: "+str(b))

# <----- one line code ----->
a = int(input())
b = int(input())
a = (a * b) / (b := a)
print("a: "+str(a))
print("b: "+str(b))

# <----- one line code ----->
a = int(input())
b = int(input())
a = (a ^ b) ^ (b := a)
print("a: "+str(a))
print("b: "+str(b))

# <----- one line code ----->
a = int(input())
b = int(input())
a,b = b,a
print("a: "+str(a))
print("b: "+str(b))


