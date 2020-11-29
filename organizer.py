from przedmioty import Notatka, Wizytowka, KuponRabatowy
from db_mysql import MySQLdb


class Organizer(object):
    __wlasciciel = ''
    # __baza_danych = []

    def __init__(self, wlasciciel):
        self.wlasciciel = wlasciciel

    def dodaj_notatke(self):
        priorytet = input('Priorytet: ')
        tytul = input('Tytuł: ')
        tresc = input('Tresc: ')

        nowa_notatka = Notatka(priorytet, tytul, tresc)
        # self.__baza_danych.append(nowa_notatka)
        MySQLdb.connect_to_db(self.__wlasciciel)
        MySQLdb.insert_into_db(nowa_notatka.typ, nowa_notatka)


    def wyswietl_notatke(self):
        print('Lista notatek: ')
        for i in self.__baza_danych:
            if i.typ == 'notatka':
                print(i)

    def dodaj_wizytowke(self):
        priorytet = input('Priorytet: ')
        imie = input('Imie: ')
        nazwisko = input('Nazwisko: ')
        telefon = input('Telefon: ')

        nowa_wizytowka = Wizytowka(priorytet, imie, nazwisko, telefon)
        self.__baza_danych.append(nowa_wizytowka)

    def wyswietl_wizytowke(self):
        print('Lista wizytówek: ')
        for i in self.__baza_danych:
            if i.typ == 'wizytowka':
                print(i)

    def dodaj_kod_rabatowy(self):
        sklep = input('Nazwa sklepu: ')
        rabat = input('Wysokość rabatu: ')
        kod = input('Kod: ')
        priorytet = input('Priorytet: ')

        nowy_rabat = KuponRabatowy(priorytet, sklep, rabat, kod)
        self.__baza_danych.append(nowy_rabat)

    def wyswietl_kod_rabatowy(self):
        print('Lista kodów rabatowych: ')

        for i in self.__baza_danych:
            if i.typ == 'kupon rabatowy':
                print(i)

    def usun_notatke(self):
        usun = input('Podaj notatkę do usunięcia: ')
        for i in self.__baza_danych:
            if i.typ == 'notatka' and i.sklep == usun:
                self.__baza_danych.remove(i)

    def usun_wizytowke(self):
        usun = input('Podaj wizytówkę do usunięcia: ')
        for i in self.__baza_danych:
            if i.typ == 'wizytowka' and i.sklep == usun:
                self.__baza_danych.remove(i)

    def usun_kod_rabatowy(self):
        usun = input('Podaj nazwę sklepu do którego chcesz usunąć kod rabatowy: ')
        for i in self.__baza_danych:
            if i.typ == 'kupon rabatowy' and i.sklep == usun:
                self.__baza_danych.remove(i)