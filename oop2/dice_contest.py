#import everything from the cheatdice library
#allows us to create instances of the class and use
#inheritted functions
from cheatdice import *
#create instances of Cheat_Swapper and Cheat_Loaded_Dice classes
swapper = Cheat_Swapper()
loaded_dice = Cheat_Loaded_Dice()
#set starting score and game count to 0 and specify # of games to run
swapper_score = 0
loaded_dice_score = 0
number_of_games = 100000
game_number = 0
#display something for the user to look at while the simulatin runs
print("Simulation running")
print("==================")
#begin while loop to run the simulatin repeatedly until we increment
#the gam_number counter all the way to the number_of_games
while game_number < number_of_games:
  #lets each player roll
  swapper.roll()
  loaded_dice.roll()

  #applies each players brand of cheating to the results of the 
  #previous 'roll' method
  swapper.cheat()
  loaded_dice.cheat()
   #Remove # before print statements to see simulation running
   #Simulation takes approximately one hour to run with print
   #statements or ten seconds with print statements
   #commented out

 #print("Cheater 1 rolled" + str(swapper.get_dice()))
 #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
 #Do nothing if there is a draw.  We are not counting them.
  if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()):
 #print("Draw!")
    pass
 #increment swapper's score by 1 if the sum of his three dice is 
 #greater   
  elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
 #print("Dice swapper wins!")
   swapper_score+= 1

 #increment loaded's score by 1 if the sum of his three dice is 
 #greater
  else:
 #print("Loaded dice wins!")
    loaded_dice_score += 1
  game_number += 1
#let the user know the results of the simulation
print("Simulation complete")
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score))
print("Loaded dice won: " + str(loaded_dice_score))
#notifies the user there was a draw if both scores are equal
if swapper_score == loaded_dice_score:
  print("Game was drawn")
#otherwise, print winner to console  
elif swapper_score > loaded_dice_score:
  print("Swapper won most games")
else:
  print("Loaded dice won most games")