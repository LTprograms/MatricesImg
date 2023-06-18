from PIL import Image
import numpy as np

class Matrix:
    def __init__(self, url:str) -> None:
        self.__img = Image.open(url)
        self.__img = self.__img.convert("RGB")
        self.__url = url
        self.resize(300)

    def resize(self, w:int):
        self.__matrix = np.array(self.__img) 
        self.__matrix = self.__matrix.tolist()
        ratio = self.__img.width / float(self.__img.height)
        h = int(w / ratio)

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
                row[i] = [0.2989*rgb[0],0.5870*rgb[1], 0.1140*rgb[2]]
                add = sum(row[i])
                row[i] = np.array([int(add), int(add), int(add)])
                i += 1

    def invert(self):
        i = 0
        for row in self.__matrix:
            aux = row
            aux.reverse()
            self.__matrix[i] = aux
            i+=1

    def rotate(self):
        dim = (len(self.__matrix), len(self.__matrix[0]), 3)
        rotated = np.zeros((dim[1], dim[0], dim[2]), dtype=np.int32)
        i = 0
        for row in self.__matrix:
            j = 0
            for rgb in row:
                rotated[j][dim[0]-1-i] = rgb
                j+=1
            i+=1
        self.__matrix = rotated.tolist()

    def bright(self):
        i = 0
        for row in self.__matrix:
            j = 0
            for rgb in row:
                k = 0
                for pixel in rgb:
                    pixel = pixel*1.2
                    if pixel > 255:
                        pixel = 255
                    self.__matrix[i][j][k] = int(pixel)
                    k+=1
                j+=1
            i+=1
    
    def setImage(self):
        image = Image.new("RGB", (len(self.__matrix[0]), len(self.__matrix)))
        for y in range(len(self.__matrix)):
            for x in range(len(self.__matrix[0])):
                color = tuple(self.__matrix[y][x])
                image.putpixel((x, y), color)
        self.__img = image
        self.resize(300)