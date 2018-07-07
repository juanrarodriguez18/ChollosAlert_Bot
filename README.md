# ChollosAlert

Bot de Telegram que te alertará con tus chollos favoritos. ¡No volverás a perderte ninguno nunca más!

## Configuración Básica

A continuación se listarán los comandos básicos de la configuración del bot:

- **TOKEN**: El token del bot creado, [@BotFather](https://telegram.me/BotFather) nos lo proporcionará al preguntarle por el Token de un bot ya creado.
- **PATH**: Ruta en la que se almacenará la Base de Datos usada por el bot.
- **DEFAULT_REFRESH_TIME**: Tiempo de refresco (en segundos) del bot para la búsqueda de chollos.
- **LOG_LEVEL**: Nivel de Log a almacenar en el archivo de Log.
- **LOG_PATH**: Ruta en la que se almacenará el archivo de Log del bot.

Existen dos archivos de ejemplo donde almacenar dichos comandos, el primero es `my_config/config_example.ini` configuración usada si ejecutamos el bot directamente desde Python. Por otro lado, tenemos el archivo `.example.env` que contiene la configuración de ejemplo si ejecutamos el bot desde Docker.

## Lanzando el Bot

Podemos lanzarlos de dos formas distintas:

- [Python](./README.md#python)
- [Docker](./README.md#docker)

## Python

Para lanzarlo desde Python usaremos los siguientes comandos:

```bash
pip install -r requirements.txt
python chollos_bot.py --config_path my-config/my_config.ini
```

La ruta `my-config/my_config.ini` corresponderá con la ruta que hayamos configurado para el archivo de configuración, la indicada es la ruta que se recomienda.

## Docker

> En construcción

## Comandos del Bot

- **start** - Activa el Bot para comenzar a recibir Chollos
- **listarpalabrasclave** - Muestra la lista de Palabras Clave configuradas
- **listarcomercios** - Muestra la lista de Comercions configurados
- **modificarpalabrasclave** - Modifica la lista de Palabras Clave
- **modificarcomercios** - Modifica la lista de Comercios
- **cancel** - Cancela la conversación actual con el Bot
- **help** - Muestra la ayuda del Bot