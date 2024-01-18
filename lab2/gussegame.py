# -*- coding: utf-8 -*-
"""gusseGame.ipynb
"""

import random
lower, upper = int(input("Enter lower limit: ")), int(input("Enter upper limit: "))
num = random.randint(lower, upper)

while 1:
  guess = int(input("Enter your guess: "))
  if guess > lower and guess < num:
    print("Guess is too low")
    continue
  elif guess < upper and guess > num:
    print("Guess is too high")
    continue
  elif guess == num :
    print("Your guess is correct")
    break
