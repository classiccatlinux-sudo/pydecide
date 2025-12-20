from BASIC import *
import random

print("welcome to pydecide made by classic14")
time3()
clear()
one = input("type opinon one:")
os.system('clear')
two = input("type opinon two:")
clear()
print("and it is...")
time3()

options = (one, two)
chosen = random.choice(options)

print(chosen)
time3()
clear()
used()
time3()
clear()
exit()



