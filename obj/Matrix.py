from PIL import Image

class Matrix:
    def __init__(self, url:str) -> None:
        self.__img = Image.open(url)
        self.__img = self.__img.convert("RGB")

    def resize(self, w:int, h:int):
        self.__img = self.__img.resize((w, h))
    
    def getImg(self) -> Image:
        return self.__img
    
    def getMatrix(self) -> list: 
        return list(self.__img.getdata())