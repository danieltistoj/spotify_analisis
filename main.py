from datetime import *
from typing import Iterator

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Suministro
from Clases.Cancion import Cancion
from Servicios.ServicioCancion import *

baseURL = 'https://spotifycharts.com/regional/'
#listaPaises = ['cl', 'co', 'ar', 'pe', 'pr', 'uy', 've', 'ec', 'pa', 'mx', 'hn', 'gt', 'cr', 'do', 'es']
listaPaises = ['ec', 'pa', 'mx','co', 'hn','ar', 'gt', 'cr', 'do', 'es','cl']

class SpotifyScrapper:
    #Solicitar y obtener las mejores canciones
    def requestAndObtainTopSongs(self, country: str, date: str, driver) -> Iterator[Cancion]:
        driver.get(baseURL + '{}/daily/{}'.format(country, date))
        delay = 20
        try:
            WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'chart-table')))
            generalDetails: BeautifulSoup = BeautifulSoup(driver.page_source, "html.parser")
            songsList = generalDetails.find('table', {'class': 'chart-table'}) \
                            .find_all('tr')[1:]
            return map(
                lambda songRaw: self.parseSong(songRaw, country, date),
                songsList
            )

        except TimeoutException:
            print("Demoro mucho tiempo")
            exit()

    #Analizar cancion
    def parseSong(self, songRaw: BeautifulSoup, country: str, date: str) -> Cancion:
        #Extraemos el nombre del artista
        nameAndArtist = songRaw.find('td', {'class': 'chart-table-track'})
        #Extraemos el nombre de la cancion
        name = nameAndArtist.find('strong').getText() \
            .replace("\"", "") \
            .strip()
        #Extraemos el span del nombre del artista
        artist = nameAndArtist.find('span').getText() \
            .replace("by", "") \
            .replace("\"", "") \
            .strip()
        position = songRaw.find('td', {'class': 'chart-table-position'}).getText()
        reproducciones = songRaw.find('td',{'class':'chart-table-streams'}).getText()
        #Le eliminamos el caracter de coma a las reproducciones, para convertirlo a un entero
        caracter = ","
        #Se le ingresa esto a la clase Cancion
        #print("reproducciones: ",int(reproducciones))
        for x in range(len(caracter)):
            reproducciones = reproducciones.replace(caracter[x], "")
        return Cancion(int(position), name, artist, date, country,int(reproducciones))


if __name__ == '__main__':
    #Definimos un rango de fechas, que parta del año 2019 del 1 del 1 al 2021 al 8 del 1
    #años, mes, dia
    #Obtenemos la fehca actual para indicar el rango
    fecha_actual = datetime.now()
    dateRange = Suministro.generateMonthlyDateRange(date(2017, 1, 1), date(fecha_actual.year,fecha_actual.month,1))
    #Se crea un driver, que es un objeto, que es una libreria de selemiun
    driver = webdriver.Chrome(
        #El driver debe de ser compatible con la version de chrome que se tenga
        #Descargar: https://chromedriver.chromium.org/
        executable_path='Driver\\95\\chromedriver.exe'
    )
    #Esto es instanciar la base de datos
    servicioCancion = ServicioCancionMongoDB()
    #Esto es instanciar la clase que escanea la web
    spotifyScrapper = SpotifyScrapper()
    #leemos la lista de paises
    for country in listaPaises:
        for dateObj in dateRange:
            canciones = list(SpotifyScrapper().requestAndObtainTopSongs(
                country,
                dateObj.strftime("%Y-%m-%d"),
                driver
            ))
            for cancion in canciones:
                servicioCancion.guardar(cancion)