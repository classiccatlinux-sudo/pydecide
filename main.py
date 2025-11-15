import time
import random
import os

print("welcome to pydecide made by classic14")
time.sleep(2)
os.system('clear')
one = input("type opinon one:")
time.sleep(1)
os.system('clear')
two = input("type opinon two:")
time.sleep(1)
os.system('clear')
print("and it is...")
time.sleep(2)

options = (one, two)
chosen = random.choice(options)

print(chosen)





