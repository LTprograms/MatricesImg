import tkinter as tk
from PIL import ImageTk
from obj.Matrix import Matrix
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

class Screen(ttkb.Window):
    def __init__(self, themename):
        super().__init__(themename=themename)
        self.title("Array Images")
        self.__w, self.__h = self.winfo_screenwidth(), self.winfo_screenheight()
        ttkb.Label(self, text="Array Manipulation", font=("helvetica", 20)
                   , bootstyle=(INFO)).pack(side=TOP)
        self.__set_columns()
        self.__set_controls()
        self.__set_text_area()

    def __set_columns(self) -> None:
        """Sets the 2 main frames of the app"""
        fr = ttkb.Frame(self)
        self.__fr1 = ttkb.Frame(fr)
        self.__fr2 = ttkb.Frame(fr)
        
        self.__fr1.pack(fill=BOTH, expand=True, side=LEFT)
        
        self.__fr2.pack(fill=X, side=RIGHT)

        fr.pack(fill=BOTH, expand=True)

    def set_image(self, matrix:Matrix) -> None:
        """Sets the image to display in the app"""
        self.__matrix = matrix
        self.__photo = ImageTk.PhotoImage(matrix.get_img())

        for child in self.__fr2.winfo_children():
            child.destroy()
        
        lb = ttkb.Label(self.__fr2, image=self.__photo)
        lb.pack(padx=30, pady=30)
    
    
    def __set_text_area(self) -> None:
        """Sets the text area where it is going to display the Matrix"""
        cv = ttkb.Canvas(self.__fr1)
        cv.pack(fill=BOTH, expand=True)
        self.__txt = ttkb.Text(cv)
        self.__txt.config(font=("helvetica", 16))
        self.__txt.pack(fill=BOTH, side="left", expand=True)  

    def __set_controls(self) -> None:
        """Sets the controls frame"""
        self.__controls = ttkb.Frame(self)
        self.__controls.pack(side=BOTTOM)

        self.__grayBtn = AppButton(self.__controls, "Gray Scale", 1, (SUCCESS))
        self.__grayBtn.config(command=lambda:self.transform_img(1))
        self.__invBtn = AppButton(self.__controls, "Invert", 2, (DANGER))
        self.__invBtn.config(command=lambda:self.transform_img(2))
        self.__rotBtn = AppButton(self.__controls, "Rotate", 3, (INFO))
        self.__rotBtn.config(command=lambda:self.transform_img(3))
        self.__brightBtn = AppButton(self.__controls, "Brightness", 4, (WARNING))
        self.__brightBtn.config(command=lambda:self.transform_img(4))  
    def print_matrix(self) -> None:
        """Prints the matrix to TextField"""
        string = self.__matrix.get_reduced_matrix()
        self.__txt.delete("1.0", "end")
        size = 5
        for i in range(0, len(string), size):
            chunk = string[i:i + size]
    
            for item in chunk:
                self.__txt.insert("end", str(item).replace("], [", "]\t\t[")+"\n") 

    def transform_img(self, num:int) -> None:
        """
        Transform the RGB matrix depending of the num constant:\n
        * 1: Gray scale\n
        * 2: Invert image\n
        * 3: Rotate image\n
        * 4: Change brightness\n
        """
        match num:
            case 1:
                self.__matrix.gray_scale()
            case 2:
                self.__matrix.invert()
            case 3:
                self.__matrix.rotate()
            case 4:
                self.__matrix.bright()
        self.__matrix.set_image()
        self.set_image(self.__matrix)
        self.print_matrix()   
           
class AppButton(ttkb.Button):
    def __init__(self, master, text, i, style):
        super().__init__(master)
        self.config(text=text, bootstyle=style, width=30)
        self.grid(row=0, column=i, padx=40, pady=40, ipady=10)