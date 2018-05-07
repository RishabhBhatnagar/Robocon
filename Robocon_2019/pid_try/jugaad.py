'''jugaad'''
from time import time as millis
from time import sleep
sizeof = len
class Serial:
    def println(*args):
        print(*args)
    def print(*args):
        print(*args, end = "")
delay = lambda milliseconds : sleep(milliseconds/1000)
'''Jugaad ends here.'''
