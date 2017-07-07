from random import randint
    #find the sum of all multiples of 3 and 5  in the list.
random1=[]
for i in range (100):
    random1.append(randint(10,99))
print(random1)
def onlist(random):
    for item in random:
        if (item % 5)== 0 or (item % 3== 0):
            print(item)
onlist(random1)
