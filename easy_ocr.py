# import the necessary packages
from easyocr import Reader
import argparse
import cv2
import enchant
import os

from TextClass import TextClass


def resizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)


def cleanup_text(text):
    # strip out non-ASCII text so we can draw the text on the image
    # using OpenCV
    return "".join([c if ord(c) < 128 else "" for c in text]).strip()


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")
ap.add_argument("-l", "--langs", type=str, default="en",
                help="comma separated list of languages to OCR")
ap.add_argument("-g", "--gpu", type=int, default=-1,
                help="whether or not GPU should be used")
args = vars(ap.parse_args())

# break the input languages into a comma separated list
langs = args["langs"].split(",")
#langs = "en"
print("[INFO] OCR'ing with the following languages: {}".format(langs))

# load the input image from disk
image = cv2.imread(args["image"])
#image = cv2.imread("testplan3.png")

# OCR the input image using EasyOCR
print("[INFO] OCR'ing input image...")
reader = Reader(langs, gpu=args["gpu"] > 0)
# reader = Reader(["en"], False)
results = reader.readtext(image)

textList = [TextClass(bbox, text, prob) for (bbox, text, prob) in results]
d = enchant.Dict("en_US")

roomList = []

# loop over the results
for (bbox, text, prob) in results:

    # display the OCR'd text and associated probability
    print("[INFO] {:.4f}: {}".format(prob, text))

    # unpack the bounding box
    (tl, tr, br, bl) = bbox
    tl = (int(tl[0]), int(tl[1]))
    tr = (int(tr[0]), int(tr[1]))
    br = (int(br[0]), int(br[1]))
    bl = (int(bl[0]), int(bl[1]))

    # cleanup the text and draw the box surrounding the text along
    # with the OCR'd text itself
    text = cleanup_text(text)
    cv2.rectangle(image, tl, br, (0, 255, 0), 2)
    cv2.putText(image, text, (tl[0], tl[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200, 50, 133), 2)

    # check if text is an English word contained in the dictionary.
    # if it is a valid word, check for adjacent text to obtain the room number.
    for checkWord in text.split():
        if d.check(checkWord.lower()):
            for textObject in textList:
                tr2 = textObject.getBbox()[1]
                tr2 = (int(tr2[0]), int(tr2[1]))
                if (br[1] - tr2[1]) < 0.5 and (br[0] - tr[0]) < 5:
                    roomList.append(textObject.getText() + "," + text + ",\n")
                    break
            break

print(roomList)

file1 = open("roomList.csv", "a")
file1.writelines(roomList)
file1.close()

# show the output image
resize = resizeWithAspectRatio(image, width=1280)
cv2.imshow("Image", resize)
cv2.waitKey(0)
