'''Snake , water, gun , is a variation of the children's game "rock-paper-scisorrs
"where players use hand gestures to represent a snake,water, or a gun . The gun 
beats the snake,the snake beats the water,and the water beats the gun .

Create the game using if - else statements . Do not use fancy gui. Use proper functions to check win'''

import random

print("Lets play Snake, water and gun game")
print("-----------------------------------")

def game(comp,me):
  if comp==me:
    return None
  elif comp=="s":
    if me=="w":
      return False
  elif me=="g":
      return True
  elif comp=="w":
    if me=="g":
     return False
  elif me=="s":
     return True
  elif comp=="g":
    if me=="s":
     return False
  elif me=="w":
     return True
    
print("Computer's turn:Snake(s) Water(w) or Gun(g)")
print("---------------------------------------------")
num=random.randint(1,3)
if num==1:
  comp="s"
elif num==2:
  comp="w"
elif num==3:
  comp="g"
me=input("Please choose:Snake(s)Water(w)orGun(g)?\n")
a=game(comp,me)
print(f"The computer chooses\t {comp}\n")
print(f"You choose\t {me}\n")
if a==None:
  print("The game is tie!")
elif a:
  print("you win!")
else:
  print("you lose!")



    
    