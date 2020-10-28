# importar libreria:       figura, archivo de salida, mostrar grafica     
from bokeh.plotting import figure, output_file, show

if __name__=='__main__':
    output_file('graficado_simple.html')
    fig= figure()
    
    total_vals=int(input('¿Cuántos valores quieres graficar? ' ))
    #generar valores de x, mediante una lista
    x_vals= list(range(total_vals))
    y_vals=[]

    for x in x_vals:
        val= int(input(f'Ingrese el valor de y,  para x= {x} : '))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=5, line_color='pink')
    show(fig)

