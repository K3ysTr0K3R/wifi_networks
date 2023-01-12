#!/bin/python3

import subprocess
import re

results = subprocess.run(['iwlist', 'wlan0', 'scan'], capture_output=True)
networks = re.findall(r'Address: [A-F0-9:]{17}', results.stdout.decode())
channels = re.findall(r'Channel:[^\d]*(\d+)', results.stdout.decode())
mac = networks[0][9:]
for line in results.stdout.decode().split("\n"):
    match = re.search(r'ESSID:"(.*)"', line)
    if match:
        ssid = match.group(1)
        print("SSID:", ssid)
        print("MAC:", mac)
        print("CHANNEL:", channels[0])
