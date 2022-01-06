## Jayavardhan Ramasani 

import numpy as np
from PIL import ImageGrab
import cv2
import time

def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [0,255,0], 1)
    except:
        pass

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(original_img):
    processed_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    #processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    processed_img = cv2.GaussianBlur(processed_img, (11,11), 0)
    processed_img = cv2.Canny(processed_img, threshold1=40, threshold2=50)
    vertices = np.array([[0,500],[0,300],[150,250],[500,250],[650,300],[650,500]])

    processed_img = roi(processed_img, [vertices])
    ##processed_img = cv2.GaussianBlur(processed_img, 11)



    lines = cv2.HoughLinesP(processed_img,1,np.pi/180,180,np.array([]) ,20, 15)
    draw_lines(processed_img, lines)
    #draw_lines(original_img, lines)
    return processed_img
    #return cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)

last_time = time.time()
while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,150,650,500)))
    new_screen = process_img(screen)
    #printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')\
    #.reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))
    #cv2.namedWindow('window', cv2.CV_WINDOW_AUTOSIZE)
    #cv2.startWindowThread()
    cv2.imshow('window1',new_screen)
    #cv2.imshow('window2',cv2.cvtColor(new_screen,cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
