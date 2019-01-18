#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import RPi.GPIO as GPIO
import path

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
temp_sensor = path.sensorPath

# ODCZYT PLIKU CZUJNIKA


def temp_raw():
    f = open(temp_sensor, 'r')
    lines = f.readlines()
    f.close()
    return lines


# OBSLUGA CZUJNIKA wyjscie w stC
def read_temp():
    lines = temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        print('Odczyt temperatury zakonczony niepowiodzeniem :( " + loc_time()')
        time.sleep(1)
        lines = temp_raw()
    temp_output = lines[1].find('t=')
    if temp_output != -1:
        temp_string = lines[1].strip()[temp_output + 2:]
    return float(temp_string) / 1000.0
