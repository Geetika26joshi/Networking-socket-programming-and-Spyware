#Capture video from webcam
import cv2

captured = cv2.VideoCapture(0)
vid = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("VdoCamera.mp4", vid, 20.0, (640,480))
while(True):
     # Capturing all the frames of recorded webcam video
    ret,frame = captured.read()
    cv2.imshow("My cam video", frame)
    output.write(frame)
    # Close and break the loop after pressing "z" key
    if cv2.waitKey(1) &0XFF == ord('z'):
        break
    # close the  opened camera
captured.release()
# close the opened file
output.release()
 
