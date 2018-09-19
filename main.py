#main file to compile car counting
import cv2

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
hv = cv2.VideoWriter('my.avi',fourcc,fps=10,frameSize=(640,480))
