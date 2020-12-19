from przedmioty import Note, BusinessCard, DiscountCode
from db_mysql import MySQLdb


class Organizer(object):

    database = MySQLdb()

    def __init__(self, owner):
        self.owner = owner
        self.database.connect_to_db(self.owner)
        self.database.create_tables()

    def add_note(self, title, content):
        new_note = Note(title, content)
        self.database.insert_note_into_db(new_note.__dict__)

    def display_notes(self):
        print('Your notes:')
        notes = MySQLdb().extract_note_from_db()
        for (id, date, time, title, content) in notes:
            print(f'{id}| {date} | {time} | {title} | {content}')

    def delete_note(self):
        to_be_deleted = input('Which id number?: ')
        self.database.delete_note_from_db((to_be_deleted,))
        print(f'Note with id {to_be_deleted} removed')

    def add_business_card(self):
        name = input('Name: ')
        surname = input('Surname: ')
        mobile = input('Mobile: ')

        print('Adding new business card: ', end='')
        new_business_card = BusinessCard(name, surname, mobile)
        data = ('', '', new_business_card.name, new_business_card.surname, new_business_card.mobile)
        self.database.inser_business_card_into_db(data)
        print('done')

    def display_business_cards(self):
        print('Your business cards:')
        bcs = self.database.extract_business_card_from_db()
        for (id, date, time, name, surname, mobile) in bcs:
            print(f'{id} | {date} | {time} | {name} | {surname} | {mobile}')

    def delete_business_card(self):
        to_be_deleted = input('Which id number?: ')
        self.database.delete_business_card_from_db((to_be_deleted,))
        print(f'Business card with id {to_be_deleted} removed')

    def add_discount_code(self):
        shop = input('Shop name: ')
        discount = input('Discount amount: ')
        code = input('Code: ')

        new_discount = DiscountCode(shop, discount, code)
        data = ('', '', new_discount.shop, new_discount.discount, new_discount.code)
        self.database.insert_discount_code_into_db(data)

    def display_discount_code(self):
        print('Your discount codes: ')
        dcs = self.database.extract_discount_code_from_db()
        for (id, date, time, shop, discount, code) in dcs:
            print(f'{id} | {date} | {time} | {shop} | {discount} | {code}')

    def delete_discount_code(self):
        to_be_deleted = input('Which id number?: ')
        self.database.delete_discount_code_from_db((to_be_deleted,))
        print(f'Discount code with id {to_be_deleted} removed')
