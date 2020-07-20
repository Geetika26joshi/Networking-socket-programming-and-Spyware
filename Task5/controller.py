#Geetika Joshi
#2019h1030124h

from pyfiglet import Figlet
from functions import *
import subprocess 
from subprocess import call,STDOUT

import os
if __name__ == '__main__':

    f = Figlet(font='slant')
    
    print("")
    

    print("select Menu :")
    print("1 Encypt & Merge into Video")
    print("2 Decrypt & Get the plain text")
   
    choice = raw_input("Choose option : ")

    if choice == "1":
        
        file_name = raw_input("Video file   ? : ")
      

        try:
         
         open('/home/geetika/Desktop/NS/Task5-6/'+file_name)
         
        except IOError:
            
            print(" File not found ")
            exit()


        frame_extract(str(file_name))
        subprocess.call(["ffmpeg", "-i", "/home/geetika/Desktop/NS/Task5-6/"+str(file_name), "-q:a", "0", "-map", "a", "temp/audio.mp3", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)

        encode_frame("temp", "/home/geetika/Desktop/NS/Task5-6/text-to-hide.py",5)
      
        subprocess.call(["ffmpeg", "-i","temp/%d.png" , "-vcodec","png","/home/geetika/Desktop/NS/Task5-6/encVDO.mov"])
        
        subprocess.call(["ffmpeg", "-i", "temp/ %d.png" , "-vcodec", "png", "temp/video.mov", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)

        print("Optimizing encode & Merging audio ")
        
        subprocess.call(["ffmpeg", "-i", "temp/video.mov", "-i", "temp/audio.mp3", "-codec", "copy","/home/geetika/Desktop/NS/Task5-6/enc-" + str(file_name)+".mov", "-y"],stdout=open(os.devnull, "w"), stderr=STDOUT)
       
        print("Success ")

    elif choice == "2" :
        
        

        
        file_name = raw_input(" Video file name in the folder  ? : ")
        '''
        try:
            caesarn = int(raw_input("Caesar cypher n value  ? : "))
        except ValueError:
            
            print(" n is not an integer ")
            exit()
        '''
        try:
            open('/home/geetika/Desktop/NS/Task5-6/'+file_name)
        except IOError:
            
            print("(!) File not found ")
            exit()

        
        frame_extract(str(file_name))
        
        decode_frame("temp",5)

        
        print("Success")


    else:
        exit()

