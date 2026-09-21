from src.config import TEMA
from src.dominio.cancion  import CATALOGO, Cancion
from src.dominio.biblioteca  import VERSION, Biblioteca





TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "1":
            Cancion.listar_catalogo()

        if opcion == "5":
            biblioteca = Biblioteca()

            id_cancion = 1 #prueba con la id 1

            resultado = biblioteca.versiones_de(id_cancion)

            for version in resultado:
                print(
                    "Versión ID:",
                    version["cancion_id"],
                    "- Tipo:",
                    version["tipo"]
                )
                
        elif opcion == "0":
            print("Chau.")
        elif opcion in { "2", "3", "4", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
