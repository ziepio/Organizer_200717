from organizer import Organizer

my_organizer = Organizer('Piotr')

while True:

    print('''What would you like to do:

        Note:        Business card:    Discount code:
    1 - add       |   4 - add       |   7 - add
    2 - display   |   5 - display   |   8 - display
    3 - delete    |   6 - delete    |   9 - delete  
                  0 - close organizer    
    ''')

    x = input()
    try:
        if x == '1':
            my_organizer.add_note()
        if x == '2':
            my_organizer.display_notes()
        if x == '3':
            my_organizer.detele_note()
        if x == '4':
            my_organizer.add_business_card()
        if x == '5':
            my_organizer.display_business_cards()
        if x == '6':
            my_organizer.delete_business_card()
        if x == '7':
            my_organizer.add_discount_code()
        if x == '8':
            my_organizer.display_discount_code()
        if x == '9':
            my_organizer.delete_discount_code()
        if x == '0':
            break
    except AttributeError as error:
        print(error)
    print('')
