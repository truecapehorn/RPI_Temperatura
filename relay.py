import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


# OBSLUGA DIODY
def relay(pin, temperatura, temp_zad, histereza):
    GPIO.setup(pin, GPIO.OUT)
    func = GPIO.input(pin)

    if temperatura < temp_zad:
        GPIO.output(pin, GPIO.HIGH)
        praca = 1
    if func == 1 and temperatura > temp_zad + histereza:
        GPIO.output(pin, GPIO.LOW)
        praca = 0

    if func == 1:
        relayMesage = 'Przekaznik pracuje'
    else:
        relayMesage = 'Brak pracy przekaznika'

    #print(func, histereza, temp_zad, relayMesage)
    return relayMesage
