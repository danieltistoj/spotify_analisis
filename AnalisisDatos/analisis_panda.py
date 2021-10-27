#Instalar: pip install pandas
import pandas as pd
import matplotlib.pyplot as plt
from numpy.distutils.system_info import dfftw_info


class analis_datos:
    #la funcion recibe el valor al que se quiere encotrar el ranking
    def __init__(self):
        #Hacemos un dataframe
        self.df =  pd.read_csv("../Respaldo_db/csv/cancion123458completo.csv", index_col=False)
        #Filtamos los datos, para eliminar los posibles valores nulos
        self.df_filtrado = self.df.fillna({"ranking": 0, "cancion": "", "artista": "", "pais": "", "data": ""})
    def ranking10_2017_2021(self,valor):
        #Agrupamos por artista y hacemos un promedio del ranking por artista
        df_agrupado = self.df_filtrado.groupby(valor).mean()
        #Dejamos en el dataframe los artista que esta solo en el top 10
        df_agrupado2 = df_agrupado[df_agrupado["ranking"] <= 10]
        #print(df_agrupado2)
       #Hacemos una grafica de barras horizontal. si quiere una grafica de barras vertical poner solo bar
        df_agrupado2["ranking"].plot(kind="barh")
        #Agragamos el titulo
        plt.title("Ranking 10: del 2017 al 2021")
        #Agregamos titulo de x
        plt.xlabel("Ranking")
        #Agregamos titulo de y
        plt.ylabel(valor)
        #Pintamos
        plt.show()
    #el pais tiene que ser la clave como esta en la lista de main
    def ranking10_2017_2021PorPais(self,pais,valor):
        #obtenemos solo los registros que tengan el pais que recibimos
        df_filtrado = self.df_filtrado[self.df_filtrado["pais"]==pais]
        #Agrupamos
        df_agrupado = df_filtrado.groupby(valor).mean()
        # Dejamos en el dataframe los artista que esta solo en el top 10
        df_agrupado2 = df_agrupado[df_agrupado["ranking"] <= 10]
        # Hacemos una grafica de barras horizontal. si quiere una grafica de barras vertical poner solo bar
        df_agrupado2["ranking"].plot(kind="barh")
        # Agragamos el titulo
        if pais == "mx":
            pais = "Mexico"
        elif pais == "ec":
            pais = "Ecuador"
        elif pais == "pa":
            pais = "Panama"
        elif pais == "co":
            pais = "Colombia"
        elif pais == "hn":
            pais = "Honduras"
        elif pais == "ar":
            pais = "Argentina"
        elif pais == "gt":
            pais = "Guatemala"
        elif pais == "cr":
            pais = "Costa Rica"
        elif pais == "do":
            pais = "Republica Dominicana"
        elif pais == "es":
            pais = "España"
        elif pais == "cl":
            pais = "Chile"

        plt.title("Ranking 10: del 2017 al 2021 "+pais)
        # Agregamos titulo de x
        plt.xlabel("Ranking")
        # Agregamos titulo de y
        plt.ylabel(valor)
        # Pintamos
        plt.show()
        #print(df_filtrado)
        #valor puede ser una cancion ó un artista
    #El valor se refiere al
    def Reproducciones2017_2021(self,valor):
        df_agrupado = self.df_filtrado.groupby(valor).mean()
        # Dejamos en el dataframe los artista que esta solo en el top 10
        df_agrupado2 = df_agrupado[df_agrupado["ranking"] <= 10]




analisis = analis_datos()
analisis.ranking10_2017_2021("cancion")
#analisis.ranking10_2017_2021PorPais("ar","artista")
#analisis.rendimientoDeRanking2017_2021("Ricky Martin")
