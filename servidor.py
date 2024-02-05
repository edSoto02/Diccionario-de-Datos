import Pyro4

@Pyro4.expose
class DiccionarioServer:
    def __init__(self):        
        with open('datos.txt', 'r') as texto:
            self.diccionario = texto.readlines()

    def buscar_significado(self, palabra):
        print(f"Solicitud de búsqueda para la palabra: {palabra}")
        for linea in self.diccionario:
            partes = linea.split('|')
            if len(partes) == 2:
                palabra_dicc, significado_dicc = partes
                if palabra.lower() == palabra_dicc.lower():
                    return significado_dicc
        return "Palabra no encontrada en el diccionario."

    def agregar_palabra(self, palabra, significado):
        try:
            with open('datos.txt', 'a') as archivo:
                archivo.write(f'{palabra}:{significado}\n')
        except FileNotFoundError:
            print("Error: El archivo Diccionario de datos no se encuentra en la ruta especificada.")

def main():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(DiccionarioServer)
    ns.register("diccionario_server", uri)

    print("Servidor listo. Esperando conexiones...")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
