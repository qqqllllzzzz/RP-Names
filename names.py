import random
import keyboard
import time

def Logo():
    print("by qualzed\nPress 'H' to start")

def Func():
    print("Press 'spacebar' if you want get again random name\nPress SpaceBar to generate")

    while 1:
        if keyboard.is_pressed('space'):
            time.sleep(0.4)
            rand_name = random.choice(name_list)
            rand_surname = random.choice(surname_list)
            print("Your Name: " + rand_name + " " + rand_surname)

name_list = ["James", "Karl", "Kevin", "Matthew", "Yan", "Kay", "Ethan", "Jimmy", "Christ", "Leonardo", "Noah", "Cliford", "Kyle", "Kurt", "Steve", "Tyler", "Travis", "Michael", "Oliver", "Liam", "Benjamin", "Brian", "Ryan", "Antrony", "Andrew", "Brandon", "Jack", "Jeffrey", "Diego", "Kennedy", "Gerald"]
surname_list = ["Smith", "Brown", "McDonald", "Wilson", "Miller", "Torres", "Sanchez", "Evans", "Harris", "Rogriguez", "Martinez", "Moore", "Lee", "Walker", "Allen", "Parker", "Campbell", "Phillips", "Roberts", "Murphy", "Cox", "Richardson", "Perry", "Patterson", "Anderson", "Wright", "Mitchell", "Winterkorn", "Dickenson"]

Logo()
while 1:
    if keyboard.is_pressed('H'):
        Func()