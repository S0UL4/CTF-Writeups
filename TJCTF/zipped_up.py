import tarfile
import sys
import os
import zipfile
path = "/home/ih3b/Desktop/Unzipper/" 
while True:
    try:
        dirs = os.listdir( path )
        for file in dirs:
            if '.bz2' in file:
                tar = tarfile.open(path+file, "r:bz2")  
                tar.extractall(path)
                break
            if '.kz3' in file:
                with zipfile.ZipFile(path+file, 'r') as zip_ref:
                    zip_ref.extractall(path)
                break
            if '.gz' in file:
                tar = tarfile.open(path+file, "r:gz")
                tar.extractall(path)
                break
        path+=file[:file.find('.')]+'/'
        f=open(path+file[:file.find('.')]+'.txt','r').read()
        if(len(f)!=20):
            print(f)
            sys.exit(0)
    except:
        break
