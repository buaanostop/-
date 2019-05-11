import Monkey
import sys

sendsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 9999
host = '127.0.0.1'
def close_monkeyrunner():
    Monkey.close()
def close_model():
    sendsocket.sendto(1,(port,host))