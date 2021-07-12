class TextClass:
    def __init__(self, bbox, text, prob):
        self.bbox = bbox
        self.text = text
        self.prob = prob

    def getBbox(self):
        return self.bbox

    def getText(self):
        return self.text

    def getProb(self):
        return self.prob
