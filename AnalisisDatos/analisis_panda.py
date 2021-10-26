#Instalar: pip install pandas
import pandas as pd
import matplotlib.pyplot as plt
class analis_datos:
    def ranking10Artistas2017_2021(self):
        #Hacemo el dataframe
        df = pd.read_csv("../Respaldo_db/csv/cancion123459data.csv", index_col="_id")
        #Filtamos los datos, para eliminar los posibles valores nulos
        df_filtrado = df.fillna({"ranking": 0, "nombre": "", "artista": "", "pais": "", "data": ""})
        #Agrupamos por artista y hacemos un promedio del ranking por artista
        df_agrupado = df_filtrado.groupby("artista").mean()
        #Dejamos en el dataframe los artista que esta solo en el top 10
        df_agrupado2 = df_agrupado[df_agrupado["ranking"] <= 10]
       #Hacemos una grafica de barras horizontal. si quiere una grafica de barras vertical poner solo bar
        df_agrupado2["ranking"].plot(kind="barh")
        #Agragamos el titulo
        plt.title("Ranking 10: del 2017 al 2021")
        #Agregamos titulo de x
        plt.xlabel("Ranking")
        #Agregamos titulo de y
        plt.ylabel("Artistas")
        #Pintamos
        plt.show()
analisis = analis_datos()
analisis.ranking10Artistas2017_2021()
