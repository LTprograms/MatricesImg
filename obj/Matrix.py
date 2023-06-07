from PIL import Image
import numpy as np

class Matrix:
    def __init__(self, url:str) -> None:
        self.__img = Image.open(url)
        self.__img = self.__img.convert("RGB")
        self.__url = url
        self.__matrix = np.array(self.__img)

    def resize(self, w:int, h:int):
        self.__img = self.__img.resize((w, h))
    
    def getImg(self) -> Image:
        return self.__img
    
    def getMatrix(self): 
        return self.__matrix

    def getURL(self) -> str:
        return self.__url
    
    def grayScale(self):
        """ 
        Sets the image to gray scale, 
        it's obteined by multiplying the factor 
        R*0.2989 + G*0.5870 + B*0.1140
        """
        for row in self.__matrix:
            i = 0
            for rgb in row:
                row[i] = rgb * [ 0.2989, 0.5870, 0.1140 ]
                add = sum(row[i])
                row[i] = np.array([add, add, add])
                i += 1

    def invert(self):
        inverted = []
        for row in self.__matrix:
            row = row[::-1]
            inverted.append(row)
        self.__matrix = np.array(inverted)
    
    def setImage(self):
        image = Image.new("RGB", (self.__matrix.shape[1], self.__matrix.shape[0]))
        for y in range(self.__matrix.shape[0]):
            for x in range(self.__matrix.shape[1]):
                color = tuple(self.__matrix[y, x])
                image.putpixel((x, y), color)
        self.__img = image