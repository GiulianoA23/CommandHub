# CommandHub

CommandHub es una aplicación gráfica multifuncional diseñada para facilitar la gestión de archivos, la edición de texto y la interacción con la terminal de comandos. Con una interfaz intuitiva y personalizable, CommandHub permite a los usuarios cambiar temas, establecer fondos de pantalla y acceder rápidamente a herramientas esenciales.

## Características

- Gestor de archivos: Permite copiar, mover, renombrar y eliminar archivos a través de la interfaz gráfica.
- Editor de texto: Ofrece características como resaltado de sintaxis, búsqueda y reemplazo, y soporte para múltiples archivos.
- Terminal de comandos: Proporciona una terminal interactiva con autocompletado de comandos y nombres de archivos.
- Temas personalizables: Permite cambiar el aspecto de la aplicación mediante diferentes temas.
- Establecer wallpaper: Opción para seleccionar un fondo de pantalla desde el sistema de archivos.

## Requisitos

- Python 3.x
- Biblioteca Pillow (PIL) instalada

## Instalación

1. Clona o descarga el repositorio de CommandHub.
2. Asegúrate de tener Python 3.x instalado en tu sistema.
3. Instala la biblioteca Pillow (PIL) usando pip:

```bash
pip install Pillow
```

4. Ejecuta el archivo `sys.py` para iniciar la aplicación:

```bash
python sys.py
```

## Uso

1. Al iniciar la aplicación, verás la ventana principal de CommandHub con una barra de tareas en la parte inferior.
2. En la barra de tareas, encontrarás:
   - Un menú desplegable para seleccionar el tema deseado.
   - Un botón para establecer un wallpaper.
   - Accesos directos para abrir el terminal, el editor de texto y el gestor de archivos.
3. Usa los botones y menús para acceder a las diferentes funcionalidades de la aplicación.

## Personalización

Si deseas personalizar o expandir CommandHub, puedes modificar el código fuente. El código está dividido en clases para facilitar su lectura y modificación.

### Estructura del Código

El código principal se encuentra en el archivo `sistema_principal.py`. Aquí está la estructura del código:

1. **Clase `Tema`**: Encapsula la información de cada tema, incluyendo el nombre y la configuración.
2. **Clase `AplicacionGrafica`**: Hereda de `tk.Tk` y contiene toda la lógica de la aplicación. Incluye métodos para manejar los widgets, los temas, el wallpaper y las funcionalidades principales.
3. **Definición de Temas**: Una lista de objetos `Tema` que define los diferentes temas disponibles.
4. **Función `main()`**: Crea una instancia de `AplicacionGrafica` y ejecuta el bucle principal.

### Modificaciones

Para modificar o expandir CommandHub, puedes seguir estos pasos:

1. Clona o descarga el código fuente de CommandHub.
2. Abre el archivo `sistema_principal.py` en tu editor de código favorito.
3. Realiza los cambios deseados en el código, como agregar nuevas funcionalidades, modificar la interfaz o personalizar los temas.
4. Guarda los cambios y ejecuta el archivo `sistema_principal.py` para probar las modificaciones.

## Contribuciones

Si deseas contribuir al proyecto CommandHub, siéntete libre de enviar pull requests o abrir issues en el repositorio de GitHub. Todas las contribuciones son bienvenidas y apreciadas.

## Licencia

Este proyecto se distribuye bajo la [Licencia MIT](LICENSE).