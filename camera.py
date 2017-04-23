import argparse
from picamera import PiCamera
from time import sleep

parser = argparse.ArgumentParser(description='take images')
parser.add_argument('fileName', help='Set file name')
args = parser.parse_args()

print(args.fileName)

with PiCamera() as camera:
    #camera.resolution = (2592, 1944) #max resolution for still images
    sleep(5)
    #camera.capture('/home/pi/Desktop/%s.jpg' % fname)
    camera.capture('/home/pi/Desktop/%s.jpg' % args.fileName)

### camera.resolution = (64, 64)
##camera.framerate = 15 # framerate must be set to 15 to permit high resolution images. 
##
###camera.start_preview(alpha=255) #turn camera on.
##camera.annotate_text = "Hello World!"
##
###take five pictures
###for i in range(5):
##i = 1
##sleep(5) #must sleep at least 2 seconds before capturing so sensor can set light levels
##camera.capture('/home/pi/Desktop/%s.jpg' % fname)
##
### Record video
###camera.start_recording('/home/pi/Desktop/video.h264')
###sleep(10)
###camera.stop_recording()
##
##
##    
###camera.stop_preview()

