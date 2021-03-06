#Instalar: pip install pandas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.distutils.system_info import dfftw_info


class analis_datos:
    #la funcion recibe el valor al que se quiere encotrar el ranking
    def __init__(self):
        #Hacemos un dataframe
        self.df =  pd.read_csv("../Respaldo_db/csv/cancion123458completo.csv", index_col=False)
        #Filtamos los datos, para eliminar los posibles valores nulos
        self.df_filtrado = self.df.fillna({"ranking": 0, "cancion": "", "artista": "", "pais": "", "data": ""})
    def artistas(self):
        dataArtistas = self.df_filtrado.groupby("artista").mean()
        #print(dataArtistas)
        dataArtistas=dataArtistas.reset_index()
        dataArtistas = dataArtistas[["artista"]]
        dataArtistas = pd.DataFrame(dataArtistas)
        #print(dataArtistas)
        arr = dataArtistas.to_numpy()
        nuevo =[]
        for x in range(arr.size):
            if arr[x][0]!="":
                nuevo.append(arr[x][0])
        #print(arr.size)
        return nuevo
    #Ver que el nombre del artista tentanga estadistica
    def paises(self):
        dataPaises = self.df_filtrado.groupby("pais").mean()
        #print(dataPaises)
        dataPaises = dataPaises.reset_index()
        dataPaises = dataPaises[["pais"]]
        dataPaises = pd.DataFrame(dataPaises)
        arr = dataPaises.to_numpy()
        nuevo=[]
        for x in range(arr.size):
            if arr[x][0]!="":
                nuevo.append(arr[x][0])
        nuevo.append("Todos")
        return  nuevo


        #return dataArtistas
    def claveApais(self,pais):
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
            pais = "Espa??a"
        elif pais == "cl":
            pais = "Chile"
        else:
            pais = "Todos los paises"
        return pais
    def paisAclave(self,pais):
        if pais == "Mexico":
            pais = "mx"
            #ec
        elif pais == "Ecuador":
            pais = "ec"
            #pa
        elif pais == "Panamo":
            pais = "pa"
            #co
        elif pais == "Colombia":
            pais = "co"
            #hn
        elif pais == "Honduras":
            pais = "hn"
            #ar
        elif pais == "Argentina":
            pais = "ar"
            #gt
        elif pais == "Guatemala":
            pais = "gt"
            #cr
        elif pais == "Costa Rica":
            pais = "cr"
            #do
        elif pais == "Republica Dominicana":
            pais = "do"
            #es
        elif pais == "Espa??a":
            pais = "es"
        #cl
        elif pais == "Chile":
            pais = "cl"
        else:
            pais = "Todos los paises"
        return pais

    #el pais tiene que ser la clave como esta en la lista de main
    def ranking10_2017_2021PorPais(self,pais,valor):
        #obtenemos solo los registros que tengan el pais que recibimos
        if pais !="Todos":
            df_filtrado = self.df_filtrado[self.df_filtrado["pais"] == pais]
        else:
            df_filtrado = self.df_filtrado
        #Agrupamos
        df_agrupado = df_filtrado.groupby(valor).mean()
        # Dejamos en el dataframe los artista que esta solo en el top 10
        df_agrupado2 = df_agrupado[df_agrupado["ranking"] <= 10]
        # Hacemos una grafica de barras horizontal. si quiere una grafica de barras vertical poner solo bar
        df_agrupado2["ranking"].plot(kind="barh")
       #Utilizamos esta funcion para convertir la clave del pais en el nombre completo
        pais = self.claveApais(pais)
        # Agragamos el titulo
        plt.title("Ranking 10: del 2017 al 2021 "+pais)
        # Agregamos titulo de x
        plt.xlabel("Ranking")
        # Agregamos titulo de y
        plt.ylabel(valor)
        # Pintamos
        plt.show()
        #print(df_filtrado)
        #valor puede ser una cancion ?? un artista
    #El valor se refiere ya sea reporducciones por canciones o por artistas
    #Grafica de barras entre todos los paises
    def Reproducciones2017_2021(self,valor,pais):
        if pais != "Todos":
            df_filtrado = self.df_filtrado[self.df_filtrado["pais"] == pais]
            df_agrupado = df_filtrado.groupby(valor).mean()
            pais = self.claveApais(pais)
        else:
            df_agrupado = self.df_filtrado.groupby(valor).mean()
            pais = "Todos los paises"
        # Dejamos en el dataframe los artista que esta solo en el top 10
        df_agrupado2 = df_agrupado[df_agrupado["ranking"] <= 10]
        df_agrupado2 = df_agrupado2[["reproducciones:"]]
        df_agrupado2["reproducciones:"].plot(kind="barh")
        destinado =""
        plt.title("Reproducciones Top 10 {}: 2017 al 2021".format(pais))
        plt.show()
    def Reproducciones_por_artista20172021(self,artista,pais):
        if pais!="Todos":
            #Filtramos por los registros que tengan solo al artista y al pais que queresmo
             df_filtrado = self.df_filtrado[(self.df_filtrado["artista"]==artista) & (self.df_filtrado["pais"]==pais)]
             print(df_filtrado)
             #Dejamos en el dataframe la fecha y las  reproduccioenes
             df_filtrado = df_filtrado[["fecha","reproducciones:"]]

             #Ploteamos los valores
             plt.plot(df_filtrado["fecha"], df_filtrado["reproducciones:"])
             print(df_filtrado)
        else:
            df_filtrado = self.df_filtrado[self.df_filtrado["artista"] == artista]
            print(df_filtrado)
            df_filtrado = df_filtrado[["fecha", "reproducciones:"]]
            print(df_filtrado)
            df_filtrado=df_filtrado.groupby("fecha").mean()
            print(df_filtrado)
            df_filtrado["reproducciones:"].plot()

        pais = self.claveApais(pais)
        plt.title("Reproducciones de {} en {}".format(artista,pais))
        plt.xticks(rotation=45)
        plt.show()





#analisis = analis_datos()
#analisis.ranking10_2017_2021("cancion")
#analisis.ranking10_2017_2021PorPais("ar","artista")
#analisis.Reproducciones2017_2021("artista","")
#analisis.Reproducciones_por_artista20172021("Ricky Martin","co")a
#analisis.artistas()
#analisis.paises()
#analisis.comprobarEstadisticaReproduccioens("")