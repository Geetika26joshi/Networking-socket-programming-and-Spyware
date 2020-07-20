# Networking-socket-programming-and-Spyware
task 1:
client sends audio and video file to server

import socket library

the recieved audio and video are stored in the folder where server script is stored.

task 2:
recording video from webcamera

import cv2 and wav library
client sends the python file to server .This python script search for web cam and record and store in the folder.
client sends code.py to server which stores it as CamCode.py

task 3:
recording audio 
import pyaudio  wave library
client sends the python file to server .This python script record audio and store in the folder.
client send xyz.py to server who stores it as Recieved.py


task 4a:keylogger
import os.path and pynput.keyboard import Key,Listener library
output file is stored in same folder as the code
keylogger.py output is stored in keylog.txt file

task 4b:making customized video
import os 
import cv2  
from PIL import Image
the final generated video is stored in folder pics where all the remaining input images are stored

task 5 :
from pyfiglet import Figlet
from functions import *
import subprocess 
from subprocess import call,STDOUT

import os

from PIL import Image
import shutil,cv2,os

the main is present in controller.py code and other functions like encryption decryption are present in functions.py.The same spyware is transferred
vdo is encoded to encVDO and the text-to-hide file is encrypted inside it .this is actually the keylogger code.
After extraction the recovered-text.py is actually the keylogger which stores the key strokes.
Task 6:
import socket library
Here the server accepts requests from multiple clients which is achieved through multi threading and server transfers the script which will record the key strokes of the clients.

Task 7:
Client sends the keylog file back to the server
The same script which is extracted from the video is sent to the client in task 6 .
now in task 7 we first run the script for the client and then send back the logged text file to the server,therefore first the script named"recieved_file.py is run and the resulted text file that is keylog.txt is sent to the server.

