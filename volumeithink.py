import math
answer = input("Give me a radius and I'll give you the area of a sphere.")
r = answer
def area (answer):
    a = (4) * math.pi * int(answer)**2
    print(a)
    return(a)
area (int(answer))
