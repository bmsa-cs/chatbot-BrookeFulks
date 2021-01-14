"""
Chatbot
Author: 
Period/Core: 

"""

import os
import importlib.util

import random



def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)

def main():
  """This function contains all code for the chatbot."""
  print("Hello!")

  n = input("What is your name:")
  print ("Hi" + " "+ n)
  if n == "brooke":
    print ("My name is also brooke")
  elif n == "nathan":
    print("nathan is also my brothers name")
  else:
    print ("My name is Brooke")


  m = input("What would you say your current mood is?")
  if m == "happy":
    print ("That is good to hear")
  else:
    print ("It's okay everyone has off days")
  

  s = int(input("How many siblings do you have? "))
  if s == 1:
    print("I also have one sibling")
  elif s == 0:
    print ("So your an only child ")
  else:
    print ("That's cool, I only have a younger brother")

  x = random.randint(1,5)
  if x == 1:
    print("Hello")
  elif x == 2:
    print ("Bye")
  elif x == 3:
    print("Same Bro")
  elif x == 4:
    print ("Ur dumb")
  elif x == 5:
    print ("so what")

  c = input("What is your favorite color?")
  if c == "blue":
    print("That is also my favorite color")
  else:
    print("That is a pretty color")
  
  s = input("Do you play any sports")
  if s == "bowling":
    print "I also bowl"
  elif s == "no":
    print "Thats okay you don't have to"
  else:
    print("Thats  cool sport")
    
  #Below Is my Final line of code/Closing Statement 
  print ("Its was nice to meet you" + " " + n + " " + "I am always here to chat!")
  
if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()