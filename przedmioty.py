from abc import ABC, abstractmethod


class Tool(ABC):

    def __init__(self, typ):
        self.typ = typ

    @abstractmethod
    def __str__(self):
        pass


class Note(Tool):

    def __init__(self, title, content):
        super().__init__('note')
        self.title = title
        self.content = content

    def __str__(self):
        info = 'Title: ' + self.title + '\n'
        info += 'Content: ' + self.content + '\n'
        return info


class BusinessCard(Tool):

    def __init__(self, name, surname, mobile):
        super().__init__('business_card')
        self.name = name
        self.surname = surname
        self.mobile = mobile

    def __str__(self):
        info = 'Full name: ' + self.name + ' Surname: ' + self.surname + '\n'
        info += 'Mobile: ' + self.mobile + '\n'
        return info


class DiscountCode(Tool):

    def __init__(self, shop, discount, code):
        super().__init__('discount_code')
        self.shop = shop
        self.discount = discount
        self.code = code

    def __str__(self):
        info = 'Shop: ' + self.shop + ', the amount of the discount: ' + self.discount + '\n'
        info += 'Code: ' + self.code + '\n'
        return info
