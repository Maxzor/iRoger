# -*- coding: utf-8 -*-
import serial
import time
import RPi.GPIO as GPIO

def deal(duration):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)
    port=serial.Serial("/dev/ttyAMA0", baudrate=1000000, timeout=3.0)

    #passage en mode rotation continue
    GPIO.output(18, GPIO.HIGH)
    port.write(bytearray.fromhex("FF FF FD 00 01 06 00 03 08 00 01 47 63"))
    time.sleep(0.002)
    GPIO.output(18, GPIO.LOW)
    time.sleep(0.01)

    #écriture de la vitesse de rotation
    GPIO.output(18,GPIO.HIGH)
    #port.write(bytearray.fromhex("FF FF FD 00 01 07 00 03 20 00 90 01 5A 3D"))
    port.write(bytearray.fromhex("FF FF FD 00 01 07 00 03 20 00 C8 04 42 ED"))
    time.sleep(0.002)
    GPIO.output(18, GPIO.LOW)

    #allumage de la LED d'éclairage
    GPIO.output(25,GPIO.HIGH)

    #laisser tourner pendant la durée passée en paramètre
    time.sleep(duration)

    #éteindre la LED d'éclairage
    GPIO.output(25,GPIO.LOW)

    #arrêter la rotation
    GPIO.output(18,GPIO.HIGH)
    #port.write(bytearray.fromhex("FF FF FD 00 01 07 00 03 20 00 00 00 55 DD"))
    port.write(bytearray.fromhex("FF FF FD 00 01 07 00 03 20 00 00 04 4E 5D"))
    time.sleep(0.002)
    GPIO.output(18, GPIO.LOW)

    time.sleep(1)

    #rarrêter la rotation
    GPIO.output(18,GPIO.HIGH)
    #port.write(bytearray.fromhex("FF FF FD 00 01 07 00 03 20 00 00 00 55 DD"))
    port.write(bytearray.fromhex("FF FF FD 00 01 07 00 03 20 00 00 04 4E 5D"))
    time.sleep(0.002)
    GPIO.output(18, GPIO.LOW)
    GPIO.setwarnings(True)
