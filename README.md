# Juego de Serpientes y Escaleras

### Trabajo realizado por:
Escorcia Alcantara Gregorio Jacobo

Karla Abigail Tovar Salazar

Ramírez Máximo Abraham Santiago

## Descripción
Spectra es un chatbot de música inteligente diseñado para brindar a los usuarios una experiencia musical personalizada. Al conectarse con la API de Spotify, Spectra puede ofrecer recomendaciones de canciones, datos curiosos sobre artistas y géneros musicales, así como un breve recorrido histórico de diversos géneros.

## Funcionalidades principales
- Recomendaciones personalizadas: Spectra utiliza la API de Spotify para sugerir las canciones más populares de un artista específico.
- Datos curiosos: Ofrece información interesante sobre artistas, géneros y canciones.
- Historia de géneros musicales: Proporciona una breve introducción a la historia de diversos géneros musicales.
- Interfaz conversacional: Permite a los usuarios interactuar de forma natural a través de un chat.

## Cómo funciona
- Entrada del usuario: El usuario ingresa una consulta relacionada con la música (por ejemplo, "recomiéndame canciones de R&B", "¿cuál es la historia del rock?").
- Procesamiento de la consulta: Spectra analiza la consulta y determina la intención del usuario.
- Búsqueda de información: Spectra utiliza un modelo de aprendizaje para detectar e interpretar con cierta probabilidad la solicitud del usuario.
- Generación de respuesta: Spectra genera una respuesta coherente y relevante basada en la información recolectada.
- Presentación de la respuesta: La respuesta se presenta al usuario en un formato fácil de entender.

## Tecnologías utilizadas:
- Lenguaje principal: Python
- Frameworks: Django para la creación de la vista web, Keras, Tensorflow y NLTK para el modelo de predicción.
- Spotify Web API: Para obtener información sobre artistas, canciones y recomendaciones.

## Instrucciones para ejecutar:

1. Crear un entorno virtual:
   ```bash
   python -m venv spectra-venv
2. Ejecutar:
   .\spectra-venv\Scripts\activate (windows)
3. Instalar dependencias:
    pip install -r requirements.txt

    En caso de aparecer el error de:
    "ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\Users\\hapyk\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python312\\site-packages\\tensorflow\\include\\external\\com_github_grpc_grpc\\src\\core\\ext\\filters\\client_channel\\lb_policy\\grpclb\\client_load_reporting_filter.h'
    HINT: This error might have occurred since this system does not have Windows Long Path support enabled. You can find information on how to enable this at https://pip.pypa.io/warnings/enable-long-paths"

    Pasos a seguir:
    - Presionar Windows + r
    - Escribir regedit
    - Navegar a HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem.
    - Encuentre la variable LongPathsEnabled DWORD y fije el valor en 1.
    - Reinicie la computadora e instale los requerimientos de nuevo
4. Con el virtual environment aún activado, se debe ejecutar el siguiente comando:
    python spectra/bot/training.py
    
    Este comando es necesario para descargar librerías de la red neural y que el código pueda funcionar.
5. Ahora, se debe ejecutar el siguiente comando:
    python manage.py tailwind start
6. Abriendo otra terminal, se debe prender el virtual environment, para después prender el servidor:
    python manage.py runserver
7. Presionar Control + click izquierdo sobre el url que proporciona el código.
8. Puedes disfrutar de tu asistente musical personal, Spectra. :)
