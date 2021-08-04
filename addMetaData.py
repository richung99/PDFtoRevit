from iptcinfo3 import IPTCInfo
from PIL import Image
from cv2 import *
from tkinter import *
import uuid
import textToDir


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
root.geometry("200x80")


def show():
    cam = VideoCapture(1)
    s, img = cam.read()
    if s:
        namedWindow("cam-test")
        imshow("cam-test", img)
        waitKey(0)
        destroyWindow("cam-test")
        filename = 'createIMG/IMG_' + str(uuid.uuid4()) + '.jpg'
        imwrite(filename, img)
        info = IPTCInfo(filename, force=True)

        info['keywords'].append(clicked.get())

        info.save()

    # im = Image.open('filename.png')
    # rgb_im = im.convert('RGB')
    # rgb_im.save('filename.jpg')


def sort_pictures():
    textToDir.create_dir()
    textToDir.sort_by_tag()


# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set(roomList[0])

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# Create Dropdown menu
drop = OptionMenu(root, clicked, *roomList)
drop.pack(pady=5)

button = Button(bottomFrame, text="CAPTURE", command=show).pack(side=LEFT, padx=5, pady=10)

buttonSort = Button(bottomFrame, text="SORT", command=sort_pictures).pack(side=LEFT, padx=5, pady=10)

# Execute tkinter
root.mainloop()
