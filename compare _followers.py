import random
from compare_data import data
logo='''
   ▄▄▄▄███▄▄▄▄    ▄██████▄     ▄████████    ▄████████         ▄████████ ███▄▄▄▄   ████████▄        ▄█          ▄████████    ▄████████    ▄████████ 
 ▄██▀▀▀███▀▀▀██▄ ███    ███   ███    ███   ███    ███        ███    ███ ███▀▀▀██▄ ███   ▀███      ███         ███    ███   ███    ███   ███    ███ 
 ███   ███   ███ ███    ███   ███    ███   ███    █▀         ███    ███ ███   ███ ███    ███      ███         ███    █▀    ███    █▀    ███    █▀  
 ███   ███   ███ ███    ███  ▄███▄▄▄▄██▀  ▄███▄▄▄            ███    ███ ███   ███ ███    ███      ███        ▄███▄▄▄       ███          ███        
 ███   ███   ███ ███    ███ ▀▀███▀▀▀▀▀   ▀▀███▀▀▀          ▀███████████ ███   ███ ███    ███      ███       ▀▀███▀▀▀     ▀███████████ ▀███████████ 
 ███   ███   ███ ███    ███ ▀███████████   ███    █▄         ███    ███ ███   ███ ███    ███      ███         ███    █▄           ███          ███ 
 ███   ███   ███ ███    ███   ███    ███   ███    ███        ███    ███ ███   ███ ███   ▄███      ███▌    ▄   ███    ███    ▄█    ███    ▄█    ███ 
  ▀█   ███   █▀   ▀██████▀    ███    ███   ██████████        ███    █▀   ▀█   █▀  ████████▀       █████▄▄██   ██████████  ▄████████▀   ▄████████▀  
                              ███    ███                                                          ▀                                                
   ▄████████  ▄██████▄   ▄█        ▄█        ▄██████▄   ▄█     █▄     ▄████████    ▄████████    ▄████████                                          
  ███    ███ ███    ███ ███       ███       ███    ███ ███     ███   ███    ███   ███    ███   ███    ███                                          
  ███    █▀  ███    ███ ███       ███       ███    ███ ███     ███   ███    █▀    ███    ███   ███    █▀                                           
 ▄███▄▄▄     ███    ███ ███       ███       ███    ███ ███     ███  ▄███▄▄▄      ▄███▄▄▄▄██▀   ███                                                 
▀▀███▀▀▀     ███    ███ ███       ███       ███    ███ ███     ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ▀███████████                                          
  ███        ███    ███ ███       ███       ███    ███ ███     ███   ███    █▄  ▀███████████          ███                                          
  ███        ███    ███ ███▌    ▄ ███▌    ▄ ███    ███ ███ ▄█▄ ███   ███    ███   ███    ███    ▄█    ███                                          
  ███         ▀██████▀  █████▄▄██ █████▄▄██  ▀██████▀   ▀███▀███▀    ██████████   ███    ███  ▄████████▀                                           
                        ▀         ▀                                               ███    ███              
'''
vs='''    
        ┬  ┬┌─┐
        └┐┌┘└─┐
         └┘ └─┘
'''
score=0
game_continue=True

def format_data(account):  # 출력
    name = account["name"]
    descr = account["description"]
    hometown = account["hometown"]
    return f"{name}, a {descr}, from {hometown}"


def answer(guess, a_follo, b_follo):
    """check the answer"""
    if a_follo > b_follo:
        return guess == "a"

    else:
        return guess == "b"

account_b=random.choice(data)

print(logo)
while game_continue:

    account_a=account_b
    account_b=random.choice(data)

    while account_a==account_b:
        account_b=random.choice(data)
    print(f"compare A:{format_data(account_a)}{vs}compare B:{format_data(account_b)}")

    guess=input("who have more followers? a or b ? :").lower()

    a_follo=account_a["follower_count"]
    b_follo=account_b["follower_count"]
    is_correct= answer(guess, a_follo, b_follo)

    if is_correct:
        score+=1
        print(f"correct! your score:{score}")
    else:
        game_continue=False
        print(f"incorrect your final score:{score}")
