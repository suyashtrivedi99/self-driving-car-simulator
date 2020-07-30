import numpy as np
import cv2
from PIL import ImageGrab

while(True):
    img = ImageGrab.grab(bbox=(0, 0, 600, 500)) #x, y, w, h
    img_np = np.array(img)
    #frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    #print(img_np)
    #vid.write(img_np)
    cv2.imshow("frame", img_np)
    key = cv2.waitKey(1)
    if key == 27:
        break    

#vid.release()
cv2.destroyAllWindows()