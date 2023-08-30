
#!/usr/bin/env python3
import subprocess
import threading
import time

oui_list = [
    ['Broadcast', 'ff:ff:ff'],
    ['Multicast', '1:0:5e'],
    ['Apple', '14:98:77', 'a4:c6:f0'],
    ['Askey', '88:de:7c'],
    ['Google', 'ac:67:84'],
    ['Intel', 'dc:53:60'],
    ['MicroStar', '30:9c:23'],
    ['Wiz', '6c:29:90'],
]

if __name__ == '__main__':
    print('start')
    output = subprocess.check_output(['arp', '-a'])
    #output = ['test 1 2 (3)', 'test 2 2 (3)']
    for line in output.splitlines():
        split = str(line).split(' ')
        if len(split) < 4:
            print('X', split)
        else: 
            ip = split[1].removeprefix('(').removesuffix(')')
            mac = split[3]
            vendor = 'Unknown'
            for oui in oui_list:
                for i in range(1, len(oui)):
                    if mac.startswith(oui[i]):
                        vendor = oui[0]
            print(vendor, ip, mac)
    print('done')
