#!/usr/bin/env python

import colorsys
import math
import time
from subprocess import PIPE, run
import ledshim
import logging
import json
import calendar
import time

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='./battery.log', level=logging.DEBUG)
ledshim.set_clear_on_exit()

hue_range = 120
hue_start = 0
max_brightness = 0.8
max_battery = 345 #365
min_battery = 295

def show_graph(v, r, g, b):
    v *= ledshim.NUM_PIXELS
    for x in range(ledshim.NUM_PIXELS):
        hue = ((hue_start + ((x / float(ledshim.NUM_PIXELS)) * hue_range)) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
        if v < 0:
            brightness = 0
        else:
            brightness = min(v, 1.0) * max_brightness

        ledshim.set_pixel(x, r, g, b, brightness)
        v -= 1

    ledshim.show()


ledshim.set_brightness(0.3)

try:
    while True:
        vbatstr = run(['/usr/local/bin/lifepo4wered-cli', 'get', 'VBAT'], stdout=PIPE, stderr=PIPE, universal_newlines=True)
        ioutstr = run(['/usr/local/bin/lifepo4wered-cli', 'get', 'IOUT'], stdout=PIPE, stderr=PIPE, universal_newlines=True)
        tempstr = run(['/usr/bin/vcgencmd', 'measure_temp'], stdout=PIPE, stderr=PIPE, universal_newlines=True)
        uptimestr = run(['uptime', '-p'], stdout=PIPE, stderr=PIPE, universal_newlines=True)

        vbat = int(vbatstr.stdout)
        iout = int(ioutstr.stdout)
        temp = int(float(tempstr.stdout.replace("temp=", "").replace("'C", "").replace("\n","")))
        uptime = uptimestr.stdout.replace("up ", "").replace("\n","")

        if ((vbat/10) > max_battery):
            vbat = max_battery*10

        batt = (((vbat/10)-min_battery)/(max_battery-min_battery))
        logging.info('Battery: %s', round(batt*100, 2))

        gmt = time.gmtime()
        ts = calendar.timegm(gmt)

        data = {
            "updated": ts,
            "battery": round(batt*100, 2),
            "vbat": vbat,
            "load": iout,
            "uptime": uptime,
            "temp": temp
        }

        with open("~/solar-host/web/solar.json", "w", encoding='utf-8') as outfile:
            json.dump(data, outfile)

        # Show battery % on LED Shim
        #for x in range(round(ledshim.NUM_PIXELS*batt)):
        #    show_graph((x * 0.03571), 255, 0, 255)
        #    time.sleep(0.01)
        #time.sleep(5)
        #ledshim.clear()
        #ledshim.show()

        time.sleep(600) # 10 mins

except KeyboardInterrupt:
    pass
