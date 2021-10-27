
class Cancion:
    def __init__(self,
                 ranking: int,
                 name: str,
                 author: str,
                 date: str,
                 country: str,
                 reproducciones: int):
        self.ranking = ranking
        self.name = name
        self.author = author
        self.date = date
        self.country = country
        self.reproducciones = reproducciones