from scripts.helpful_sctripts import multiply, menu, help, get_name


def alireza():
    while True:
        menu()
        choice = int(input("please enter your number: "))
        if choice == 1:
            get_name()
        elif choice == 2:
            multiply()
        elif choice == 3:
            help()
        elif choice == 4:
            break
        else:
            print("\nyour choice is out of menu choices range\nplease try again.\n")


def main():
    alireza()
