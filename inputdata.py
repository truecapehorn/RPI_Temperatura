#!/usr/bin/env python
# -*- coding: utf-8 -*-


def wejscie(text):
    while 1:
        try:
            wej = float(input(text))
        except ValueError as error:
            print('\n Wystapił błąd ', error)
            continue
        break

    return wej
