#CodeCademy Project

import random

name = "Jeremy"
question = "Will I win the lottery tonight?"
answer = ""
random_number = random.randint(1, 15)

# TEST RANDOM FUNCTIONALITY
# print(random_number)

if random_number == 1:
 answer = "Yes - definitely!"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very Doubtful"
elif random_number == 10:
  answer = "Very Probable"
elif random_number == 11:
  answer = "Only Time Will Tell"
elif random_number == 12:
  answer = "The God's are saying...yes?"
elif random_number == 13:
  answer = "Is it not obvious?"
elif random_number == 14:
  answer = "Ask your spirit guide"
elif random_number == 15:
  answer = "Absolutely NOT"
else:
 answer = "Error"


if name == "":
  print("Who are you, and what do you want!?")
elif name == "Jeff" and question == "":
  print("Hi!", name, "What question do you have for me?")
else:
  print(name, "asks:", question)
  print("Magic 8-Ball's answer:", answer)
