import easygui as eg


#This is the beggining of the dictionary, this includes the Cards and their stats XD
Monster_Catalouge = {
    'Stoneling': {
        'Strength': 7.00,
        'Speed': 1.00,
        'Stealth': 25.00,
        'Cunning': 15.00
    },

    'Vexscream': {
        'Strength': 1.00,
        'Speed': 6.00,
        'Stealth': 21.00,
        'Cunning': 15.00
    },

    'Dawnmirage': {
        'Strength': 5.00,
        'Speed': 15.00,
        'Stealth': 18.00,
        'Cunning': 22.00
    }
}


#This is the main, every single action goes through this function. 
#If someone were to click the "Card List" function it would show all the cards list by calling the seperate "Card" function.
def main():
    choice = eg.buttonbox("Hello traveler, what would you like to do?", "Monster Card Catalogue", ["Cards list", "Exit"])
    if choice == 'Show list':
        display_catalogue()
    elif choice == 'Exit':
        exit_handler()
#This is the exit handler, giving the user an option to see if they actually want to quit the program with a confirmation.
#This makes sure the user doesn't accidentally quit and lose their progress.
def exit_handler():
    choice = eg.buttonbox("Are you sure you want to quit?", "Confirmation", ["Exit", "Return"])
    if choice == 'Exit':
        exit()
    elif choice == 'Return':
        return main()
    
def display_catalogue():
    message = "Catalogue\n"
    for cards, items in Monster_Catalouge.items():
        message += f"{cards}: {items}"
    eg.msgbox(message, "Menu")

main()