from random import randint
    #find and print all multiples of 5 in the list.
random1=[]
for i in range (100):
    random1.append(randint(10,99))
print(random1)

def onlist(random):
    for item in random:
        if (item % 5)== 0:
            print(item)
onlist(random1)
