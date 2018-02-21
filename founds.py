"""Find the picture """
import os

LISTE_ALL_PICTURE = []
EXTENSION = ['.jpeg', ".jpg", ".png", ".gif"]
user_rep = "/"
def find(url=user_rep):
    for dirpath, pathname, filename in os.walk(url):
        try:
            for files in filename:
                #print(files.index("."))
                #print(files[files.index('.'):])
                if files[files.index("."): ] in EXTENSION:
                    LISTE_ALL_PICTURE.append(os.path.join(dirpath, files))
        except:
            pass

                
        
