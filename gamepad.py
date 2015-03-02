# -*- coding: utf-8 -*-

import sys
import serial

gamepad = open('/dev/input/by-id/usb-0079_USB_Gamepad-event-joystick', 'r')
port = '/dev/ttyUSB0'
speed = 9600
connection = serial.Serial(port, speed)

byte = []

while True:
    for bit in gamepad.read(1):
        byte.append('%02X' % ord(bit))
        if len(byte) == 8:
            button = byte[2]
            if byte == ['01', '00', button, '01', '01', '00', '00', '00']:
                print 'Pressed Button 1'
                connection.write('1')
            elif byte == ['01', '00', button, '01', '00', '00', '00', '00']:
                print 'Released Button 1'
                connection.write('2')
            byte = []
