#Instalar: pip install pandas
import pandas as pd
import matplotlib.pyplot as plt
#1.OBTENER LOS DATOS EN CRUDO-----------
df = pd.read_csv("Respaldo_db\\csv\\cancion123459data.csv",index_col="_id")
#Limpieza de datos nulos. Elimina las filas que contengan al menos un dato nulo
#df_filtrado = df.dropna()
#2.FILTRAR LOS DATOS -----------
#filtro de datos, colocando otro valor, en los que esten como nulos
df_filtrado = df.fillna({"ranking":0,"nombre":"","artista":"","pais":"","data":""})
#df_filtrado.head()
#Pata mostrar una columna en especifico
#print(df_filtrado["data"])
#print(df_filtrado.head())
#Devuelve la primera fila, pero en formato de columna
#agrupa por un promedio de las filas con numeros
df_agrupado=df_filtrado.groupby("artista").mean()
#print(df_agrupado)
df_agrupado2 = df_agrupado[df_agrupado["ranking"]<10]
print(df_agrupado2)
df_agrupado2["ranking"].plot(kind="bar")


plt.show()