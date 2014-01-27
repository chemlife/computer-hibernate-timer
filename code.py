import os
from time import sleep


def minute(x, y):
    z = x*60+y
    return z




x = int(input('Time minutes: '))
y = int(input('Time seconds: '))
z = 0
sleep(minute(x, y))



os.system(r'%windir%\system32\rundll32.exe powrprof.dll,SetSuspendState Hibernate')
