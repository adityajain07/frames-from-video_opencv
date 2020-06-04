#!/usr/bin/env python
# coding: utf-8

# In[17]:


'''
This code fetches frames from video given a frame rate
Author: Aditya Jain
Date  : 2nd June, 2020
'''
import cv2
import math

VIDEO_PATH = "/home/aditya/Dropbox/LearningfromDemons/VideoData/robot_video2.mp4" 
WRITE_PATH = "/home/aditya/Dropbox/LearningfromDemons/ImageData/robot_video2/"
FRAME_RATE = 10              # FPS : CHANGE HERE, Mention the FPS here to fetch data
TIME_SEC   = 1/FRAME_RATE    # a frame after every this second


# In[18]:


sec    = 0
vidcap = cv2.VideoCapture(VIDEO_PATH)

# calculates total video length
vidcap.set(cv2.CAP_PROP_POS_AVI_RATIO,1)
total_sec = math.floor(vidcap.get(cv2.CAP_PROP_POS_MSEC)/1000)   

count  = 0


while (sec < total_sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)     # setting the which frame to get
    
    sec          += TIME_SEC
    success,image = vidcap.read()
    
    if success:
        cv2.imwrite(WRITE_PATH + "image-"+ str(count) + ".jpg", image) 
        count += 1
    else:
        break

        
vidcap.release()






