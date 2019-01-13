#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# script by Alex Eames http://RasPi.tv/
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# GPIO 23 установить как вход. И подтянуть чтобы отсечь ложныу срабатывания
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print “Убедитесь, что у вас есть кнопка, подключенная таким образом, что при нажатии”
print “она соеденит GPIO порт 23 (pin 16) с GND (pin 6)”
raw_input(“Нажмите Enter когда готовы”)

print “Ожидание падения фронта на порту 23”
# Теперь программа не будет делать ничего, пока сигнал на порту 23
# начнет падать к нулю. Именно поэтому мы использовали подтяжки
# держать сигнал высокого фронта и предотвратить ложное прерывание

print “В течение этого времени ожидания, ваш компьютер не”
print “тратит ресурсы путем опроса нажатия кнопки.”
print “Нажмите кнопку, когда вы готовы инициировать прерывание.”
try:
  GPIO.wait_for_edge(23, GPIO.FALLING)
  print “Падение фронта обнаружено. Теперь программа может продолжить”
  print “выполнять все что ожидало нажатия кнопки.”
except KeyboardInterrupt:
  GPIO.cleanup() # очистить GPIO при CTRL+C выходе
GPIO.cleanup() # очистить GPIO при нормальном выходе