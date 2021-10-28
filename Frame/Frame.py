from tkinter import *
from tkinter import ttk
from AnalisisDatos.analisis_panda import *
analisis = analis_datos()
def ReproduccionPromedio(artista,pais):
    analisis.Reproducciones_por_artista20172021(artista,pais)


ventana = Tk()
ventana.geometry("500x300")
ventana.title("Analisis Spotify")

#Labels
labelListaArtista = Label(ventana,text="Lista de artistas").place(x=30,y=30)
labelListaArtista2 = Label(ventana,text="Lista paises").place(x=200,y=30)
#ComboBox
lista_desplegable = ttk.Combobox(ventana,width=20)
lista_desplegable.place(x=30,y=50)
lista_desplegable["values"] = analisis.artistas()
lista_desplegable.current(0)
lista_desplegable2 = ttk.Combobox(ventana,width=20)
lista_desplegable2.place(x=200,y=50)
lista_desplegable2["values"] = analisis.paises()
lista_desplegable2.current(11)
#Botones
botonAnalisis_rep = Button(ventana,text="Reproducciones promedio", command= lambda: ReproduccionPromedio(lista_desplegable.get(),lista_desplegable2.get())).place(x=30,y=80)


ventana.mainloop()