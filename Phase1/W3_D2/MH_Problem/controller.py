import model
import view
import os
import time

while True:
    os.system('clear')
    choice = view.main_menu()
    if choice.lower() == 'y':
        view.choose_door()
        door_num = int(input('Choose the door by number [1]or[2]or[3]\n'))
        model.monty_h(door_num)
        time.sleep(2)
        os.system('clear')
        break

    elif choice.lower() == 'n':
        print("\nExiting...")
        time.sleep(2)
        os.system('clear')
        print('BYE~!')
        time.sleep(2)
        os.system('clear')
        break
