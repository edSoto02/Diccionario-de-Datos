import Pyro4

def main():
    with Pyro4.Proxy("PYRONAME:diccionario_server") as server:
        while True:
            palabra = input("Ingrese una palabra (o 'salir' para salir): ")
            
            if palabra.lower() == "salir":
                break

            significado = server.buscar_significado(palabra)
            print(significado)

            if significado == "Palabra no encontrada en el diccionario.":
                agregar_nueva = input("¿Desea agregar esta palabra al diccionario? (s/n): ")

                if agregar_nueva.lower() == "s":
                    nuevo_significado = input(f"Ingrese el significado de {palabra}: ")
                    server.agregar_palabra(palabra, nuevo_significado)
                    print(f"Palabra {palabra} agregada al diccionario.")

if __name__ == "__main__":
    main()