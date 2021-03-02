import cv2
import numpy as np
import pytesseract
import re
camera_port=0
cap =  cv2.VideoCapture(0)
pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\LENOVO\\Desktop\\Tesseract-OCR\\tesseract.exe'
font = cv2.FONT_HERSHEY_SIMPLEX

i=1
str = ''
prev_str = ''
str_show = ''

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    kernel = np.ones((1, 1), np.uint8)
    hsv = cv2.dilate(hsv, kernel, iterations=1)
    hsv = cv2.erode(hsv, kernel, iterations=1)

    
    
    sensitivity = 15
    lower_white = np.array([0,0,255-sensitivity], dtype=np.uint8)
    upper_white = np.array([255,sensitivity,255], dtype=np.uint8)

    
    mask = cv2.inRange(hsv, lower_white, upper_white)

    i=i + 1
    result = ''
    if i == 30:
        result=pytesseract.image_to_string(mask)
        print(result)



        str = re.sub('[^0-9a-zA-Z -]+', '', result)

        i=1

    if str!='':
        str_show = str
        prev_str = str
    else:
        str_show = prev_str

    cv2.putText(frame,str_show, (230, 50), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('frame',frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


camera.release()
cv2.destroyAllWindows()