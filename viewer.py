import cv2
import zmq
import base64
import numpy as np

ip = input("please enter ip: ")
# ip ='10.19.129.177'
context = zmq.Context()
footage_socket = context.socket(zmq.SUB)
footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))
footage_socket.connect('tcp://' + ip + ':5555')

while True:
    try:
        frame = footage_socket.recv_string()
        img = base64.b64decode(frame)
        # print(img[:20])
        npimg = np.fromstring(img, dtype=np.uint8)
        print(npimg[:20])
        source = cv2.imdecode(npimg, 1)
        cv2.imshow("Stream", source)
        cv2.waitKey(1)

    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        break