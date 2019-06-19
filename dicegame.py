"""This is the roll dice game in which user have to give the sum of the two dice rolled. """

from random import randint
from time import sleep 


def get_user_guess():
  guess = int(raw_input("Make a guess:"))
  return guess


def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "Max Val %d" % (max_val)
  guess = get_user_guess()
  
  if guess > max_val:
    print "Invalid Guess by User!"
  else:
    print "Rolling!!"
    sleep(2)
    print "First Roll %d" %(first_roll)
    sleep(1)
    print "Second Roll %d" %(second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print "Results is %d" % (total_roll)
    sleep(1)
  if guess == total_roll:
    print "You Win"
  else:
    print "You Lose"
roll_dice(6)  
    
  
  