"""Find the [picture] and others group media """
import os
import logging 
import re, shutil, filecmp
 

PICTURE_EXTENSION = ['.jpeg', ".jpg", ".png", ".gif"]
MOVIE_EXTENSION = ["mp4", "avi"]
user_rep = "/"
def find(url=user_rep, extension=PICTURE_EXTENSION):
    liste_all_madia = list()
    for dirpath, pathname, filename in os.walk(url):
        try:
            for files in filename:
                if files[files.index("."): ] in extension:
                    liste_all_madia.append(os.path.join(dirpath, files))
        except:
            pass
    return liste_all_madia


def loggin(loggin='root', passord):
   raise NotImplementError()

