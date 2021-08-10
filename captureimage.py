import dropbox
import random
import time
import cv2
starttime=time.time()
class uploadfile:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken
    def uploadFilesToDb(self,source,destination):
        db=dropbox.Dropbox(self.accesstoken)
        f=open(source,"rb")
        db.files_upload(f.read(),destination)
def captureImage():
    image=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=image.read()
        imagename="img"+str(random.randint(1,100))+".png"
        cv2.imwrite(imagename,frame)
        starttime=time.time()
        result=False
    return imagename    
    image.release()


        

    

def main():
    while(True):
        if(time.time()-starttime>5):
            imagename=captureImage()
            f=uploadfile("35r6VdDyMtgAAAAAAAAAARHPT50ex5fTL1FjZZlWyMaBuvqVruxmxPp4b5yYSM7y")
            f.uploadFilesToDb(imagename,"/pythonFiles123/file1.txt")
main()

        
