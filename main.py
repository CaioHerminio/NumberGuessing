import random
from random import randint
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}")

def set_difficulty():
  level = input("Choose the difficulty. Type 'easy' or 'hard':")
  if level == "easy":
    return EASY_LEVEL
  else:
    return HARD_LEVEL

def game():
  print(logo)
  print("NUMBER GUESSING GAME!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint (1,100)
  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()

