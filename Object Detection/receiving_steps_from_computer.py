import socket
from time import sleep
import RPi.GPIO as GPIO


# Define host and port
HOST = 'host_ip_address'
PORT = 12345                 

DIR = 20    # Direction GPIO Pin
STEP = 21   # Step GPIO Pin
DIR_Y = 5   # Direction in y GPIO Pin
STEP_Y = 6  # Step in y direction GPIO Pin

CW = 1      # Clockwise Rotation
CCW = 0     # Counterclockwise Rotation
SPR = 200   # Steps per Revolution (360 / 1.8)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR_Y, GPIO.OUT)
GPIO.setup(STEP_Y, GPIO.OUT)

MODE = (14, 15, 16)
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0), 
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}

GPIO.output(MODE, RESOLUTION['1/32'])


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

    client_socket.connect((HOST, PORT))
    print(f'connected to sender at {HOST}:{PORT}')

    while True:
        data = client_socket.recv(1024)
        data = data.decode()
        data = data.split('s')

        if(data[-1][0] == 'x'):

            data = data[-1].split('x')
            data = int(data[-1])
            print(f'Received data: {data}')


            data = client_socket.recv(1024)

            print(f'Received: {data}')

            delay = .005 / 32

            if(data < 0):
                GPIO.output(DIR, CCW)
                step_count = abs(data)
                for i in range(step_count):
                    GPIO.output(STEP, GPIO.HIGH)
                    sleep(delay)
                    GPIO.output(STEP, GPIO.LOW)
                    sleep(delay)        

            elif(data > 0):
                GPIO.output(DIR, CW)
                step_count = data
                for i in range(step_count):
                    GPIO.output(STEP, GPIO.HIGH)
                    sleep(delay)
                    GPIO.output(STEP, GPIO.LOW)
                    sleep(delay)

            else:
                continue

        elif(data[-1][0] == 'y'):

            data = data[-1].split('y')
            data = int(data[-1])
            print(f'Received data: {data}')

            data = client_socket.recv(1024)

            print(f'Received: {data}')

            delay = .005 / 32

            if(data < 0):
                GPIO.output(DIR_Y, CCW)
                step_count = abs(data)
                for i in range(step_count):
                    GPIO.output(STEP_Y, GPIO.HIGH)
                    sleep(delay)
                    GPIO.output(STEP_Y, GPIO.LOW)
                    sleep(delay)        

            elif(data > 0):
                GPIO.output(DIR_Y, CW)
                step_count = data
                for i in range(step_count):
                    GPIO.output(STEP_Y, GPIO.HIGH)
                    sleep(delay)
                    GPIO.output(STEP_Y, GPIO.LOW)
                    sleep(delay)

            else:
                continue