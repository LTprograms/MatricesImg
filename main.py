from screen.Screen import Screen
from obj.Matrix import Matrix
import numpy as np

np.set_printoptions(threshold=np.inf)
rt = Screen()
matrix = Matrix("./img/papagayo.png")
rt.setImage(matrix)
rt.printMatrix()
rt.mainloop()