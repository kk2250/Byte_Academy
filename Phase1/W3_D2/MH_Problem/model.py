import random
import os
import time
import view

def monty_h(door_num):
    os.system('clear')
    n = random.randrange(1,4)
    if door_num == 1:
        print('You chose door number 1')
        time.sleep(1)
        if n == 3:
            print('Open door number 2, there is a goat!')
            time.sleep(1)
            print('Would you like to switch door number 1 to door number 3?')
            time.sleep(1)
            answer = input('[Y]/[N]\n')
            view.prize(answer)
            os.system('clear')
            if answer.lower() == 'y':
                print('\n\nYou win the prize!! Brand New Car!!')
                time.sleep(2)
            elif answer.lower() == 'n':
                print('\n\nYou lose the prize.. sorry...')
                time.sleep(2)

        elif n == 2:
            print('Open door number 3, there is a goat!')
            time.sleep(1)
            print('Would you like to switch door number 1 to door number 2?')
            time.sleep(1)
            answer = input('[Y]/[N]\n')
            view.prize(answer)
            os.system('clear')
            if answer.lower() == 'y':
                print('\n\nYou win the prize!! Brand New Car!!')
                time.sleep(2)
            elif answer.lower() == 'n':
                print('\n\nYou lose the prize.. sorry...')
                time.sleep(2)


        elif n == 1:
            nm = random.randrange(1,3)
            if nm == 1:
                print('Open door number 3, there is a goat!')
                time.sleep(1)
                print('Would you like to switch door number 1 to door number 2?')
                time.sleep(1)
                answer = input('[Y]/[N]\n')
                view.prize(answer)
                os.system('clear')
                if answer.lower() == 'n':
                    print('\n\nYou win the prize!! Brand New Car!!')
                    time.sleep(2)
                elif answer.lower() == 'y':
                    print('\n\nYou lose the prize.. sorry...')
                    time.sleep(2)
            elif nm == 2:
                print('Open door number 2, there is a goat!')
                time.sleep(1)
                print('Would you like to switch door number 1 to door number 3?')
                time.sleep(1)
                answer = input('[Y]/[N]\n')
                view.prize(answer)
                os.system('clear')
                if answer.lower() == 'n':
                    print('\n\nYou win the prize!! Brand New Car!!')
                    time.sleep(2)
                elif answer.lower() == 'y':
                    print('\n\nYou lose the prize.. sorry...')
                    time.sleep(2)


    elif door_num == 2:
        print('You chose door number 2')
        time.sleep(1)
        if n == 3:
            print('Open door number 1, there is a goat!')
            time.sleep(1)
            print('Would you like to switch door number 2 to door number 3?')
            time.sleep(1)
            answer = input('[Y]/[N]\n')
            view.prize(answer)
            os.system('clear')
            if answer.lower() == 'y':
                print('\n\nYou win the prize!! Brand New Car!!')
                time.sleep(2)
            elif answer.lower() == 'n':
                print('\n\nYou lose the prize.. sorry...')
                time.sleep(2)

        elif n == 2:
            nm = random.randrange(1,3)
            if nm == 1:
                print('Open door number 3, there is a goat!')
                time.sleep(1)
                print('Would you like to switch door number 2 to door number 1?')
                time.sleep(1)
                answer = input('[Y]/[N]\n')
                view.prize(answer)
                os.system('clear')
                if answer.lower() == 'n':
                    print('\n\nYou win the prize!! Brand New Car!!')
                    time.sleep(2)
                elif answer.lower() == 'y':
                    print('\n\nYou lose the prize.. sorry...')
                    time.sleep(2)
            elif nm == 2:
                print('Open door number 1, there is a goat!')
                time.sleep(1)
                print('Would you like to switch door number 2 to door number 3?')
                time.sleep(1)
                answer = input('[Y]/[N]\n')
                view.prize(answer)
                os.system('clear')
                if answer.lower() == 'n':
                    print('\n\nYou win the prize!! Brand New Car!!')
                    time.sleep(2)
                elif answer.lower() == 'y':
                    print('\n\nYou lose the prize.. sorry...')
                    time.sleep(2)

        elif n == 1:
            print('Open door number 3, there is a goat!')
            time.sleep(1)
            print('Would you like to switch door number 2 to door number 1?')
            time.sleep(1)
            answer = input('[Y]/[N]\n')
            view.prize(answer)
            os.system('clear')
            if answer.lower() == 'y':
                print('\n\nYou win the prize!! Brand New Car!!')
                time.sleep(2)
            elif answer.lower() == 'n':
                print('\n\nYou lose the prize.. sorry...')
                time.sleep(2)


    elif door_num == 3:
        print('You chose door number 3')
        time.sleep(1)
        if n == 3:
            nm = random.randrange(1,3)
            if nm == 1:
                print('Open door number 2, there is a goat!')
                time.sleep(1)
                print('Would you like to switch door number 3 to door number 1?')
                time.sleep(1)
                answer = input('[Y]/[N]\n')
                view.prize(answer)
                os.system('clear')
                if answer.lower() == 'n':
                    print('\n\nYou win the prize!! Brand New Car!!')
                    time.sleep(2)
                elif answer.lower() == 'y':
                    print('\n\nYou lose the prize.. sorry...')
                    time.sleep(2)
            elif nm == 2 :
                print('Open door number 1, there is a goat!')
                time.sleep(1)
                print('Would you like to switch door number 3 to door number 2?')
                time.sleep(1)
                answer = input('[Y]/[N]\n')
                view.prize(answer)
                os.system('clear')
                if answer.lower() == 'n':
                    print('\n\nYou win the prize!! Brand New Car!!')
                    time.sleep(2)
                elif answer.lower() == 'y':
                    print('\n\nYou lose the prize.. sorry...')
                    time.sleep(2)

        elif n == 2:
            print('Open door number 1, there is a goat!')
            time.sleep(1)
            print('Would you like to switch door number 3 to door number 2?')
            time.sleep(1)
            answer = input('[Y]/[N]\n')
            view.prize(answer)
            os.system('clear')
            if answer.lower() == 'y':
                print('\n\nYou win the prize!! Brand New Car!!')
                time.sleep(2)
            elif answer.lower() == 'n':
                print('\n\nYou lose the prize.. sorry...')
                time.sleep(2)

        elif n == 1:
            print('Open door number 2, there is a goat!')
            time.sleep(1)
            print('Would you like to switch door number 3 to door number 1?')
            time.sleep(1)
            answer = input('[Y]/[N]\n')
            view.prize(answer)
            os.system('clear')
            if answer.lower() == 'y':
                print('\n\nYou win the prize!! Brand New Car!!')
                time.sleep(2)
            elif answer.lower() == 'n':
                print('\n\nYou lose the prize.. sorry...')
                time.sleep(2)

