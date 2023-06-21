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
        self.__matrix = self.__matrix
        ratio = self.__img.width / float(self.__img.height)
        h = int(w / ratio)

        self.__img = self.__img.resize((w, h))

    
    def get_img(self) -> Image:
        return self.__img
    
    def get_matrix(self): 
        return self.__matrix

    def get_URL(self) -> str:
        return self.__url
    
    def gray_scale(self):
        """ 
        Sets the image to gray scale, 
        it's obteined by multiplying the factor 
        R*0.2989 + G*0.5870 + B*0.1140
        """
        factor = np.array([0.2989, 0.5870, 0.1140])
        for row in self.__matrix:
            i = 0
            for rgb in row:
                product = rgb * factor
                add = sum(product)
                row[i] = np.array([add for i in range(3)])
                i += 1

    def invert(self):
        i = 0
        for row in self.__matrix:
            self.__matrix[i] = np.flip(self.__matrix[i], axis=0)
            i+=1

    def rotate(self):
        dim = self.__matrix.shape
        rotated = np.zeros((dim[1], dim[0], dim[2]), dtype=np.int32)
        i = 0
        for row in self.__matrix:
            j = 0
            for rgb in row:
                rotated[j][dim[0]-1-i] = rgb
                j+=1
            i+=1
        self.__matrix = rotated

    def bright(self):
        i = 0                  
        for row in self.__matrix:
            j = 0
            for rgb in row:
                k = 0
                for color in rgb:
                    color *= 1.2
                    if color > 255:
                        color = 255
                    self.__matrix[i][j][k] = int(color)
                    k+=1
                j+=1
            i+=1
    
    def set_image(self):
        image = Image.new("RGB", (len(self.__matrix[0]), len(self.__matrix)))
        for y in range(len(self.__matrix)):
            for x in range(len(self.__matrix[0])):
                color = tuple(self.__matrix[y][x])
                image.putpixel((x, y), color)
        self.__img = image
        self.resize(300)
    
    def get_reduced_matrix(self):
        chunk_size = 5
        matriz_3d = np.array(self.__matrix)
        dimensiones_originales = matriz_3d.shape
        bloques_n = dimensiones_originales[0] // chunk_size
        bloques_m = dimensiones_originales[1] // chunk_size
        bloques_3d = matriz_3d[:bloques_n*chunk_size, :bloques_m*chunk_size, :].reshape(bloques_n, chunk_size, bloques_m, chunk_size, 3)
        promedios_3d = np.round(bloques_3d.mean(axis=(1, 3))).astype(int)

        return promedios_3d.tolist()