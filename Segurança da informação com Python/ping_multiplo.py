import os
import time

with open('host.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('-' * 60)
        print(" " * 14 + 'Verificando ip: ', ip)
        print('-' * 60)
        time.sleep(2)
        os.system('ping -n 2 {}'.format(ip))
        time.sleep(5)
