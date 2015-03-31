# -*- coding: utf-8 -*-

from pyfirmata import Arduino as ard
from pyfirmata import util
import thread, os, time
VERSION = "0.0.1"

probeaddrs = []
probes = []

def init():
    probeaddrs.insert(0, raw_input("Enter the address of the probe with ID 0: "))
    print("Attempting to connect to probe on ", probeaddrs[0], "...")
    try:
        probes.insert(0, ard(probeaddrs[0]))
    except:
        print("Connection Failed.")
        return 1
    print("Connection Succeeded.  Device with ID 0 is connected.")
    return 0
    
def main():
    print("LPyKit ArduinoProbe version ", VERSION)
    init()

def blink(board, time):
    probes[board].digital[13].write(1)
    time.sleep(time)
    probes[board].digital[13].write(0)
    time.sleep(time)

if __name__ == "__main__":
    main()