"""This is a game of 
rock paper 
scissors"""
from random import randint
options = ["ROCK","PAPER","SCISSORS"]
message = { 
            "tie" : "Yawn its a tie",
            "won" : "Yay tou won!", 
            "lost" : "Aww you Lost!"
          }
def decide_winner(user_choice,computer_choice):
  print ("User choice %s" %(user_choice))
  print ("Computer choice %s" %(computer_choice))
  if user_choice == computer_choice:
    print ((message["tie"]))
  elif user_choice == options[0] and computer_choice == options[2]:  
    print (message["won"])
  elif user_choice == options[1] and computer_choice == options[0]:  
    print (message["lost"])
  elif user_choice == options[2] and computer_choice == options[1]:  
    print (message["won"] )
  else:
    print (message["lost"])


def play_RPS():  #enter user and computer choice.
  user_choice = (raw_input("Enter Rock, Paper, or Scissors:")).lower()
  
  computer_choice =options[randint(0,2)]
  decide_winner(user_choice,computer_choice)

play_RPS()  
