## Este es un Diccionario de datos desarrollado en Python, con el modelo Cliente-Servidor utilizando Pyro, en entorno Linux dis. Ubuntu.

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

### Esta es una aplicacion cliente servidor utilizando llamadas a métodos remotos (Pyro) utilizando python.

### Descripción del proyecto:

El proyecto "Diccionario Cliente-Servidor con Pyro" es una aplicación cliente-servidor funcional que permite a los usuarios realizar consultas sobre el significado de palabras almacenadas en un diccionario. El servidor proporciona acceso a un diccionario que se carga desde un archivo de texto, y los clientes pueden realizar consultas sobre el significado de palabras específicas, así como agregar nuevas palabras al diccionario.

- El servidor deberá estar siempre disponible y permitirá conexiones de múltiples  clientes.

- El cliente envía una petición con una palabra cuyo significado será devuelto por el programa sevidor. En caso de que el servidor no encuentre la palabra, permitirá la opción de que esta palabra y su significado sea agregado al diccionario.

- El archivo diccionario.txt, (que se encuentra en el repositorio), será el diccionario a utilizar en la aplicación. este archivo será cargado en memoria por servidor para la ejecución de las consultas.   Se agregarán nuevas entradas al archivo cuando el cliente las propocione a fin de que estos cambios estén disponibles para una nueva ejecución.


### Guia general.

1. Instalación de Pyro:
   - Hay que tener instalado pyro.
3. Diseño del Servidor:
   - Crea una clase DiccionarioServer que implemente la funcionalidad del servidor. Esta clase debe contener métodos para buscar y agregar palabras al diccionario.
5. Diseño del Cliente:
   - Crea un cliente que se conecte al servidor y realice las operaciones necesarias.
4. Archivo de texto plano, datos.txt.
   - Este archiivo es el que va a actuar como el diccionario de datos, que cuaenta con al menos 800 palabras.

### Código del Servidor utilizando Pyro:

1. Inicialización del Servidor:
   - @Pyro4.expose: Esto es un decorador que indica que la clase.
   - DiccionarioServer debe exponer sus métodos para que sean accesibles a         través de Pyro (Python Remote Objects).
   - __init__(self): El método de inicialización del servidor. Aquí se carga el diccionario desde un archivo llamado 'datos.txt' y se almacena en self.diccionario.
   - self.diccionario: Una lista que contiene líneas del archivo 'datos.txt'. Cada línea representa una entrada en el diccionario y está formateada como "palabra|significado".

