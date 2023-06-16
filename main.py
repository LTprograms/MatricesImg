from screen.Screen import Screen
from obj.Matrix import Matrix

rt = Screen()
matrix = Matrix("./img/papagayo.png")
rt.setImage(matrix)
rt.printMatrix()
rt.mainloop()