from ultralytics import YOLO
import cv2
from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated
import socket
from math import atan, tan, pi
import time

# Define host and port
HOST = '10.24.70.153'  
PORT = 12345 


model = YOLO('DroneSpottingRiktig.pt')
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))

    server_socket.listen()

    print("Waiting for connection...")
    conn, addr = server_socket.accept()
    with conn:
        print('Connected by', addr)

        while True:
            _, img = cap.read()
            results = model.predict(img)

            for r in results:
                
                annotator = Annotator(img)
                pos = 0
                x_pos = 320
                y_pos = 180
                sector = 39
                best_conf_score = 0
                confidence_score = 0
                boxes = r.boxes
                counter = 0

                for box in boxes:
                    confidence_score = float(box.conf)

                    b = box.xyxy[0]  # get box coordinates in (top-left corner, bottom-right corner) format

                    b1,b2,b3,b4 = float(b[0]),float(b[1]),float(b[2]),float(b[3])
                    center_x = (b3 - b1)/2 + b1
                    center_y = (b4 - b2)/2 + b2

                    if confidence_score > best_conf_score:
                        best_conf_score = confidence_score
                        pos = counter
                        x_pos = center_x
                        y_pos = center_y
                    
                    c = box.cls
                    counter += 1
                    annotator.box_label(b, f'{model.names[int(c)]} {confidence_score: .2f}')

                print(f'x_pos: {x_pos}')
                print(f'y_pos: {y_pos}')

                if(x_pos < 320):
                    x_pos_rad = -atan((320-x_pos)/(320/tan(13*pi/60)))
                    print(f'x_pos_rad: {x_pos_rad}')
                    steps = int(x_pos_rad/(1.8*pi/180))
                    print(f'Steps: {steps}')
                    steps = 'sx' + str(steps)

                    data_to_send = steps.encode()
                    conn.sendall(data_to_send)
                
                else:
                    x_pos_rad = atan((x_pos-320)/(320/tan(13*pi/60)))
                    print(f'x_pos_rad: {x_pos_rad}')
                    steps = int(x_pos_rad/(1.8*pi/180))
                    print(f'Steps: {steps}')
                    steps = 'sx' + str(steps)

                    data_to_send = steps.encode()
                    conn.sendall(data_to_send)

                if(y_pos < 240):
                    y_pos_rad = -atan((240-y_pos)/(240/tan(13*pi/60)))
                    print(f'y_pos_rad: {y_pos_rad}')
                    steps = int(y_pos_rad/(1.8*pi/180))
                    print(f'Steps y_dir: {steps}')
                    steps = 'sy' + str(steps)

                    data_to_send = steps.encode()
                    conn.sendall(data_to_send)

                else:
                    y_pos_rad = atan((y_pos-240)/(240/tan(13*pi/60)))
                    print(f'y_pos_rad: {y_pos_rad}')
                    steps = int(y_pos_rad/(1.8*pi/180))
                    print(f'Steps y_dir: {steps}')
                    steps = 'sy' + str(steps)

                    data_to_send = steps.encode()
                    conn.sendall(data_to_send)

            img = annotator.result()  
            cv2.imshow('YOLO V8 Detection', img)     
            if cv2.waitKey(1) & 0xFF == ord(' '):
                break

        cap.release()
        cv2.destroyAllWindows()