from tkinter import *
from tkinter import ttk
from AnalisisDatos.analisis_panda import *
ventana = Tk()
ventana.geometry("500x300")
ventana.title("Analisis Spotify")
analisis = analis_datos()
#Labels
labelListaArtista = Label(ventana,text="Lista de artistas").place(x=30,y=30)
labelListaArtista2 = Label(ventana,text="Lista paises").place(x=200,y=30)
#ComboBox
lista_desplegable = ttk.Combobox(ventana,width=20)
lista_desplegable.place(x=30,y=50)
lista_desplegable["values"] = analisis.artistas()

lista_desplegable2 = ttk.Combobox(ventana,width=20)
lista_desplegable2.place(x=200,y=50)
#lista_desplegable["values"] = analisis.artistas()


ventana.mainloop()