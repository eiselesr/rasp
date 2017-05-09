import argparse
from picamera import PiCamera
from time import sleep

parser = argparse.ArgumentParser(description='take images')
parser.add_argument('fileName', help='Set file name')
args = parser.parse_args()

print(args.fileName)

##with PiCamera() as camera:
##    #camera.resolution = (2592, 1944) #max resolution for still images
##    camera.start_preview()
##    sleep(5)
##    camera.capture('/home/pi/Desktop/%s.jpg' % args.fileName)
##    camera.stop_preview()

with PiCamera() as camera:
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/%s.h264' % args.fileName)
    sleep(20)
    camera.stop_recording()
    camera.stop_preview()


