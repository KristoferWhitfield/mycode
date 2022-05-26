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
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print(rooms[currentRoom]['desc'])
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
                  'south' : 'Main Hall',
                  'desc' : 'You come out from your locker and look around, you can head sout                            h to leave'
                },
            'Main Hall' : {
                  'east' : 'Captains Quarters', 
                  'west' : 'Labs',
                  'south': 'Transportation Hub',
                  'desc' : 'You enter the main hall east brings you to the captains room that he has a keycard to give you access to all rooms, west brings you to the labs that have some powerful chemicals against alien hide, south brings you to the transportation hub where the escape pods will be',
                },
            'Waste Disposal' : {
                  'east' : 'Transportation Hub',
                  'desc' : 'You enter waste management, but the xenomorph leaps out towards you.', 
                  'item'  : 'monster',
                },
            'Labs' : {
                  'east' : 'Main Hall',
                  'desc' : 'You enter the labs full of chemicals and see a powerful acid',
                  'item' : 'HBr acid'
               },
            'Captains Quarters' : {
                  'west' : 'Main Hall',
                  'desc' : 'You enter the prestine captains quarters, his keycard is on the desk',
                  'item' : 'keycard'
               },
            'Transportation Hub' : {
                  'north' : 'Main Hall',
                  'south' : 'Escape Pods',
                  'west' : 'Waste Disposal',
                  'desc' : 'You enter the transportation hub, south brings you to the escape pods, but theres a keypad on the door. West brings you to waste management where you hear some noise coming from that direction. Maybe theres survivors there.',
            },
            'Escape Pods' : {
                  'desc' : 'You see a keypad to be able to get into the escape pods, but oh no the xenomorph has spoted you.', 
                  'item' : 'keycard',

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
  if currentRoom == 'Escape Pods' and 'keycard' in inventory:
    print('''
    You put the captains keycard in and rush into the escape pods. You escaped safely YOU WIN
                         `. ___
                    __,' __`.                _..----....____
        __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
  _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
,'________________                          \`-._`-','
 `._              ```````````------...___   '-.._'-:
    ```--.._      ,.                     ````--...__\-.
            `.--. `-`                       ____    |  |`
              `. `.                       ,'`````.  ;  ;`
                `._`.        __________   `.      \'__/`
                   `-:._____/______/___/____`.     \  `
                               |       `._    `.    \
                               `._________`-.   `.   `.___
                                             SSt  `------'`
                                             ''')
    break



  ## If a player enters a room with a monster
  elif currentRoom == 'Escape Pods' and 'keycard' not in inventory:
    print('''
    The xenomorph got you GAME OVER
                             .---._
                                  /==----\_
                 |\              |8=---()-\|   |\
         /|      ::\             |8=-/|\(_)>_   \\
         |:\     `::\_            \=/:\= (_)\|   |\
         `::|     |::::.            \;:\=\(_)>_  |\\
          |b\\_,_ \`::::\             \:\=\( \/  \_(
          `\88b`\|/|'`:::\   .-----   :8:\=|`=>_  [d[
           \;\88b.\=|///::`-/::;;;;:\ |8;|=\( )/   [8[
      __    ||/`888b.\_\/\:/:;/'/-\::\/( \|=(=)>_  [d|
     //):.. `::|/|\"96.\|//;/|'| /-\::+\|-\=(. )/  [8[
    |(/88e::.. `'.|| "min;/\\/8|\.-|::|8|||=|`='_  `[d|
     `-|8888ee::,,,`\/88utes8P//8|-|::|8||\=|( )/   ]8[
      |:`"|####b:::/8pq8e/::'`;q8|/::dP'|\|=|`='_   [d|
 .=-. \::..`""##Gst:q| e|:/..\:|8|.:/|'/\/|/|(_)/   ]8[
/(,:;:, \::::.\#/88q;`;'\||.:/-//.;/<8\\\^\||./>    `]d[
`8888b::,,_ ::/88q;.`;|d8/`-.]/|./  |8|\|:|;/.d|     [8|
  `"88###n::-/d8P.\e/-|d/ _//;;|/   |8(|::(/).8/     ]d[
    `"###o2:1dP;`q./=/d/_//|8888\   ;8|^\/`-'8/      [8\
       `"v7|9q8e;./=/d//=/\|eeeb|  /dP= =<ee8/       ]d-
          \|9; qe/-d/ .|/=/888|:\ `--=- =88p'        [8[
          (d5b;,/ d/.|/=-\Oo88|:/                   ,8_\
         _|\q88| d/ /'=q8|888/:/                    ]d|
        _\\\/q8/|8\_""/////eb|/_                    [8_\
        \|\\<==_(;d888b,.////////--._               ]8|
       _/\\\/888p |=""";;;;`eee.////.;-._          ,8p\
      /,\\\/88p\ /==/8/.'88`""""88888eeee`.        ]8|
    .d||8,\/p   /-dp_d8|:8:.d\=\    `""""|=\\     .[8_\
    |8||8||8.-/'d88/8p/|:8:|8b\=\        /|\\|    ]8p|
    |8||8||8b''d.='8p//|:8:'`88b`\       |||||)   [8'\
    `8b:qb.\888:e8P/'/P'8:|:8:`888|      |'\||'  /8p|
     q8q\\qe---_P;'.'P|:8:|:8:|`q/\\     '_///  /8p_\
     _|88b-:==:-d6/P' |8::'|8:| ,|\||    '-=' .d8p/
    |__8Pdb-q888P-'  .:8:| |8:| |/\||\     .-e8p/\|
     .-\888b.__      |:8/' |8:| \ _|;|,-eee8\8\|
     \.-\'88/88/e.e.e|8/|\_--.-.-e8|8|88\8p\|
       .'`-;88]88|8|/':|:\ `q|8|8|8'-\| \|
        `' || || |_/(/|;\)`-\\`--,\|
              `' /v"""' `""""""vVV\
                              ''')
    break

  ## If a player enters a room with a monster
if currentRoom == 'Waste Disposal' and 'HBr' not in inventory:
    print('''
    The xenomorph got you GAME OVER
            .---._
                                  /==----\_
                 |\              |8=---()-\|   |\
         /|      ::\             |8=-/|\(_)>_   \\
         |:\     `::\_            \=/:\= (_)\|   |\
         `::|     |::::.            \;:\=\(_)>_  |\\
          |b\\_,_ \`::::\             \:\=\( \/  \_(
          `\88b`\|/|'`:::\   .-----   :8:\=|`=>_  [d[
           \;\88b.\=|///::`-/::;;;;:\ |8;|=\( )/   [8[
      __    ||/`888b.\_\/\:/:;/'/-\::\/( \|=(=)>_  [d|
     //):.. `::|/|\"96.\|//;/|'| /-\::+\|-\=(. )/  [8[
    |(/88e::.. `'.|| "min;/\\/8|\.-|::|8|||=|`='_  `[d|
     `-|8888ee::,,,`\/88utes8P//8|-|::|8||\=|( )/   ]8[
      |:`"|####b:::/8pq8e/::'`;q8|/::dP'|\|=|`='_   [d|
 .=-. \::..`""##Gst:q| e|:/..\:|8|.:/|'/\/|/|(_)/   ]8[
/(,:;:, \::::.\#/88q;`;'\||.:/-//.;/<8\\\^\||./>    `]d[
`8888b::,,_ ::/88q;.`;|d8/`-.]/|./  |8|\|:|;/.d|     [8|
  `"88###n::-/d8P.\e/-|d/ _//;;|/   |8(|::(/).8/     ]d[
    `"###o2:1dP;`q./=/d/_//|8888\   ;8|^\/`-'8/      [8\
       `"v7|9q8e;./=/d//=/\|eeeb|  /dP= =<ee8/       ]d-
          \|9; qe/-d/ .|/=/888|:\ `--=- =88p'        [8[
          (d5b;,/ d/.|/=-\Oo88|:/                   ,8_\
         _|\q88| d/ /'=q8|888/:/                    ]d|
        _\\\/q8/|8\_""/////eb|/_                    [8_\
        \|\\<==_(;d888b,.////////--._               ]8|
       _/\\\/888p |=""";;;;`eee.////.;-._          ,8p\
      /,\\\/88p\ /==/8/.'88`""""88888eeee`.        ]8|
    .d||8,\/p   /-dp_d8|:8:.d\=\    `""""|=\\     .[8_\
    |8||8||8.-/'d88/8p/|:8:|8b\=\        /|\\|    ]8p|
    |8||8||8b''d.='8p//|:8:'`88b`\       |||||)   [8'\
    `8b:qb.\888:e8P/'/P'8:|:8:`888|      |'\||'  /8p|
     q8q\\qe---_P;'.'P|:8:|:8:|`q/\\     '_///  /8p_\
     _|88b-:==:-d6/P' |8::'|8:| ,|\||    '-=' .d8p/
    |__8Pdb-q888P-'  .:8:| |8:| |/\||\     .-e8p/\|
     .-\888b.__      |:8/' |8:| \ _|;|,-eee8\8\|
     \.-\'88/88/e.e.e|8/|\_--.-.-e8|8|88\8p\|
       .'`-;88]88|8|/':|:\ `q|8|8|8'-\| \|
        `' || || |_/(/|;\)`-\\`--,\|
              `' /v"""' `""""""vVV\
                              ''')
    break


  elif currentRoom == 'Waste Disposal' and 'HBr' in inventory:
     print('''
      You threw the acid at the xenomorph and it melted, YOU WIN
                                                   _,'/
                                  _.-''._:
                          ,-:`-.-'    .:.|
                         ;-.''       .::.|
          _..------.._  / (:.       .:::.|
       ,'.   .. . .  .`/  : :.     .::::.|
     ,'. .    .  .   ./    \ ::. .::::::.|
   ,'. .  .    .   . /      `.,,::::::::.;\
  /  .            . /       ,',';_::::::,:_:
 / . .  .   .      /      ,',','::`--'':;._;
: .             . /     ,',',':::::::_:'_,'
|..  .   .   .   /    ,',','::::::_:'_,'
|.              /,-. /,',':::::_:'_,'
| ..    .    . /) /-:/,'::::_:',-'
: . .     .   // / ,'):::_:',' ;
 \ .   .     // /,' /,-.','  ./
  \ . .  `::./,// ,'' ,'   . /
   `. .   . `;;;,/_.'' . . ,'
    ,`. .   :;;' `:.  .  ,'
   /   `-._,'  ..  ` _.-'
  (     _,'``------''  SSt
   `--''
                              ''') break
