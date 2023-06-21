import serial
from time import sleep

DEFAULT_MESSAGE = 'c - Clockwise | C - Counter clockwise: '

# TODO Use ls -l /dev/ttyACM* + grep to fetch port name
# TODO Controlling rotation based on steps

connection = serial.Serial('/dev/ttyACM0', 9600)
# Wait for Arduino to reboot before issuing the first command
sleep(2)

while(data := input(DEFAULT_MESSAGE).encode('utf-8')):
    connection.write(data)
    response = connection.readline()
    print(response)
