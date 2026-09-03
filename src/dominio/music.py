CATALOGO = [
    {"id": 51, "titulo": "Billie Jean", "artista": "Michael Jackson", "album" : "Thriller" , "anio" : 1982 , "genero" : "Pop", "duracion_seg" : 294},
    {"id": 1, "titulo": "De Musica Ligera", "artista": "Soda Stereo", "album" : "Cancio Animal" , "anio" : 1990 ,"genero" : "Rock", "duracion_seg" : 213},
    {"id": 50, "titulo": "Africa", "artista": "Toto", "album" : "Toto IV" , "anio" : 1982 , "genero" : "Pop" , "duracion_seg" : 296 },
]

def listar_catalogo():
    for item in CATALOGO:
        print(f"{item['id']:>3}  {item['titulo']} {item['artista']} {item['album']} {item['anio']}")