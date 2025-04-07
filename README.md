###Laboratorio 1 de Criptografía y Seguridad en Redes

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
En esta actividad, se implementó un sistema para enviar mensajes cifrados a través de un ping ICMP. Utilizando el cifrado César para ocultar el mensaje, enviamos este mensaje oculto a una dirección IP (en este caso, Google: 8.8.8.8) utilizando el protocolo ICMP, que generalmente se usa para realizar pings y verificar la conectividad de red.

#### Archivos Relacionados:
- **`ping_script.py`**: Script utilizado para enviar el ping normal y el ping oculto (stealth) con un mensaje encriptado utilizando el cifrado César.

#### Descripción:
En esta sección, se hizo uso del módulo scapy para enviar dos tipos de pings:

Ping Normal: Se envió un ping convencional sin ningún mensaje oculto para verificar la conectividad con la IP de destino.

Ping Oculto (Stealth Ping): Se implementó un ping ICMP que oculta el mensaje cifrado en el paquete de datos. Este mensaje es el mismo que fue cifrado en la actividad anterior con un desplazamiento de 9, y se envía a la dirección IP de destino utilizando un paquete ICMP.

El mensaje cifrado enviado fue:

```bash
larycxpajorj h bnpdarmjm nw anmnb
```

Este proceso tiene como objetivo verificar si es posible ocultar un mensaje dentro de los datos del paquete ICMP sin que el receptor pueda identificar fácilmente el contenido sin el descifrado adecuado.

#### Instrucciones de Ejecución:
1. Ejecuta el script con el siguiente comando:

```bash
sudo python3 ping_script.py
```

El script te pedirá que ingreses la IP de destino (por ejemplo, 8.8.8.8 para Google).

El script realizará primero un ping normal para verificar la conexión y luego enviará el ping con el mensaje oculto cifrado.

Si se realiza correctamente, el script mostrará la respuesta del ping normal y confirmará que el mensaje cifrado fue enviado.

### 3. **Descifrado Automático del Mensaje**
En esta etapa se analizó el archivo de tráfico capturado con Wireshark durante la Actividad 2. El objetivo fue recuperar el mensaje oculto enviado mediante paquetes ICMP (ping), y posteriormente descifrarlo utilizando el mismo método de cifrado César de la Actividad 1.

#### Archivos Relacionados:
- **`Trafico_Lab1.pcapng`**: Archivo de captura generado con Wireshark, contiene el mensaje oculto en un paquete ICMP.
- **`decifrar.py`**: Script en Python que analiza el archivo .pcapng, extrae el contenido de los paquetes ICMP y descifra el mensaje automáticamente usando fuerza bruta sobre el cifrado César.
- 
## Descripción
El script utiliza Scapy para leer el archivo .pcapng y buscar paquetes ICMP con carga útil (Raw). Una vez extraído el mensaje cifrado, se aplica un ataque de fuerza bruta para probar todos los desplazamientos posibles del cifrado César (de 1 a 25), y se selecciona el más probable basándose en la presencia de palabras comunes en español.

#### Instrucciones de Ejecución:

1. Ejecuta el script con el siguiente comando:

```bash
sudo python3 decifrar.py Trafico_Lab1.pcapng
```
#### Resultado Esperado:
```bash
✅ Posible mensaje en claro:
[Desplazamiento 9] criptografia y seguridad en redes
```

Conclusión
Este laboratorio permitió aplicar conceptos básicos de criptografía para ocultar mensajes en paquetes ICMP, utilizando herramientas como Python, Scapy y Wireshark para el envío, captura y análisis de datos en una red.
