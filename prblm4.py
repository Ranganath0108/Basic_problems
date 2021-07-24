"""4. Write a Python program which accepts the radius of a circle from the user and compute the area."""
"""Sample Output :
r = 1.1
Area = 3.801327110843650"""


from math import pi
r=float(input("Enter the radius of the circle:"))
Area=pi*(r)**2
print(f"{r=} \n{Area=}")