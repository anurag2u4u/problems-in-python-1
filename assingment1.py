#1.
#name=input("enter your name")
#print("welcome",name)

#2.
#num1=int(input("enter first number : "))
#num2=int(input("enter second number: "))
#z=num1+num2
#print("value :",z)

#3.
#num1=float(input("enter the temperature in celsius"))
#fahrenheit=9/5*(num1)+32
#print("temperature in fahrenheit is :",farenhite)

#4.
#principal=float(input("enter the principal value :"))
#time=float(input("enter the time :"))
#rate=float(input("enter the rate :"))
#val=(principal*rate*time)/100
#print("simple interest",val)

#5.
#seconds=int(input("enter the seconds"))
#hrs=int(seconds/3600)
#rem=seconds%3600
#mins=int(rem/60)
#sec=int(rem%60)
#print("hours",hrs)
#print("seconds",sec)
#print("minutes",mins)

#6.
"""
num1=int(input("enter the number"))
num2=int(input("enter the second"))
var=num1
num1=num2
num2=var
print("num1:",num1)
print("num2:",num2)
"""

#7.
"""
a=int(input("Enter value : "))
b=int(input("Enter value : "))

a=a+b 
b=a-b
a=a-b

#a,b=b,a   is also possible
print("After swapping a becomes :",a)
print("After swapping b becomes :",b)

"""
#8.
"""
from math import pi as k
rad=float(input("enter the value of radius of circle"))
area=k*rad*rad
crf=2*k*rad
print("area is",area)
print("circumference is",crf)
"""

#9.
"""
len=float(input("enter the length of rectangle :"))
brd=float(input("enter the breadth of rectangle :"))
area=len*brd
perimeter=2*(len+brd)
print("area",area)
print("perimeter",perimeter)

"""
#10.
"""
a=float(input("a"))
b=float(input("b"))
c=float(input("c"))

s=(a+b+c)/2
import math_________

area=math.sqrt(s*(s-a)*(s-b)*(s-c))_______
print(area)

"""

#11.

p=float(input("enter the principal value"))
r=float(input("enter the rate"))
t=int(input("enter the time"))
ci=(p*((1+(r/100))**t))-p
print(ci)

 





























