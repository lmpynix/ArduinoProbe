# -*- coding: utf-8 -*-

from __future__ import print_function
from pyfirmata import Arduino as ard
from pyfirmata import util
import threading
import os
import _thread
import time

VERSION = "0.0.1"

probeaddrs = []
probes = []
pin13led = True


def init():
    probeaddrs.insert(0, input('Enter the address of the probe with ID 0: '))
    print('Attempting to connect to probe on ', probeaddrs[0], '...')
    try:
        probes.insert(0, ard(probeaddrs[0]))
    except:
        print('Connection Failed.')
        return 1
    print('Connection Succeeded.  Device with ID 0 is connected.')
    blinks(0, 'confirm')
    return 0


def main():
    print('LPyKit ArduinoProbe version ', VERSION)
    init()


def led(probeid, state):
    if pin13led:
        try:
            probes[probeid].digital[13].write(state)
        except:
            print('Writing to LED failed.')
            raise
    else:
        print('Pin 13 is not enabled as an LED.')


def blinks(probeid, blinktype):
    if blinktype == 'confirm':
        led(probeid, 1)
        time.sleep(0.5)
        led(probeid, 0)
        time.sleep(0.5)
        led(probeid, 1)
        time.sleep(0.25)
        led(probeid, 0)
        time.sleep(0.25)
    elif blinktype == 'failure':
        led(probeid, 1)
        time.sleep(0.25)
        led(probeid, 0)
        time.sleep(0.25)
        led(probeid, 1)
        time.sleep(0.25)
        led(probeid, 0)
        time.sleep(0.25)
        led(probeid, 1)
        time.sleep(0.25)
        led(probeid, 0)
        time.sleep(0.25)
        led(probeid, 1)
        time.sleep(0.25)
        led(probeid, 0)
        time.sleep(0.25)


if __name__ == '__main__':
    main()