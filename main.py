from screen.Screen import Screen
from obj.Matrix import Matrix

rt = Screen("cyborg")
matrix = Matrix("./img/papagayo.png")
rt.set_image(matrix)
rt.print_matrix()

rt.mainloop()

