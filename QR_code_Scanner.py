import cv2
from pyzbar.pyzbar import decode

capture = cv2.VideoCapture(0) #for capturing video from defalut camera
recieved_data= None
while True:
    _,frame = capture.read() #read the images and save to frame

    decoded_data = decode(frame) #if there is qr code then save it in variable
    try:
        data=decoded_data[0][0]
        if data != recieved_data:
            print(data)
            recieved_data=data
    except:
        pass
    cv2.imshow("QR code Scanner",frame)

    key = cv2.waitKey(1) #wait for 1 milisecond
     
    if key == ord('q'):
        break