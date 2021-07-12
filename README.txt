
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

## Usage
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
Schedules that are exported in Revit should be reformatted such that the Room Number and Room Name are separated by commas and appear as the first 2 columns in the .csv file. To create file directories based on a Room List .csv:

```console
> textToDir.py
```

This will prompt you to select the .csv file to export, and all newly created file directories will be located under /createDirs.
## License
[MIT](https://choosealicense.com/licenses/mit/)