![1](https://github.com/edSoto02/Diccionario-de-Datos/assets/106222946/6b069b3e-9655-4650-811c-f03604d9405a)


2. Método buscar_significado:
    - buscar_significado(self, palabra): Este método toma una palabra como argumento y busca su significado en el diccionario.
    - print(f"Solicitud de búsqueda para la palabra: {palabra}"): Imprime un mensaje indicando que se está buscando el significado de una palabra específica.
    - for linea in self.diccionario: Itera sobre cada línea en el diccionario.
    - partes = linea.split('|'): Divide cada línea en dos partes usando el carácter '|' como separador.
    - palabra_dicc, significado_dicc = partes: Desempaqueta las dos partes (palabra y significado) de la línea.
    - if palabra.lower() == palabra_dicc.lower():: Compara la palabra proporcionada (en minúsculas) con la palabra en el diccionario (también en minúsculas).
    - return significado_dicc: Si encuentra la palabra, devuelve su significado.
    - return "Palabra no encontrada en el diccionario.": Si no encuentra la palabra, devuelve un mensaje indicando que la palabra no está en el diccionario.

![2](https://github.com/edSoto02/Diccionario-de-Datos/assets/106222946/055bc6de-52f0-4182-a979-84ee562ea14a)


3. Método agregar_palabra:
    - agregar_palabra(self, palabra, significado): Este método toma una palabra y su significado y los agrega al diccionario.
    - with open('datos.txt', 'a') as archivo: archivo.write(f'{palabra}:{significado}\n'): Abre el archivo 'datos.txt' en modo de apertura (append) y escribe la nueva entrada en el formato "palabra:significado".
    - except FileNotFoundError: print("Error: El archivo Diccionario de datos no se encuentra en la ruta especificada."): Captura la excepción si el archivo 'datos.txt' no se encuentra y imprime un mensaje de error.

![3](https://github.com/edSoto02/Diccionario-de-Datos/assets/106222946/f989f175-257d-4567-a6db-b305ca71a124)


4. Método main:
   - main(): La función principal que inicia el servidor Pyro.
   - daemon = Pyro4.Daemon(): Crea una instancia del demonio Pyro que manejará las conexiones remotas.
   - ns = Pyro4.locateNS(): Localiza el servicio de nombres de Pyro.
   - uri = daemon.register(DiccionarioServer): Registra la instancia de DiccionarioServer en el demonio y obtiene un identificador único (URI) para ella.
   - ns.register("diccionario_server", uri): Registra el URI en el servicio de nombres con el nombre "diccionario_server".
   - daemon.requestLoop(): Inicia el bucle de solicitud del demonio, lo que permite que el servidor Pyro espere conexiones remotas.
   - if __name__ == "__main__": main(): Si el script se ejecuta como el programa principal, llama a la función main().

![4](https://github.com/edSoto02/Diccionario-de-Datos/assets/106222946/d82564de-a2d7-443e-b566-a8434974796b)


### Código del Cliente utilizando Pyro:

1. Importación de Pyro4:
   - import Pyro4: Importa el módulo Pyro4, que se utiliza para la implementación de objetos remotos en Python.
2. Función Principal main:
   - def main():: Define la función principal del cliente.
3. Conexión al Servidor Pyro:
   - with Pyro4.Proxy("PYRONAME:diccionario_server") as server::
    Crea una conexión al servidor remoto Pyro utilizando el nombre registrado "diccionario_server" en el servicio de nombres Pyro.
4. Bucle Principal del Cliente:
   - while True:: Inicia un bucle infinito para permitir que el cliente realice múltiples consultas al servidor.
   - palabra = input("Ingrese una palabra (o 'salir' para salir): "): Solicita al usuario que ingrese una palabra o escriba "salir" para salir del programa.
   - if palabra.lower() == "salir": break: Verifica si el usuario desea salir del programa y rompe el bucle si es así.
   - significado = server.buscar_significado(palabra): Llama al método remoto buscar_significado del servidor Pyro para obtener el significado de la palabra ingresada
   - print(significado): Imprime el significado obtenido, ya sea el significado real o el mensaje "Palabra no encontrada en el diccionario."
   - if significado == "Palabra no encontrada en el diccionario.":: Verifica si la palabra no se encontró en el diccionario.

     - agregar_nueva = input("¿Desea agregar esta palabra al diccionario? (s/n): "): Pregunta al usuario si desea agregar la palabra al diccionario.
     - if agregar_nueva.lower() == "s":: Verifica si el usuario desea agregar la palabra.
     -   nuevo_significado = input(f"Ingrese el significado de {palabra}: "): Solicita al usuario que ingrese el significado de la nueva palabra.
     - server.agregar_palabra(palabra, nuevo_significado): Llama al método remoto agregar_palabra del servidor Pyro para agregar la nueva palabra al diccionario con su significado.
     -  print(f"Palabra {palabra} agregada al diccionario."): Imprime un mensaje indicando que la palabra ha sido agregada al diccionario.

5. Entrada Principal del Programa:
    - if __name__ == "__main__": main(): Verifica si el script se está ejecutando como el programa principal y, en ese caso, llama a la función principal main().


![5](https://github.com/edSoto02/Diccionario-de-Datos/assets/106222946/e98b5352-739c-467a-810d-1eba478e276b)


### Ejecución del Servidor y Cliente:

1. Lanzamos Pyro

![Captura desde 2024-02-05 14-10-22](https://github.com/edSoto02/Diccionario-de-Datos/assets/106222946/fcdadf14-3aa7-47af-a7dc-99b640d617c2)

2. Ejecutamos el Servidor.
   - El servidor nos mostrara un mensaje de que se estan espreando conexiones.
   - De igual manera, el Servidor nos va mostrando en fomra de lista la solicitud de las palabras de las cuales se desea saber su significado.

![Captura desde 2024-02-05 13-58-17](https://github.com/edSoto02/Diccionario-de-Datos/assets/106222946/c7b2afbd-526f-4521-9268-8298227bf610)

3. Ejecutamos el Cliente
   - El cliente nos mostrara un mensaje en consola que ingresemos la palabra a buscar o escribir salir, para salir del cliente.
   - Si la palabra se encuentra en el diccionario, nos mostrara el significado.

![Captura desde 2024-02-05 13-57-02](https://github.com/edSoto02/Diccionario-de-Datos/assets/106222946/9232196b-ac90-44ac-990b-2e8871e71766)

![Captura desde 2024-02-05 13-57-25](https://github.com/edSoto02/Diccionario-de-Datos/assets/106222946/127adaf5-be20-41a6-ba14-d3994c52d4b1)

![Captura desde 2024-02-05 13-57-39](https://github.com/edSoto02/Diccionario-de-Datos/assets/106222946/6d66a69e-1181-4fb3-8a8c-0f6c29650d78)

4. Agregamos palabras que no estan en el Diccionario.
   - En este punto solicitamos palabras que no se encuentran eb el diccionario de datos.
   - Desde la terminal del cliente agregamos la palabra y su significado al diccionario.

![Captura desde 2024-02-05 14-05-27](https://github.com/edSoto02/Diccionario-de-Datos/assets/106222946/7eeb3c58-7133-417e-bb38-a7ca0d44138c)

5. Acutalizamos el archivo txt, y verificamos que se guardaron las nuevas palabras.
   - En el archivo txt. verificamos que las palabras nuevas si se agregaron al diccionario.
   - Las palabras se agregan el final de la lista.

![Captura desde 2024-02-05 14-05-06](https://github.com/edSoto02/Diccionario-de-Datos/assets/106222946/b0f2843e-fc7d-4a52-8a06-913efdc46404)


### Cómo Utilizar el Proyecto:

1. Clonar el Repositorio:
   - Clone el repositorio del proyecto desde GitHub a su máquina local utilizando el comando git clone.

2. Instalar Dependencias:
   - Asegúrese de tener Pyro instalado en su entorno de desarrollo. Puede instalarlo usando pip con el comando pip install Pyro4.

3. Configurar el Servidor:
   - Configure el servidor para que cargue el diccionario desde un archivo de texto. Asegúrese de que el archivo de diccionario tenga el formato adecuado (por ejemplo, 
     "palabra|significado" en cada línea).

4. Iniciar el Servidor:
   - Ejecute el script del servidor (servidor.py). Esto iniciará el servidor Pyro y lo registrará en el servicio de nombres.

5. Conectar y Utilizar el Cliente:
   - Ejecute el script del cliente (cliente.py). Esto iniciará el cliente y lo conectará al servidor Pyro. Desde el cliente, podrá realizar consultas sobre el significado de palabras y 
     agregar nuevas palabras al diccionario según sea necesario.




<p align="center">
   <img src="https://img.shields.io/badge/STATUS-%20COMPLETO-green">
</p>
