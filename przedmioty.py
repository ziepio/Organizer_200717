from abc import ABC, abstractmethod
import datetime

class Tool(ABC):

    today_date = datetime.datetime.now().date()

    def __init__(self, typ, date, priority):
        self.typ = typ
        self.date = date
        self.priority = priority

    @abstractmethod
    def __str__(self):
        pass


class Note(Tool):

    def __init__(self, priority, title, content):
        super().__init__('note', self.today_date, priority)
        self.title = title
        self.content = content

    def __str__(self):
        info = 'Date: ' + self.date + '\n'
        info += 'Priority: ' + self.priority + '\n'
        info += 'Title: ' + self.title + '\n'
        info += 'Content: ' + self.content + '\n'
        return info


class BusinessCard(Tool):

    def __init__(self, priority, name, surname, mobile):
        super().__init__('business_card', self.today_date, priority)
        self.name = name
        self.surname = surname
        self.mobile = mobile

    def __str__(self):
        info = 'Date: ' + self.date + '\n'
        info += 'Priority: ' + self.priority + '\n'
        info += 'Full name: ' + self.name + ' Surname: ' + self.surname + '\n'
        info += 'Mobile: ' + self.mobile + '\n'
        return info
        # return (self.date, self.priorytet, self.imie, self.nazwisko, self.telefon)


class DiscountCode(Tool):

    def __init__(self, priority, shop, discount, code):
        super().__init__('discount_code', self.today_date, priority)
        self.shop = shop
        self.discount = discount
        self.code = code

    def __str__(self):
        info = 'Date: ' + self.date + '\n'
        info += 'Priority: ' + self.priority + '\n'
        info += 'Shop: ' + self.shop + ', the amount of the discount: ' + self.discount + '\n'
        info += 'Code: ' + self.code + '\n'
        return info