BlackPanther={'real name':"T'Challa",'First Appearance':'Fantastic Four (Vol. 1) #52 (July, 1966)','Creators':['Stan Lee','Jack Kirby'],'Powers':['Superhuman senses','Enhanced strength','durability','speed'],'equipment':['Vibranium claws','Vibranium daggers','Vibranium suit']}


BlackPanther.update({"suitColor" : "black"})

print(BlackPanther.keys())

# input() returns strings, so to save it as an integer you need int() to convert it
choice = int(input("Choose a number between 0-3 to see one of black panthers powers"))

print(f"Black Panther's power is {BlackPanther['Powers'][choice]}")

