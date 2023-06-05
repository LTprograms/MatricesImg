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
        """Sets the 2 frames of the app"""
        w, h = self.getSize()

        self.__fr1 = tk.Frame(self)
        self.__fr2 = tk.Frame(self)

        self.__fr1.config(width=(w*3)//5, height=h)
        self.__fr2.config(width=(w*2)//5, height=h)
        
        self.__fr1.config(bg="black")
        self.__fr2.config(bg="green")

        self.__fr1.place(x=0, y=0)
        self.__fr2.place(x=(w*3)//5, y=0)
    
    def setImage(self, img:Matrix) -> None:
        """Sets the image to display in the app"""
        w, h = self.getSize()
        img.resize((w*2)//5, h)
        self.__photo = ImageTk.PhotoImage(img.getImg())

        for child in self.__fr2.winfo_children():
            child.destroy()
        
        lb = tk.Label(self.__fr2, image=self.__photo)
        lb.place(x=(w)//5, y=h//2, anchor="center")

    def __setTextArea(self) -> None:
        """Sets the text area where it is going to display the Matrix"""
        self.__txt = tk.Text(self.__fr1)
        w, h = self.getSize()
        self.__txt.config(font=("helvetica", 16))
        # self.__txt.config(width=(w*3)//5, height=(h*4)//5)
        self.__txt.place(x=0, y=0)

    def __setControls(self) -> None:
        """Sets the controls frame"""
        w, h = self.getSize()
        self.__controls = tk.Frame(self.__fr1)
        self.__controls.config(width=(w*3)//2, height=h//5, bg="green")
        self.__controls.place(x=0, y=h, anchor="sw")

    def printMatrix(self, array:list) -> None:
        CONST = 200
        count = CONST
        start = 0
        end = CONST
        for rgb in array:
            string = str(array[start:end])
            string = string[1:-2]
            string = string.replace("), (", ")\t\t(")
            self.__txt.insert("end",string+"\n")
            start = end
            end += CONST
            count+=CONST
            if count>=len(array):
                end = -1

            
