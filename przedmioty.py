from abc import ABC, abstractmethod


class Przedmiot(ABC):

    def __init__(self, typ, priorytet):
        self.typ = typ
        self.priorytet = priorytet

    @abstractmethod
    def __str__(self):
        pass


class Notatka(Przedmiot):

    def __init__(self, priorytet, tytul, tresc):
        super().__init__('notatka', priorytet)
        self.tytul = tytul
        self.tresc = tresc

    def __str__(self):  # funkcja odpowiada za print() na instancji
        info = 'Priorytet: ' + self.priorytet + '\n'
        info += 'Tytuł: ' + self.tytul + '\n'
        info += 'Treść: ' + self.tresc + '\n'
        return info


class Wizytowka(Przedmiot):

    def __init__(self, priorytet, imie, nazwisko, telefon):
        super().__init__('wizytowka', priorytet)
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon

    def __str__(self):
        info = 'Priorytet: ' + self.priorytet + '\n'
        info += 'Imię: ' + self.imie + ' Nazwisko: ' + self.nazwisko + '\n'
        info += 'Telefon: ' + self.telefon + '\n'
        return info


class KuponRabatowy(Przedmiot):

    def __init__(self, priorytet, sklep, rabat, kod):
        super().__init__('kupon rabatowy', priorytet)
        self.sklep = sklep
        self.rabat = rabat
        self.kod = kod

    def __str__(self):
        info = 'Priorytet: ' + self.priorytet + '\n'
        info += 'Sklep: ' + self.sklep + ', wysokość rabatu: ' + self.rabat + '\n'
        info += 'Kod rabatowy: ' + self.kod + '\n'
        return info
