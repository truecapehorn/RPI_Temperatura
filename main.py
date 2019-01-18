#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import path
from inputdata import *
from sensor import read_temp
from loctime import *
import time
import settings
import relay
import log
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# warunki zadane
print('\t!!!Program start !!! \n')
run = 1
log_no = 1
histereza = 0
pin = 17
temp_zad1 = wejscie('Podaj dolną temperaturę zadaną : ')
temp_zad2 = wejscie('Podaj górną temperaturę zadaną : ')
time_sleep = wejscie('Podaj czas między pomiarami : ')
print('Tmp dolna = {0} [stC], Tmp górna = {1} [stC], Czas = {2}'.format(
    temp_zad1, temp_zad2, time_sleep))
print('log - ', path.logPath, '\n')
# ZAPIS NASTAW DO PLIKU
settings.settingsWrite(temp_zad1, temp_zad2, histereza, time_sleep, run)
# PĘTLA GŁÓWNA
while run:  # jezeli 0 to stop
    set = settings.settingsRead()  # ODCZYT NASTAW Z PLIKU
    temp_zad1_F = set[0]
    temp_zad2_F = set[1]
    histereza_F = set[2]
    time_sleep_F = set[3]
    run = set[4]
    temperatura = read_temp()  # ODCZYT SENSORA
    local_time = loc_time()  # ODCZYT DATY
    data = local_time[1]
    godzina = local_time[2]
    relayMesage = relay.relay(pin, temperatura, temp_zad1_F, histereza_F)  # WYSTEROWANIE WYJSCIA
    # WYDRUK POMIARU
    if temperatura > temp_zad1_F and temperatura < temp_zad2_F:
        color = '\x1b[1;32;40m'
        message = ' ' + relayMesage
    else:
        color = '\x1b[1;31;40m'
        if temperatura < temp_zad1_F:
            message = '!!! Temp. poniżej dolnej granicy !!! ' + relayMesage

        elif temperatura > temp_zad2_F:
            message = '!!! Temp. powyzej górnej granicy !!! ' + relayMesage

    print(godzina + ' ' + color + str(temperatura) + '°C ' + message + '\x1b[0m')

    # ZAPIS POMIARU
    log_no = log.logWrite(data, godzina, temperatura, temp_zad1_F, relayMesage, log_no)
    time.sleep(time_sleep_F)
GPIO.cleanup()
print('\t!!! Koniec programu !!! \n')
