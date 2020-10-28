import numpy as np

# importar libreria:       figura, archivo de salida, mostrar grafica  
from bokeh.plotting import figure, output_file, show

#Calidad de formas
N = 1000
x = np.linspace(0, 10, N)
y = np.linspace(0, 10, N)
xx, yy = np.meshgrid(x, y)
d = np.sin(xx)*np.cos(yy)

p = figure(tooltips=[("x", "$x"), ("y", "$y"), ("value", "@image")])
p.x_range.range_padding = p.y_range.range_padding = 0

# parámetros  para el vector
p.image(image=[d], x=0, y=0, dw=10, dh=10, palette="Spectral11", level="image")
p.grid.grid_line_width = 0.5

output_file("grafica_numpy.html", title="grafica_numpy.py example")

show(p)