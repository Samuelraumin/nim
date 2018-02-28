#The Game of NIM
#Created By Samuel

#import tags
import sys

#global headers and logo
startlogo = '''


__ __||           __|                    _ \  _|   \ |_ _|  \  |    *
   |    \   -_)  (_ |  _` |  ` \   -_)  (   | _|  .  |  |  |\/ |   ***
  _| _| _|\___| \___|\__,_|_|_|_|\___| \___/_|   _|\_|___|_|  _|  *****
'''
starttext = '''
                  Welcome to The Game of NIM
            For Commands and their functions, type help
                    For questions and feedback,
          please visit https://github.com/Samuelraumin/nim
                      Current Version: V0.01
'''

helpline = '''
Main Menu Commands:
start - starts the game from the main menu
exit - exit the program
'''

badcom = '''
      Please enter a correct command
     For a list of commands, type help
'''

howtoplay = '''
              There are three piles of three rocks
   You select what pile to pick rocks from, after you select what 
pile you want to pick from, you chose how many rocks you would like to
            take, whomever grabs the last rock wins!"
'''

info = '''


                      _ _|        _|      
                        |  __ \  |    _ \ 
                        |  |   | __| (   |
                      ___|_|  _|_|  \___/ 
                                          
Welcome to the game of NIM created by Sam Raumin and AJ Ogrodnick,
        we're student at Palm Desert High School in
          California in a Computer Science course.
'''
exitinglogo = '''
              
                  ______     _ __  _            
                 / ____/  __(_) /_(_)___  ____ _
                / __/ | |/_/ / __/ / __ \/ __ `/
               / /____>  </ / /_/ / / / / /_/ / 
              /_____/_/|_/_/\__/_/_/ /_/\__, /  
                                       /____/   
                        Thanks for playing :)
                            -Sam and AJ
'''
gamecommand = '''
Move - allow the current player to execute his turn, following the dialogue instructions.
status - list the amount of rocks in all three piles (does not use up a turn)
'''


#startup
def startup():
  print startlogo
  print starttext
  exit = 0
  while exit != 1:
    com = raw_input()
    if com == 'help':
      print helpline
    elif com == 'exit':
      print exitinglogo
      exit = 1
    elif com == 'info':
      inform()
    elif com == 'start':
      gameready()
    else:
      print badcom
  exit = 1
  
#info
def inform():
  print info
  startup()

#maingame startup
def gameready():
  print howtoplay
  global player1
  global player2
  player1 = raw_input("What would Player 1 like to be called:")
  player2 = raw_input("What would Player 2 like to be called:")
  print gamecommand
  gamestartup()

    
#Game Runtime
def gamestartup():
  global pile1
  pile1 = 3
  global pile2
  pile2 = 3
  global pile3
  pile3 = 3
  print "It is", player1, "'s turn first."
  gameaction1()
  
def gameaction1():
  action1 = 0
  while pile1 + pile2 + pile3 > 0:
    while action1 != 1:
      action = raw_input("Action: ")
      if action == "status":
        print "Pile 1 contains", pile1, "stones."
        print "Pile 2 contains", pile2, "stones."
        print "Pile 3 contains", pile3, "stones."
      elif action == "move":
        action1 = 1
      elif action == "help":
        print howtoplay
    gameruntime1()
  print player1, "has won the game."
  print "You will now be brought back to the main menu."
  startup()
    
#Game runtime
def gameruntime1():
  pilechoice = int(raw_input("Select a pile, ranging from 1 to 3 (number please): "))
  rockchoice = int(raw_input("How many rocks (number please):"))
  global pile1
  global pile2
  global pile3
  global pick
  pick = 0
  while pick != 1:
    if pilechoice == 1 and pilechoice <= pile1 and pilechoice <= 3: #or "pile 1" or "pile1":
      pile1 -= rockchoice
      pick += 1
    elif pilechoice == 2 and pilechoice <= pile2 and pilechoice <= 3: #or "pile 2" or "pile2":
      pile2 -= rockchoice
      pick += 1
    elif pilechoice == 3 and pilechoice <= pile3 and pilechoice <= 3: #or "pile 3" or "pile3":
      pile3 -= rockchoice
      pick += 1
    else:
      print "Not a defined action. Please choose an apporiate amount of stones."
      gameruntime1()
      
  print "OK.", player1, "picked up", str(rockchoice), "from pile", str(pilechoice), "."
  gameaction2()
  
def gameaction2():
  action1 = 0
  while pile1 + pile2 + pile3 > 0:
    while action1 != 1:
      action = raw_input("Action: ")
      if action == "status":
        print "Pile 1 contains", pile1, "stones."
        print "Pile 2 contains", pile2, "stones."
        print "Pile 3 contains", pile3, "stones."
      elif action == "move":
        action1 = 1
      elif action == "help":
        print howtoplay
    gameruntime2()
  print player2, " has won the game."
  print "You will now be brought back to the main menu."
  startup()
    
#Game runtime
def gameruntime2():
  pilechoice = int(raw_input("Select a pile, ranging from 1 to 3 (number please): "))
  rockchoice = int(raw_input("How many rocks (number please):"))
  global pile1
  global pile2
  global pile3
  global pick
  pick = 0
  while pick != 1:
    if pilechoice == 1 and pilechoice <= pile1 and pilechoice <= 3: #or "pile 1" or "pile1":
      pile1 -= rockchoice
      pick += 1
    elif pilechoice == 2 and pilechoice <= pile2 and pilechoice <= 3: #or "pile 2" or "pile2":
      pile2 -= rockchoice
      pick += 1
    elif pilechoice == 3 and pilechoice <= pile3 and pilechoice <= 3: #or "pile 3" or "pile3":
      pile3 -= rockchoice
      pick += 1
    else:
      print "Not a defined action. Please choose an apporiate amount of stones."
      gameruntime2()
      
  print "OK.", player2, "picked up", str(rockchoice), "from pile", str(pilechoice), "."
  gameaction1()

startup()