import tkinter as tk
from PIL import ImageTk
from obj.Matrix import Matrix

class Screen(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Imagenes")
        self.state("zoomed")
        self.resizable(0, 0)
        self.__setColumns()
        self.__setTextArea()
        self.__setControls()
    
    def getSize(self) -> tuple[int, int]:
        """Returns (width, height) of screen in a tuple"""
        return self.winfo_screenwidth(), self.winfo_screenheight()
    
    def __setColumns(self) -> None:
        """Sets the 2 main frames of the app"""
        w, h = self.getSize()

        self.__fr1 = tk.Frame(self)
        self.__fr2 = tk.Frame(self)

        self.__fr1.config(width=(w*3)//5, height=h)
        self.__fr2.config(width=(w*2)//5, height=h)

        self.__fr1.place(x=0, y=0)
        self.__fr2.place(x=(w*3)//5, y=0)
    
    def setImage(self, img:Matrix) -> None:
        """Sets the image to display in the app"""
        self.__matrix = img
        w, h = self.getSize()
        img.resize((w*2)//5, h)
        self.__photo = ImageTk.PhotoImage(img.getImg())

        for child in self.__fr2.winfo_children():
            child.destroy()
        
        lb = tk.Label(self.__fr2, image=self.__photo)
        lb.place(x=(w)//5, y=h//2, anchor="center")

    def __setTextArea(self) -> None:
        """Sets the text area where it is going to display the Matrix"""
        w, h = self.getSize()
        auxFr = tk.Frame(self.__fr1, width=(w*3)//2, height=(h*4)//5)
        auxFr.place(x=0, y=0)
        cv = tk.Canvas(auxFr)
        cv.pack(fill="both", expand=True)
        self.__txt = tk.Text(cv)
        self.__txt.config(font=("helvetica", 16))
        self.__txt.pack(fill="both", side="left", expand=True)        

    def __setControls(self) -> None:
        """Sets the controls frame"""
        w, h = self.getSize()
        self.__controls = tk.Frame(self.__fr1)
        self.__controls.config(width=(w*3)//2, height=h//5)
        self.__controls.place(x=0, y=h, anchor="sw")

        self.__grayBtn = AppButton(self.__controls, "Grises", ((w*1)//10))
        self.__grayBtn.config(command=lambda:self.transformImg(1))
        self.__invBtn = AppButton(self.__controls, "Invertir", (w*2)//10)
        self.__invBtn.config(command=lambda:self.transformImg(2))
        self.__rotBtn = AppButton(self.__controls, "Rotar", (w*3)//10)
        self.__rotBtn.config(command=lambda:self.transformImg(3))
        self.__brightBtn = AppButton(self.__controls, "Brillo", (w*4)//10)
        self.__brightBtn.config(command=lambda:self.transformImg(4))

    def printMatrix(self) -> None:
        """Prints the matrix to TextField"""
        string = self.__matrix.getMatrix()
        # string = string[1:-2]
        # string = string.replace("]\n  [", "]\t\t[")
        self.__txt.delete("1.0", "end")
        size = 1000000
        for i in range(0, len(string), size):
            chunk = string[i:i + size]
            
            for item in chunk:
                self.__txt.insert("end", str(item).replace("], [", "]\t\t["))

    def transformImg(self, num:int) -> None:
        """
        Transform the RGB matrix depending of the num constant:\n
        * 1: Gray scale\n
        * 2: Invert image\n
        * 3: Rotate image\n
        * 4: Change brightness\n
        """
        match num:
            case 1:
                self.__matrix.grayScale()
            case 2:
                self.__matrix.invert()
            case 3:
                self.__matrix.rotate()
            case 4:
                self.__matrix.bright()
        self.__matrix.setImage()
        self.setImage(self.__matrix)
        self.printMatrix()
    
           
class AppButton(tk.Button):
    def __init__(self, master, text, i):
        super().__init__(master)
        self.config(text=text, font=("helvetica", 16))
        self.place(x = i, y=30, anchor="center")