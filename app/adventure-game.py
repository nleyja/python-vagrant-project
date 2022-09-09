import time
import csv

data_header = ["intro_choice", "goodNeighbor_choice"]

data = {
  'intro_choice' : '',
  'goodNeighbor_choice' : ''
}

class Answers:
  first = ["A", "a"]
  second = ["B", "b"]

Answer_A = Answers.first
Answer_B = Answers.second

def save_input(player_input):
  with open('gameLog.txt', mode='a', encoding= 'UTF8', newline='') as gameLog:
    gameLog.write(player_input)
  
    

# Pick player option ///
player_style = 0

user_in = int(input("input number 1, 2, or 3 to select character: "))
time.sleep(2)
print(" ")

if user_in == 1:
    player_style = 1
elif user_in == 2:
    player_style = 2
elif user_in == 3:
    player_style = 3
else:
    print("not valid character choice")

def class_selection(character):
  if character == 1:
    print("you have selcted Dad watching football to answer the door.")
  elif character == 2:
    print("you have selcted Mom shopping online to answer the door.")
  elif character == 3:
    print("You have selcted a Kid on TikTok to answer the door.")

    print(" ")

if player_style != 0:
  class_selection(player_style)

  print(" ")

  # Intro ////

  def intro():
      print(" ") 
      print("This story will take you down a strange path where reality doesnt make sense, Do you still want to continue? ")
      time.sleep(2)
      print( """A. Yes, proceed"""
        """   B. No, I'm scared""")

      print(" ")
      while True:
        choice = input("What is your choice? ")
        save_input(choice)
        # data["intro_choice"] = choice
        time.sleep(2)
        if choice in Answer_A:
          getInCar()
          break
        elif choice in Answer_B:
          print("I kinda need you to pick A, try again")
          intro()
          break
        else:
          print("Not a valid choice... Try again, choose A or B")
          intro()

  # first descsions /////

  def goodNeighbor():
    print(" ")
    print("You hear a knock at the door, your neighbor ask you for help. Do you help or respectfully decline? (help/decline) ")
    time.sleep(2)
    print(" ")
    print( """A. I'm a good neighbor, I'll help"""
          """   B. Politley decline""")

    print(" ")
    while True:
      choice = input("What is your choice? ")
      save_input(choice)
      # data["goodNeighbor_choice"] = choice
      if choice in Answer_A:
        getInCar()
        break
      elif choice in Answer_B:
        print("Not the best choice, you might as well start over")
        goodNeighbor()
      else:
          print("Not a valid choice... Try again, choose A or B")
          goodNeighbor()
          print(" ")


# Second Decision

  def getInCar():
    print(" ")
    print("Your neighbor's car is stuck in the street. She's says it won't reverse. Do you get in the car? ")
    time.sleep(2)
    print(" ")
    print( """A. Sure, I'll see what I can do"""
            """   B. Sorry, I dont know how to drive""")
    print(" ")
    while True:
      choice = input("What is your choice? ")
      save_input(choice)
      if choice in Answer_A:
        helpCat()
        break
      elif choice in Answer_B:
        print("You'll never get invited the the BBQ, Try again.")
        getInCar()
      else:
        print("Not a valid choice... choose A or B")
        getInCar()
        print(" ")


  # 3rd decision

  def helpCat():
    print(" ")
    print("You are able to get the car to move, as you drive to your neighbor's house to park the car, you hear a cat crying in the back seat. Do you help the cat? ")
    time.sleep(2)
    print(" ")
    print( """A. No, you shouldn't mess with people's animals"""
            """   B. Sure, what could be the harm""")
    print(" ")
    while True:
      choice = input("What is your choice? ")
      save_input(choice)
      if choice in Answer_A:
        reverseCar()
        break
      elif choice in Answer_B:
        print("Dummy, the cat just scracted your eyes out, now your blind, Try again.")
        helpCat()
      else:
          print("Not a valid choice... choose A or B")
          helpCat()
          print(" ")

  def reverseCar():
    print(" ")
    print("You park the car in the driveway, but she wants you to reverse the car in the drivway. But remember, thats how she got stuck in the first place. do you try and reverse the car in to the driveway? ")
    time.sleep(2)
    print(" ")
    print( """A. I've done this much, might as well try to make her happy"""
            """   B. I've already parked the car, i've done enough""")
    print(" ")
    while True:
      choice = input("What is your choice? ")
      save_input(choice)
      if choice in Answer_A:
        print("You WIN, but the neighbors talks to you for another 30 mins until your face melts off and now you have fleas from the cat in the back seat. You walk home face in hand, but hey, you really are a great neighbor, Congrats.")
        endGame()
        break
      elif choice in Answer_B:
        print("You were so close you being neighbor of the year.")
        reverseCar()
      else:
        print("You were so close you being neighbor of the year, but YOU LOSE!!")

  def endGame():
    print("Thanks for playing")

intro()

