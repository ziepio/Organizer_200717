from abc import ABC, abstractmethod


class Przedmiot(ABC):

    def __init__(self, typ, date, priorytet):
        self.typ = typ
        self.date = date
        self.priorytet = priorytet

    @abstractmethod
    def __str__(self):
        pass


class Notatka(Przedmiot):

    def __init__(self, date, priorytet, tytul, tresc):
        super().__init__('notatka', date, priorytet)
        self.tytul = tytul
        self.tresc = tresc

    def __str__(self):  # funkcja odpowiada za print() na instancji
        info = 'Date: ' + self.date + '\n'
        info += 'Priorytet: ' + self.priorytet + '\n'
        info += 'Tytuł: ' + self.tytul + '\n'
        info += 'Treść: ' + self.tresc + '\n'
        return info


class Wizytowka(Przedmiot):

    def __init__(self, date, priorytet, imie, nazwisko, telefon):
        super().__init__('wizytowka', date, priorytet)
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon

    def __str__(self):
        info = 'Date: ' + self.date + '\n'
        info += 'Priorytet: ' + self.priorytet + '\n'
        info += 'Imię: ' + self.imie + ' Nazwisko: ' + self.nazwisko + '\n'
        info += 'Telefon: ' + self.telefon + '\n'
        return info


class KuponRabatowy(Przedmiot):

    def __init__(self, date, priorytet, sklep, rabat, kod):
        super().__init__('kupon rabatowy', date, priorytet)
        self.sklep = sklep
        self.rabat = rabat
        self.kod = kod

    def __str__(self):
        info = 'Date: ' + self.date + '\n'
        info += 'Priorytet: ' + self.priorytet + '\n'
        info += 'Sklep: ' + self.sklep + ', wysokość rabatu: ' + self.rabat + '\n'
        info += 'Kod rabatowy: ' + self.kod + '\n'
        return info
