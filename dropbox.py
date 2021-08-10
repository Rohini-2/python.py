import dropbox
class transferData:
    def __init__(self,accessToken) :
        self.accessToken=accessToken
    def transfer(self,source,destination)    :
        db=dropbox.Dropbox(self.accessToken)
        f=open(source,"rb")
        db.files_upload(f.read(),destination)

def main():
    t=transferData("4-xQQvI1I-gAAAAAAAAAARVbibMNXbZlXgHPD2jDnu21nT4uboklXbTkNWrFfisa")
    t.transfer("file1.txt","/pythonFiles123/file1.txt")

