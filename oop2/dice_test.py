#import three classes from the cheatdice library
#allows us to create instances of the class and use
#inheritted functions
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice

#creates instance of Cheat_Swapper and Cheat_Loaded_Dice classes
cheater1 = Cheat_Swapper()
cheater2 = Cheat_Loaded_Dice()

#cheater1 and cheater2 use the 'roll' method inherited from the player class
cheater1.roll()
cheater2.roll()

#prints results of the 'get_dice' method for each player
print("Cheater 1 rolled" + str(cheater1.get_dice()))
print("Cheater 2 rolled" + str(cheater2.get_dice()))

#adds the three elemnents of the dice list for both players.
#if they are equal, notifies user
if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
  print("Draw!")

#if the sum is greater for cheater1, notifies user
elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
  print("Cheater 1 wins!")

#if the sum is greater for cheater2, notifies user
else:
  print("Cheater 2 wins!")