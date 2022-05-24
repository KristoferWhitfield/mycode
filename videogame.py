#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
Alien
========
                                                      _____
                         .() .'()                    ( .--.)
                 .---.  / / / .'                     /.)  '
               .'     )/ /-/ /  .'()                ((/>
             .'    .---.( / (`./  .'
           .'     (-./  \\\_//  .'     _____
  ,-._.   /        <\//  \`--\_/\    .'     `-._       <,. \/>
,,== \> \/    .'.-' <\//  \   |  `---\    `--.  `-._/>_/>/>  )
    `(__/  (  |-<____<\/ .-')-+'``'`'`\       `.   _ __ __ _ \
        \.-<\ )--------)/  /      ///--\        )-' \> \> \>`'
          / )/        // /'`-----'      `-.    (___        `-._  _
        ,(   )
                / ||-- \                  / | ---\`         //---'
                 

You are an engineer on the ship U.S.S. Sulaco, there's an alien on board. Reach the escape
pods to get to saftey. Hide if you can if the alien is in the room. 
Commands:
  go [direction]
  get [item]
  hide [hidingspot]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Crew Quarters' : {
                  'south' : 'Main Hall'
                },
            'Main Hall' : {
                  'east' : 'Captains Quarters', 
                  'west' : 'Labs',
                  'south': 'Transportation Hub',
                },
            'Waste Disposal' : {
                  'east' : 'Transportation Hub' 
                  'item'  : 'monster',
                },
            'Labs' : {
                  'east' : 'Main Hall',
                  'item' : 'HBr acid'
               },
            'Captains Quarters' : {
                  'west' : 'Main Hall'
                  'item' : 'keycard'
               },
            'Transportation Hub' : {
                  'north' : 'Main Hall',
                  'south' : 'Escape Pods',
                  'west' : 'Waste Disposal', 
            },
            'Escape Pods' : {
                  'terminal' : 'cookie',

         }
        },
#start the player in the Hall
currentRoom = 'Crew Quarters'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
