# -*- coding: utf-8 -*-
# !/usr/bin/python3


def wejscia():
    print('\nPodaj warunki wejsciowe: \n')

    while True:
        try:
            temp_zad = float(input("\nPodaj temperaturę maksymalną: "))
        except ValueError as error:
            print('\n Wystapil blad ', error)
            continue
        break
    while True:
        try:
            t = float(input("Podaj odstęp pomiędzy pomiarami: "))
        except ValueError as error:
            print('\n Wystapil blad ', error)
            continue
        break
    print('Temp zad = {} [stC],Czas = {} [s]'.format(temp_zad, t))

    return temp_zad, t
