#!/bin/python3

import subprocess
import wifi
import re

wifi_networks = wifi.Cell.all('wlan0')
results = subprocess.run(['iwlist', 'wlan0', 'scan'], capture_output=True)
networks = re.findall(r'Address: [A-F0-9:]{17}', results.stdout.decode())
channels = re.findall(r'Channel:[^\d]*(\d+)', results.stdout.decode())

try:
    mac = networks[0][9:]
    lines = results.stdout.decode().split("\n")
    for line in lines:
        match = re.search(r'ESSID:"(.*)"', line)
        if match:
            ssid = match.group(1)
            print("")
            if not ssid:
                print("SSID: None")
            else:
                print("SSID:", ssid)
            print("MAC:", mac)
            print("CHANNEL:", channels[0])
            for network in wifi_networks:
                if network.address == mac:
                    print("PASSWORD:", network.encrypted)
                    break
            print("")
except IndexError:
    print("[!] Couldnt capture WIFI networks")
