import os
from tkinter.filedialog import askopenfilename


def cleanup_text(text):
    # strip out non-ASCII text so we can draw the text on the image
    # using OpenCV
    return "".join([c if ord(c) < 128 else "" for c in text]).strip()


filename = askopenfilename()

with open(filename) as x:
    os.chdir("createDir")
    for line in x:
        line = cleanup_text(line)
        lineArr = line.strip().split(",")
        lineArr[1] = lineArr[1].replace("/", "")
        if not os.path.exists(lineArr[0] + " " + lineArr[1]):
            os.mkdir(lineArr[0] + " " + lineArr[1])
