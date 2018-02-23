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
Commands:
start - starts the game from the main menu
info - gives info on the creator and the creation process
exit - exit the program
'''

badcom = '''
      Please enter a correct command
     For a list of commands, type help
'''

howtoplay = '''

'''

info = '''

'''

#exiting
def exiting():
  print "Now exiting the game of NIM"
  exit()

#startup
def startup():
  print startlogo
  print starttext
  
#info
def info():
  print info
  comready()

#maingame startup
def gameready():
  print howtoplay


  
#Command Ready Function
def comready():
  com = raw_input()
  if com == 'help':
    print helpline
    comready()
  elif com == 'exit':
    exiting()
  elif com == 'info':
    info()
  elif com == 'start':
    gameready()
  else:
    print badcom
    comready()
    
#Initial Startup
startup()
comready()