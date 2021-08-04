import os
from tkinter.filedialog import askopenfilename
from iptcinfo3 import IPTCInfo
import shutil

# ROOT_DIR = os.path.dirname(os.path.abspath("addMetaData.py"))


def cleanup_text(text):
    # strip out non-ASCII text so we can draw the text on the image
    # using OpenCV
    return "".join([c if ord(c) < 128 else "" for c in text]).strip()


def create_dir():
    filename = askopenfilename()

    with open(filename) as x:
        os.chdir("createDir")
        for line in x:
            line = cleanup_text(line)
            lineArr = line.strip().split(",")
            lineArr[1] = lineArr[1].replace("/", "")
            if not os.path.exists(lineArr[0] + " " + lineArr[1]):
                os.mkdir(lineArr[0] + " " + lineArr[1])

    os.chdir('..')


def sort_by_tag():
    for file in os.listdir("createIMG"):
        if file.endswith(".jpg"):
            info = IPTCInfo('createIMG/' + file)
            infoTag = info['keywords']
            print(infoTag[0].decode("utf-8"))
            shutil.copy('createIMG/' + file, 'createDir/' + infoTag[0].decode("utf-8"))
