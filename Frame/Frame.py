import tkinter as tk
from tkinter import ttk
from AnalisisDatos.analisis_panda import *
from pandastable import Table
#inatalar: pip install pandastable
analisis = analis_datos()
def ReproduccionPromedio(artista,pais):
    analisis.Reproducciones_por_artista20172021(artista,pais)

def ReproduccionPromedio2(valor,pais):
    analisis.Reproducciones2017_2021(valor,pais)

def RankingPromedio(pais,valor):
    analisis.ranking10_2017_2021PorPais(pais,valor)

def crearNuevaVentana():
    newWindow = tk.Toplevel(ventana)
    table = Table(newWindow, dataframe=analisis.df_filtrado,
        showtoolbar=False,
        showstatusbar=True,
        editable=False)
    table.show()




ventana = tk.Tk()
ventana.geometry("500x300")
ventana.title("Analisis Spotify")

#Labels
labelListaArtista = tk.Label(ventana,text="Lista de artistas").place(x=30,y=30)
labelListaArtista2 = tk.Label(ventana,text="Lista paises").place(x=200,y=30)
labelListaReproducciones = tk.Label(ventana,text="Opciones Promedio").place(x=30,y=120)
labelListaReproducciones2 = tk.Label(ventana,text="Lista Paises").place(x=200,y=120)
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
botonAnalisis_rep = tk.Button(ventana,text="Reproducciones promedio", command= lambda: ReproduccionPromedio(lista_desplegable.get(),lista_desplegable2.get())).place(x=30,y=80)

lista_desplegable3 = ttk.Combobox(ventana,width=20)
lista_desplegable3.place(x=30,y=140)
opciones = ["artista","cancion"]
lista_desplegable3["values"] = opciones
lista_desplegable3.current(0)

lista_desplegable4 = ttk.Combobox(ventana,width=20)
lista_desplegable4.place(x=200,y=140)
lista_desplegable4["values"] = analisis.paises()
lista_desplegable4.current(11)

botonAnalisis_rep2 = tk.Button(ventana,text="Reproducciones promedio", command= lambda: ReproduccionPromedio2(lista_desplegable3.get(),lista_desplegable4.get())).place(x=30,y=170)

lista_desplegable5 = ttk.Combobox(ventana,width=20)
lista_desplegable5.place(x=30,y=210)
lista_desplegable5["values"] = opciones
lista_desplegable5.current(0)

lista_desplegable6 = ttk.Combobox(ventana,width=20)
lista_desplegable6.place(x=200,y=210)
lista_desplegable6["values"] = analisis.paises()
lista_desplegable6.current(11)

botonAnalisis_rep3 = tk.Button(ventana,text="Ranking promedio", command= lambda: RankingPromedio(lista_desplegable6.get(),lista_desplegable5.get())).place(x=30,y=240)

BotonDataFrame = tk.Button(ventana,text="Data Frame", command= crearNuevaVentana).place(x=400,y=50)

ventana.mainloop()