# PDFtoRevit

PDFtoRevit is a Python script that uses EasyOCR and computer vision techniques to extract room names and numbers from a building plan PDF. It can also export a .csv file of a Room List to individual file directories.

## Installation

Clone or download the Github repository.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install Pillow
pip install easyOCR
pip install enchant
```

## Image Processing
To run the image processing software, use the command line and navigate to the directory that the project is saved to. For command line arguments, 2 must be provided: the --image (image path) and --lang (languages to process).
```console
> easy_ocr.py --image filepath\image.png --lang en
```

The imaging processing software also produces a text file in the format of:
```bash
Room Number,Room Name,
Room Number,Room Name,
...
```
Schedules that are exported in Revit should be reformatted such that the Room Number and Room Name are separated by commas and appear as the first 2 columns in the .csv file.

## On Site Photo Capture and Storage
addMetaData.py is used to capture and sort images into room directories. To use, navigate to the dist folder and run addMetaData.exe, which will launch the user interface shown below.

![addMetaData GUI](/images/gui.PNG?raw=true "addMetaData GUI")

A: The drop down menu is populated from roomList.csv. Replace this file to edit the contents of the drop down list.

B: Images can be captured and stored inside of the createIMG directory. These images are tagged with IPTC metadata containing the room name. A preview of the capture image will be displayed on screen. This window can only be closed with a keyboard input and not by hitting the 'X' button.

C: All images inside of the createIMG are sorted into individual room directories inside of the createDir directory based on their metadata tagging.

## License
[MIT](https://choosealicense.com/licenses/mit/)
