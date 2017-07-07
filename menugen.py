import random
print("Will you be dining with us tonight?")
answer= input()
if answer=="yes":
    main = ["spaghetti","steak","eggplant parmesan"]
    side = ["vegetables","salad","potatoes"]
    dessert = ["pie","ice cream","cake"]
menu = ([main], [side] ,[dessert])
print((random.choice(side)), (random.choice(main)), (random.choice(dessert)))
