import time


def loc_time():
    localtime = time.strftime("%d.%m.%Y %H:%M:%S")
    znacznik = time.strftime("%d%m%Y_%H_%M")
    data = time.strftime("%d-%m-%Y")
    godzina = time.strftime("%H:%M:%S")
    return localtime, data, godzina, znacznik
