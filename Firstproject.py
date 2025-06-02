import random
import time
chatPlaces = ["The beach","anywhere with snow","any big city","walking in the hills"]
print("Welcome to chatbot!")
name = input("What's your name?")
print("Hi there", name, "It's great to meet you!")
place = input("Where is your favourite place to be?")
time.sleep(2)
print("That sounds great, I really love", random.choice(chatPlaces))
day = input("Have you ad a good day?")
day= day.lower()
if day == "yes":
    print("ok")
else:
    print("ok")
