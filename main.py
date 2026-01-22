from dice import DieHandler, Dice

dice = Dice()
die_handler = DieHandler()


def show_dice():
    show = die_handler.__str__()
    return print(show)

def play_game():
    checking = True
    while checking is True:
        try:
            show_dice()
            print("ex: for die #1 type '1'")
            keep_ans = int(input("Type '0' to continue rolling\nKeep or Un-Keep Which Die?: "))

        except:
            print("Use Numbers 1-5")
        else:
            if keep_ans == 0:
                checking = False

            elif 5 >= keep_ans > 0:
                die_handler.check_dice(keep_ans)

            else:
                print("type the number of the die, ex: Die #1 type '1'")

def menu():
    print(" ______  _________ _______  _______          \n"
          "(  __  \ \__   __/(  ____ \(  ____ \         \n"
          "| (  \  )   ) (   | (    \/| (    \/         \n"
          "| |   ) |   | |   | |      | (__             \n""| |   | |   | |   | |      |  __)            \n""| |   ) "
          "|   | |   | |      | (               \n""| (__/  )___) (___| (____/\| (____/\         \n""(______/ "
          "\_______/(_______/(_______/         \n"" _______  _______  _        _______  _______\n""(  ____ )(  ___  "
          ")| \    /\(  ____ \(  ____ )\n""| (    )|| (   ) ||  \  / /| (    \/| (    )|\n""| (____)|| |   | ||  (_/ "
          "/ | (__    | (____)|\n""|  _____)| |   | ||   _ (  |  __)   |     __)\n""| (      | |   | ||  ( \ \ | (    "
          "  | (\ (   \n""| )      | (___) ||  /  \ \| (____/\| ) \ \__\n""|/       (_______)|_/    \/(_______/|/   "
          "\__/\n")
    start = True
    while start is True:
        print("1.Start \n"
              "2.Exit")
        answer = input("Answer:")
        if answer.isnumeric() == 1:
            play_game()
            start = False
        elif answer.isnumeric() == 2:
            exit()

        else:
            print("/!\ Invalid Input, Use 1 or 2 to pick your desired option.")


menu()
