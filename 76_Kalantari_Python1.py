# -*- coding: utf-8 -*-
"""
Kavian Kalantari
Introduction to Mechanical Engineering
11/17/2018
"""

# Question 1:
x1 = (2+(4*5/2*4)-2)**3
x2 = int((2+4)*5/2*4-2**3) #in your instructions you said to make
x3 = int(2+4*5/2*4-2**3)  # x3 equal to exactly 34 which is why I used int()

print(x1)
print(x2)
print(x3)
#make sure to make decimals match what Wanklyn
#says explicitly

#%%
# Question 2:

import cmath
a = 1
b = 5
c = 6

discriminant = cmath.sqrt(abs(((b*b)-4*a*c)))

root1 = (-b + discriminant)/(2*a)
root2 = (-b - discriminant)/(2*a)

print("root1 = {} root2 = {}".format(root1, root2))

#%%
# Question 3:

m = int(input('Enter an integer: '))
m = m%2

oddEven = ["m is even", "m is odd"]
print(oddEven[m])

#%%
# Question 4:

import math

angle1 = math.asin(3/5)
angle2 = math.asin(4/5)
#values are returned in radians

angle1 = round(angle1*(180/math.pi),2)
angle2 = round(angle2*(180/math.pi),2)

print("The angles are", + angle1, "and", + angle2)

#%%
# Question 5:
sides = []
sides.append(2)
sides.append(round(2*math.sin(60*math.pi/180),2))
sides.append(round(2*math.sin(30*math.pi/180),2))
print("The side lengths are", + sides[0], ",", + sides[1], ", and", + sides[2])
#%%
# Question 6:

lst = [1,2,3,4,5,6,7,8,9]

lst.insert(3, "K-State")

lst.remove(1)
lst.remove(2)
lst.remove(5)
lst.remove(7)
lst.remove(8)
lst.remove(6)
lst.insert(4,6)
print (lst)
#%%