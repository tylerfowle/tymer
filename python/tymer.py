#!/usr/bin/env python
import sys
import os
import datetime
import time
from time import sleep

TYMERS_FILEPATH=os.path.expanduser('~/.tymer/tymers.txt')

TYMERS_FILE = open(TYMERS_FILEPATH, "r")

CURRENT_TIME=time.ctime()
CURRENT_TIME_SEC=time.time()

ARGUMENT_LEN=len(sys.argv)
ARGUMENT_LIST=str(sys.argv)

print ARGUMENT_LEN
print ARGUMENT_LIST





print(CURRENT_TIME)
print(CURRENT_TIME_SEC)



exit()


while True:
    CURRENT_TIME=time.ctime()
    CURRENT_TIME_SEC=time.time()
    os.system('clear')
    print(CURRENT_TIME_SEC)
    sleep(1)


