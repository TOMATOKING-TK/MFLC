import os
import math

add_per_level = 160
first_level = 200
kill_XP = 50

options = """
[1] how much more xp is needed for your next level goal
[2] how much xp is needed to go to that level from 0
"""

chose_list = [
    1,
    2
]

def clear():
    os.system('cls')

def get_start_level_XP(start_level):
    start_level_XP = 0
    for I in range(start_level):
        start_level_XP_cal = add_per_level * I; start_level_XP_cal += first_level; start_level_XP += start_level_XP_cal
    return start_level_XP

def calculator_from(start_level, go_level):
    clear()
    level_needed = go_level - start_level
    start_level_XP = get_start_level_XP(start_level); XP_amount = get_start_level_XP(go_level)
    XP_amount = XP_amount - start_level_XP
    kills_needed = XP_amount / kill_XP; kills_needed = math.ceil(kills_needed)
    print("these are the stats for your wanted level:")
    print("current level: " + str(start_level))
    print("wanted level: " + str(go_level))
    print("levels needed: " + str(level_needed))
    print("XP needed: " + str(XP_amount))
    print("raw kills needed: " + str(int(kills_needed)))
    input("press enter to go back")

def calculator_to(start_level):
    clear()
    XP_amount = get_start_level_XP(start_level)
    level_UP = get_start_level_XP(start_level + 1); level_UP = level_UP - XP_amount
    print("level: " + str(start_level))
    print(f"XP needed for {start_level} to {start_level + 1}: {level_UP}")
    print("XP needed: " + str(XP_amount))
    input("press enter to go back")

def main():
    print(options)
    chose = input()
    try:
        chose = int(chose)
    except:
        return
    if chose in chose_list:
        if chose == 1:
            start_level = input("what is your starting level: ")
            go_level = input("what is your level goal: ")
            try:
                start_level = int(start_level)
                go_level = int(go_level)
            except:
                return
            calculator_from(start_level, go_level)
        elif chose == 2:
            start_level = input("level: ")
            try:
                start_level = int(start_level)
            except:
                return
            calculator_to(start_level)
    else:
        print(f"\n{chose} is not an option")
        input("press enter to go back")

while True:
    clear()
    main()