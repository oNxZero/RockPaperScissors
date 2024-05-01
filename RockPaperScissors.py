import random
import time
from colorama import Fore

player_score = 0
boss_score = 0
SL = '------------------------------------------------------------'


print("""
 .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| |  _______     | || |   ______     | || |    _______   | |
| | |_   __ \    | || |  |_   __ \   | || |   /  ___  |  | |
| |   | |__) |   | || |    | |__) |  | || |  |  (__ \_|  | |
| |   |  __ /    | || |    |  ___/   | || |   '.___`-.   | |
| |  _| |  \ \_  | || |   _| |_      | || |  |`\____) |  | |
| | |____| |___| | || |  |_____|     | || |  |_______.'  | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'                                                                                                                            
""")
time.sleep(0.5)
print(SL)
print("Boss: Dare To Play RPS?")

while True:
    Want_Play = input("Answer 'Y'es or 'N'o : ").upper()
    if Want_Play == 'Y':
        print(SL)
        print("Boss: Let The Game Begin!")
        print(SL)
        time.sleep(0.5)
        break  # exit loop
    elif Want_Play == 'N':
        time.sleep(0.5)
        print(SL)
        print("Boss: Run Away Then, Coward!")
        print(SL)
        exit()  # exit the entire program
    else:
        print(SL)
        print("Boss: Invalid Input")
        print(SL)

while True:
    if Want_Play == 'Y':
        weapon_names = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

        while True:
            print(f"Your Score {player_score} | {boss_score} Boss Score")
            print(SL)
            time.sleep(0.5)
            print("Boss: What Do You Choose?")
            player_weapon = input("Boss: 'R'ock, 'P'aper or 'S'cissors?: ").upper()
            if player_weapon in ('R', 'P', 'S'):
                choices = ['R', 'P', 'S']
                computer_weapon = random.choice(choices)

                time.sleep(0.5)
                print(SL)
                print(f"Boss: You Chose {weapon_names[player_weapon]} and I Chose {weapon_names[computer_weapon]}")
                print(SL)

                if player_weapon == computer_weapon:
                    time.sleep(0.5)
                    print("RPS: Its A Tie!")
                elif (
                    (player_weapon == 'R' and computer_weapon == 'S') or
                    (player_weapon == 'P' and computer_weapon == 'R') or
                    (player_weapon == 'S' and computer_weapon == 'P')
                ):
                    player_score += 1
                    time.sleep(0.5)
                    print(Fore.GREEN + "RPS : Player Wins!" + Fore.RESET)
                else:
                    boss_score += 1
                    time.sleep(0.5)
                    print(Fore.RED + "RPS : Boss Wins!" + Fore.RESET)
                break
            else:
                time.sleep(0.5)
                print (SL)
                print("Boss: Invalid Input")
                print (SL)

    time.sleep(0.5)
    print (SL)
    print(f"Boss: Your Score: {player_score} | Boss Score: {boss_score}")
    time.sleep(0.5)
    print (SL)
    print("Boss: Do You Want To Play Again?")
    print (SL)
    time.sleep(0.5)
    Want_Play_Again = input("Answer 'Y'es or 'N'o : ").upper()

    if Want_Play_Again == 'Y':
        print (SL)
    else:
        if Want_Play_Again == 'N':
            time.sleep(0.5)
            print (SL)
            print("Boss: We Shall Meet Again!")
            exit()  # exit the entire program
        else:
            time.sleep(0.5)
            print (SL)
            print("Boss: Invalid Input")
