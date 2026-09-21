VERSION = [
    {"cancion_id": 13, "version_de_id": 12, "tipo": "live"},
    {"cancion_id": 16, "version_de_id": 61, "tipo": "cover"},
    {"cancion_id": 33, "version_de_id": 32, "tipo": "live"},
    {"cancion_id": 48, "version_de_id": 47, "tipo": "live"},
    {"cancion_id": 52, "version_de_id": 51, "tipo": "remix"},
    {"cancion_id": 62, "version_de_id": 1, "tipo": "live"},
    {"cancion_id": 63, "version_de_id": 19, "tipo": "live"},
    {"cancion_id": 64, "version_de_id": 55, "tipo": "live"},
    {"cancion_id": 65, "version_de_id": 54, "tipo": "live"},
    {"cancion_id": 66, "version_de_id": 31, "tipo": "cover"},
    {"cancion_id": 67, "version_de_id": 37, "tipo": "remix"}
]


class Biblioteca:

    def __init__(self):
        self.versiones = VERSION

    def versiones_directas(self, id_cancion):
        resultado = []

        for version in self.versiones:
            if version["version_de_id"] == id_cancion:
                resultado.append(version)

        return resultado

    def versiones_de(self, id_cancion):

        directas = self.versiones_directas(id_cancion)

        if not directas:
            return []

        resultado = list(directas)

        for version in directas:
            resultado += self.versiones_de(
                version["cancion_id"]
            )

        return resultado
"""
#prueba con el factorial
    def factorial(x):
        if x == 1:
            return 1
        return x * Biblioteca.factorial(x - 1)

"""
