import random
print("Boy or girl?")
answer= input()
if answer=="boy":
    boyname = ["Tim", "Tom", "Daniel", "John"]
        #secure_random = random.SystemRandom()
    print(random.choice(boyname))
if answer=="girl":
    girlname = ["Jessica", "Anne","An","Ann"]
    #secure_random = random.SystemRandom()
print(random.choice(girlname))
