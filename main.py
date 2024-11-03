import os
import platform
import random

while True:
  choices = ["rock", "paper", "scissors"]
  botChoice = random.choice(choices)
  
  if platform.system() == 'Windows':
    os.system('cls') 
  else: 
    os.system('clear')
    
  print("Rock Paper Scissors\n")
  print("Make your choice\n")
  choice = str(input())
  choice = choice.lower()

  if choice in choices:
    print(f"\nYou chose: {choice}")
    print(f"Bot chose: {botChoice}\n")

    if choice == botChoice:
      print("Tied!")
    if choice == "rock" and botChoice == "paper":
      print("You lost!")
    if choice == "paper" and botChoice == "rock":
      print("You won!")
    if choice == "rock" and botChoice == "scissors":
      print("You won!")
    if choice == "scissors" and botChoice == "rock":
      print("You lost!")
    if choice == "paper" and botChoice == "scissors":
      print("You lost!")
    if choice == "scissors" and botChoice == "paper":
      print("You won!")
    print("\nPress enter to continue")
    input()
    continue
  else:
    print("\nInvalid choice. (Try typing rock, paper, or scissors)\n")
    print("Press enter to continue")
    input()
    continue
  

