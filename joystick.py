# -*- coding: utf-8 -*-

import sys
import serial

joystick = open('/dev/input/by-id/usb-0079_USB_Gamepad-event-joystick', 'r')

action = []

while True:
    for character in joystick.read(1):
        action += ['%02X' % ord(character)]
        if len(action) == 8:
            print action
            action = []
