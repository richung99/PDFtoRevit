from iptcinfo3 import IPTCInfo
from PIL import Image
from cv2 import *
from tkinter import *
import uuid


def cleanup_text(text):
    # strip out non-ASCII text so we can draw the text on the image
    # using OpenCV
    return "".join([c if ord(c) < 128 else "" for c in text]).strip()


roomList = []

with open('roomList.csv') as x:
    for line in x:
        line = cleanup_text(line)
        lineArr = line.strip().split(",")
        lineArr[1] = lineArr[1].replace("/", "")
        roomList.append(lineArr[0] + " " + lineArr[1])

# Create object
root = Tk()

# Adjust size
root.geometry("200x200")


def show():
    cam = VideoCapture(0)
    s, img = cam.read()
    if s:
        namedWindow("cam-test")
        imshow("cam-test", img)
        waitKey(0)
        destroyWindow("cam-test")
        filename = 'IMG_' + str(uuid.uuid4()) + '.jpg'
        imwrite(filename, img)

    # im = Image.open('filename.png')
    # rgb_im = im.convert('RGB')
    # rgb_im.save('filename.jpg')

    info = IPTCInfo(filename, force=True)

    info['keywords'].append(clicked.get())

    info.save()


# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set(roomList[0])

# Create Dropdown menu
drop = OptionMenu(root, clicked, *roomList)
drop.pack()

button = Button(root, text="Take Picture", command=show).pack()

# Execute tkinter
root.mainloop()
