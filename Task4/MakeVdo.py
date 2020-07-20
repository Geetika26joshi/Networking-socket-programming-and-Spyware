#Geetika Joshi
#2019h1030124h 


import os 
import cv2  
from PIL import Image
 
print(os.getcwd())  
  

os.chdir("/home/geetika/Desktop/NS/Task4/pics/")   
path = "/home/geetika/Desktop/NS/Task4/pics"
  
mean_height = 0
mean_width = 0
  
num_of_images = len(os.listdir('.')) 
 
  
for file in os.listdir('.'): 
    im = Image.open(os.path.join(path, file)) 
    width, height = im.size 
    mean_width += width 
    mean_height += height 
   
mean_width = int(mean_width / num_of_images) 
mean_height = int(mean_height / num_of_images) 

for file in os.listdir('.'): 
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"): 
         
        im = Image.open(os.path.join(path, file))  
   
        
        width, height = im.size    
        print(width, height) 
  
        # resizing  
        imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)  
        imResize.save( file, 'JPEG', quality = 95) 
        print(im.filename.split('\\')[-1], " is resized")  
  
  

def generate_video(): 
    image_folder = '.'  
    video_name = 'GeneratedVdo.avi'
    os.chdir("/home/geetika/Desktop/NS/Task4/pics") 
      
    images = [img for img in os.listdir(image_folder) 
              if img.endswith(".jpg") or
                 img.endswith(".jpeg") or
                 img.endswith("png")] 
    
    print("generating video")  
  
    frame = cv2.imread(os.path.join(image_folder, images[0])) 
  
   
    height, width, layers = frame.shape   
  
    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'DIVX'), 0.5, (width, height))  
  
    
    for image in images:  
        video.write(cv2.imread(os.path.join(image_folder, image)))  
      
     
    cv2.destroyAllWindows()  
    print("successfully generated")
    video.release()  
  

generate_video() 

