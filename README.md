# frames-from-video_opencv
Often in deep learning applications, one has video dataset and requires individual images to be fetched from it. This repository contains a short code for fetching frames from a video using opencv, given a desired frame rate. 

PS: I didn't find any commonly available library or opencv function which does this.

## Dependencies
1. opencv2
2. python3 (my system had python3 but ideally, should work with python2 as well)

## Setup
Simply run the fetch-frame.py script with the following changes:
1. Line 15 (VIDEO_PATH) - Change the input video path
2. Line 16 (WRITE_PATH) - Change the write directory for the images
3. Line 17 (FRAME_RATE) - Mention the desired frame rate i.e. how many frames you require per second. Usually videos are 30 fps. Thus, this variable should be <= 30. 
