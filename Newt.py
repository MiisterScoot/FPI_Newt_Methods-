import math
import numpy as np
import itertools
import matplotlib.pyplot as plt
#Finds nth root of any positive number

fig, axis = plt.subplots()
num = -1
while num <= 0:
    num = input("Enter a number: ")
    num = float(num)
    if num <= 0:
        print("Please enter a positive number")

root = 0
root_sel = False
while root_sel == False:
    root = input("What root of " + str(num) + " do you want? ")
    try:
        root = int(root)
        root_sel = True
    except ValueError:
        print("Your input must be a positive integer. Please try again")


def f(x, root, a):
    return x**root-a
def df(x, root):
    if root > 1:
        return root*(x**(root-1))
    if root == 1:
        return 1

x = 1.1
epsilon = .000000000001

for i in range(1000): #Newton's method in action 
    axis.scatter(i, x, color = "blue")
    x1 = x - f(x, root, num)/df(x, root)
    t = abs(x1 - x)
    if t < epsilon:
        print("Steps to converge: " + str(i+1))
        break
    x = x1
    i += 1

#displays value
if root == 1:
    print("The first root of " + str(num) + " is " + str(x))
elif root == 2:
    print("The second root of " + str(num) + " is " + str(x))
elif root == 3:
    print("The third root of " + str(num) + " is " + str(x))
else:
    print("The " + str(root) + "th root of " + str(num) + " is " + str(x))

plt.show()