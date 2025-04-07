# Lab1Cripto - Laboratorio 1 de Criptografía y Seguridad de Redes

Este repositorio contiene los códigos, resultados y análisis del experimento sobre el tráfico ICMP. El objetivo principal es analizar el tráfico de red, implementando técnicas de cifrado y descifrado de mensajes.

## Descripción del Proyecto

En este laboratorio se realiza un análisis de tráfico ICMP con el objetivo de aplicar técnicas criptográficas. Los pasos incluyen:

1. **Captura de tráfico ICMP**: Se utiliza un archivo de captura `.pcapng` que contiene el tráfico ICMP.
2. **Cifrado de mensajes**: Se utiliza el cifrado César para ocultar los mensajes en los paquetes de datos.
3. **Descifrado de mensajes**: A partir del tráfico cifrado, se utiliza un análisis para intentar descifrar el mensaje original.

## Archivos del Proyecto

- **`prueba.py`**: Script principal para capturar, cifrar y analizar los paquetes.
- **`prueba2.py`**: Script para leer y analizar los paquetes ICMP desde el archivo `.pcapng`.
- **`Trafico_Lab1.pcapng`**: Archivo con el tráfico ICMP capturado para realizar las pruebas.
- **`README.md`**: Este archivo con la documentación del proyecto.

## Requisitos

Para ejecutar los scripts en este proyecto, necesitarás tener instalados los siguientes paquetes de Python:

- **Scapy**: Para el análisis y manipulación de paquetes de red.
  - Instala Scapy con: `pip install scapy`
- **Termcolor**: Para imprimir el mensaje descifrado en color.
  - Instala Termcolor con: `pip install termcolor`

## Cómo Ejecutar el Proyecto

1. Asegúrate de tener el archivo `Trafico_Lab1.pcapng` en el directorio de trabajo.
2. Ejecuta el script principal de análisis con el siguiente comando:

   ```bash
   sudo python3 prueba2.py Trafico_Lab1.pcapng
