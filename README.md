# Lab1Cripto - Laboratorio 1 de Criptografía y Seguridad en Redes

Este repositorio contiene los códigos, resultados y análisis de tres actividades realizadas en el laboratorio sobre el tráfico ICMP, utilizando técnicas de cifrado y descifrado de mensajes.

## Actividades Realizadas

### 1. **Cifrado César - Transformación de Frases y Palabras**
En esta actividad, se implementó un sistema de cifrado de mensajes utilizando el cifrado César. El script permite tomar cualquier palabra o frase y cifrarla con un desplazamiento especificado por el usuario.

#### Archivos Relacionados:
- **`cesar.py`**: Script que implementa el cifrado de mensajes utilizando el cifrado César con un desplazamiento específico.

#### Descripción:
El programa toma como entrada una frase o palabra y la cifra utilizando un desplazamiento determinado por el usuario. El código aplica el cifrado César, que desplaza cada letra del texto por una cantidad especificada. Además, el script mantiene los caracteres no alfabéticos (como espacios) sin modificarlos. 

**Importante:** El script toma en cuenta las letras mayúsculas y minúsculas, así como los espacios, pero **no cifra números ni caracteres especiales**. Estos se mantienen tal como están en el mensaje original.

Este código fue utilizado para cifrar el mensaje que posteriormente se enviará a través de un ping a una red externa.

#### Instrucciones de Ejecución:
1. Asegúrate de tener Python 3 instalado en tu máquina.
2. Abre una terminal en el directorio donde se encuentra el archivo `cesar.py`.
3. Ejecuta el script con el siguiente comando:
   
   ```bash
   python3 cesar.py
   
Nota: Si al ejecutar el comando python en lugar de python3 obtienes un error como el siguiente:

```bash
zsh: command not found: python
```
Asegúrate de usar python3 en lugar de python para ejecutar el script, ya que en algunas configuraciones de macOS, el comando python podría no estar vinculado a Python 3.

El script te pedirá que ingreses el texto a cifrar y el desplazamiento (número entero). Asegúrate de introducir estos datos correctamente para obtener el resultado deseado.


### 2. **Captura de Tráfico ICMP**
En esta actividad se capturó el tráfico ICMP utilizando herramientas como Wireshark. El archivo de captura resultante se guarda en formato `.pcapng`, el cual contiene los paquetes de red capturados para su posterior análisis.

#### Archivos Relacionados:
- **`Trafico_Lab1.pcapng`**: Archivo con el tráfico ICMP capturado.

### 3. **Descifrado Automático del Mensaje**
En la tercera actividad, se desarrolló un script para intentar descifrar el mensaje oculto en los paquetes cifrados. El script prueba todas las combinaciones posibles de desplazamiento y elige el mensaje más probable basándose en las palabras comunes en español.

#### Archivos Relacionados:
- **`prueba2.py`**: Script que lee los paquetes `.pcapng` y realiza el análisis de descifrado con todas las combinaciones posibles de desplazamiento.

## Descripción de los Archivos del Proyecto

- **`cesar.py`**: Script para cifrar y descifrar el mensaje utilizando el cifrado César.
- **`prueba.py`**: Script para transformar cualquier palabra o frase con el cifrado César.
- **`prueba2.py`**: Script para leer los paquetes `.pcapng` y realizar el análisis de descifrado.
- **`Trafico_Lab1.pcapng`**: Archivo con el tráfico ICMP capturado.
- **`README.md`**: Este archivo con la documentación del proyecto.

## Requisitos

Para ejecutar los scripts en este proyecto, necesitarás tener instalados los siguientes paquetes de Python:

- **Scapy**: Para el análisis y manipulación de paquetes de red.
  - Instala Scapy con: `pip install scapy`
- **Termcolor**: Para imprimir el mensaje descifrado en color.
  - Instala Termcolor con: `pip install termcolor`

## Cómo Ejecutar el Proyecto

1. Asegúrate de tener el archivo `Trafico_Lab1.pcapng` en el directorio de trabajo.
2. Ejecuta el script de descifrado con el siguiente comando:

   ```bash
   sudo python3 prueba2.py Trafico_Lab1.pcapng

