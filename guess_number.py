import random
from random import randint
logo=""""
  ▄████  █    ██ ▓█████   ██████   ██████    ▄▄▄█████▓ ██░ ██ ▓█████     ███▄    █  █    ██  ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  
 ██▒ ▀█▒ ██  ▓██▒▓█   ▀ ▒██    ▒ ▒██    ▒    ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀     ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▓██  ▒██░▒███   ░ ▓██▄   ░ ▓██▄      ▒ ▓██░ ▒░▒██▀▀██░▒███      ▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
░▓█  ██▓▓▓█  ░██░▒▓█  ▄   ▒   ██▒  ▒   ██▒   ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒▒▒█████▓ ░▒████▒▒██████▒▒▒██████▒▒     ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒
 ░▒   ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░     ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░ ░░▒░ ░ ░  ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░       ░     ▒ ░▒░ ░ ░ ░  ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
░ ░   ░  ░░░ ░ ░    ░   ░  ░  ░  ░  ░  ░       ░       ░  ░░ ░   ░         ░   ░ ░  ░░░ ░ ░ ░      ░    ░    ░    ░     ░░   ░ 
      ░    ░        ░  ░      ░        ░               ░  ░  ░   ░  ░            ░    ░            ░    ░         ░  ░   ░     
                                                                                                             ░                 
"""
LV1=7
LV2=5
LV3=3

def set_level():
    level=input("choose your level: 1.level 1, 2. level 2, 3, level 3 :")
    if level=="1":
        print("you have 7 turns")
        return LV1
    elif level=="2":
        print("you have 5 turns")
        return LV2
    else:
        print("you have 3 turns")
        return LV3
#lv1=7, lv2=5, lv3=3 chances

def check_answer(ran_num, guess_num, turns):
    if 100<guess_num:
        print("out of range no reduction of turns")
    elif 0>guess_num:
        print("out of range no reduction of turns")
    elif ran_num==guess_num:
        print("correct")
        return turns-1
    elif ran_num>guess_num:
        print("up")
        return turns - 1
    elif ran_num<guess_num:
        print("down")
        return turns - 1

turns=0
def guess_game():
    print(logo)
    ran_num=random.randint(1, 100)
    print(f"{ran_num}")


    turns = set_level()
    guess_num=0
    while guess_num!=ran_num:

        guess_num=int(input("guess the number:"))

        turns=check_answer(ran_num, guess_num, turns)
        print(f"you have {turns} turns left guess again")
        if turns==0:
            print("you have out of turns")
            return
guess_game()