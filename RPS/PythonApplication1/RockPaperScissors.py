﻿from random import *
from keyboard import *


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
    answer=input("Bot ili ne bot? bot/ne bot\n")
    answer=answer.lower()
    num=0
    winp1=0
    winp2=0
    p1=0
    p2=0
    while num < 1:
        selection = input("Что vibiraet player 1? Rock\Paper\Scissors: ")
        selection = selection.lower()
        if selection == "rock":
            print(rock)
        elif selection == "paper":
            print(paper)
        else:
            print(scissors)
    
        if answer == "ne bot":
            computer_chose = input("Что vibiraet player 2? Rock\Paper\Scissors: ")
            computer_chose = computer_chose.lower()
            if computer_chose == "rock":
                print(rock)
            elif computer_chose == "paper":
                print(paper)
            else:
                print(scissors)

        if answer == "bot":
            options = [rock, paper, scissors]
            computer_chose = choice(options)
            print("Computer chose:" , computer_chose)
        
        if p1 < 3 and p2 < 3:
            if p1 == 3:
                winp1+=1
                print("Player 1 win")
                num+=1
            if p2 == 3:
                winp2+=1
                print("Player 2 win")
                num+=1
        elif selection == "rock" and computer_chose == rock:
            print("Nichja")
        elif selection == "paper" and computer_chose == paper:
            print("Nichja")
        elif selection == "scissors" and computer_chose == scissors:
            print("Nichja")        
        elif selection == "rock" and computer_chose == scissors:
            print("You win")
            p1+=1
        elif selection == "paper" and computer_chose == rock:
            print("You win")
            p1+=1
        elif selection == "scissors" and computer_chose == paper:
            print("You win")
            p1+=1
        else:
            print("You lose")
            p2+=1
    print("Game over")
    print(f"Ochko p1 {winp1} \n Ochko p2 {winp2}" )
    a=input("Prodolzhim? da/net ")
    if a == "da":
        pass
    if a == "net":
        break
    
   