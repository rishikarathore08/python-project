#Text based adventure_game
import time

def game_start():
    print("Welcome to the Dungeon adventure!")
    time.sleep(1)
    print("You find yourself standing at the entrance of a dark dungeon.")
    time.sleep(1)
    print("Your objective is to find the treasure hidden deep within. ")
    time.sleep(1)
    print("Let's begin!\n")
    time.sleep(1)
    choose_path()

def choose_path():
        print("You are at a crossroads. what path will you take?")
        print("1.Go left")
        print("2.Go right")
        print("3.Straight")
        choice +input("Enter your choice(1/2/3):")

        if choice == '1':
           go_left()
        elif choice == '2':
           go_right()
        elif choice == '3':
           go_straight()
        else: 
            print("Invalid choice. Please enter 1,2,or 3,")
            choose_path()

def go_left():
    print("\nyou choose to go left.")
    time.sleep(1)
    print("You encounter a monster!")
    time.sleep(1)
    print("fight or run?")
    choice = input("Enter 'fight' or 'run':")

    if choice.lower() == 'fight':
        print("\nYou bravely fight the moster and defeat it!")
        time.sleep(1)
        print("You continue deeper into the dungeon.")
        time.sleep(1)
        choose_path()
    elif choice.lower() == 'run':
        print("\nYou run away from the monster.")
        time.sleep(1)
        print("You go back to the crossroads.")
        time.sleep(1)
        choose_path()
    else:
        print("Invalid choice. Please ente 'fight' or 'run'.")
        go_left()

        def go_right():
            print("\nYou choose to go right.")
            time.sleep(1)
            print("You find a locked door.")
            time.sleep(1)
            print("Search for key or return?")
            choice = input("Enter 'search' or 'return': ")

            if choice.lower() == 'search':
                print("\nYou search around and find the key!")
                time.sleep(1)
                choose_path()
                time.sleep(1)
                choose_path()
            elif choice.lower() == 'return':
                print("\nYou return to the crossroads.")
                time.sleep(1)
                choose_path()
            else:
                print("Invalid choice. Please enter 'search' or 'return'.")
                go_right()

def go_straight():
    print("\nYou choose to go straight.")
    time.sleep(1)
    print("You discover a treaure chest!")
    time.sleep(1)
    print("you found the treasure! You win!")
    play_agin()

def play_again():
    print("\nYou choose to go straight.")
    choice = input("Enter 'yes'or 'no':")

    if choice.lower() == 'yes':
        game_start()
    elif choice.lower() == 'no':
        print("Thank you for playing!")
    else:
        print("Invalid choice.please enter 'yes' or 'no'.")
        play_again()

    if __name__=="__main__":
        game_start()



