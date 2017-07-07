import math
answer = input("Give me a radius and I'll give you the volume.")
r = answer
def volume (answer):
    v = (4/3) * math.pi * int(answer)**3
    print(v)
volume(int(answer))
