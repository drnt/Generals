import numpy as np
import matplotlib.pyplot as plt


# single line comment

""" this is a multiline comment
  which spawns many lines"""

class RainDrop:
    """ This is the documentation string
    It can be multiple line long """


    """data members can be
    class variable or
    instance variable"""

    "this is a class variable"
    rdCount = 0

    "definition of methods"
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        RainDrop.rdCount += 1
    def displayCount():
        print("numOfInstances %d" % RainDrop.rdCount)
    def displayRainDrop(self):
        print("xPos : ", self.xPos, ", yPos: ", self.yPos)

"something here"
drop1 = RainDrop(1,1)
drop2 = RainDrop(2,2)
drop3 = RainDrop(3,3)
print("number is %d" % drop2.xPos)
print(drop2.xPos)
print(" ")
print(drop2.rdCount)
print(" ")
print(RainDrop.rdCount)
print(" ")
print(RainDrop.__dict__)
print(" ")
print(RainDrop.__doc__)
print(" ")
"displayCount(drop1)"
print(" ")
"displayRainDrop(drop1)"
print(" ")
print(RainDrop.rdCount)
RainDrop.displayCount()

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()


