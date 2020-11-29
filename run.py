from organizer import Organizer


my_organizer = Organizer('Piotr')

while True:

    print('''What would you like to do:

    1 - add note            |   4 - display note
    2 - add business card   |   5 - display business card
    3 - add discount code   |   6 - display discount code 
                0 - close organizer    
    ''')

    x = input()
    try:
        if x == '1':
            my_organizer.dodaj_notatke()
        if x == '2':
            my_organizer.dodaj_wizytowke()
        if x == '3':
            my_organizer.dodaj_kod_rabatowy()
        if x == '4':
            my_organizer.wyswietl_notatke()
        if x == '5':
            my_organizer.wyswietl_wizytowke()
        if x == '6':
            my_organizer.wyswietl_kod_rabatowy()
        if x == '0':
            break
    except:
        print('The selected option does not exist.\n')