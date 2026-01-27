# TaskManager

## Descripción
Una herramienta de línea de comandos para gestionar tareas de forma eficiente. Este proyecto fue desarrollado como parte de mi aprendizaje personal usando el core de Python resolviendo algunas lagunas practicas, incluyendo la aplicación de principios de Programación Orientada a Objetos y la gestión de módulos.

## Mejoras a Futuro
- Implementar persistencia de datos utilizando una base de datos SQLite mediante un ORM como sqlalchemy (Ganando felixibiladad y escalabilidad a otro tipo de bd como PostgreSQL o MySQL).

## Características Principales
- **Añadir nuevas tareas**: Agrega tareas con una descripción detallada.
- **Marcar como completadas**: Actualiza el estado de cualquier tarea a "completada".
- **Visualizar todo**: Muestra una lista de todas las tareas, indicando su ID, descripción y estado.
- **Eliminar tareas**: Borra tareas de la lista de forma permanente.

## Arquitectura del Proyecto

El proyecto está estructurado en dos componentes principales:

1.  **`main.py`**: Es el punto de entrada de la aplicación. Se encarga de mostrar el menú interactivo al usuario y procesar sus selecciones para invocar los métodos correspondientes del gestor de tareas.

2.  **`gestor/manager.py`**: Contiene la lógica de negocio encapsulada en la clase `TaskManager`.
    -   **Clase `TaskManager`**:
        -   `__init__()`: Inicializa una lista vacía para almacenar las tareas y un contador para asignar IDs únicos.
        -   `add_task(description)`: Crea y añade una nueva tarea a la lista.
        -   `complete_task(id_task)`: Busca una tarea por su ID y la marca como completada.
        -   `show_tasks()`: Imprime en la consola todas las tareas existentes con su estado actual.
        -   `delete_task(id_task)`: Elimina una tarea de la lista utilizando su ID.

## Aprendizaje y Conceptos Clave
Durante el desarrollo de este proyecto, apliqué y reforcé los siguientes conceptos:

- **Programación Orientada a Objetos (POO)**: La lógica principal está encapsulada en la clase `TaskManager`, utilizando constructores (`__init__`), atributos (`self.tasks`) y métodos para organizar el código de manera reutilizable.
- **Gestión de Módulos y Paquetes**: El proyecto está estructurado como un paquete de Python (`gestor`), lo que permite una separación clara de responsabilidades y facilita la importación de la clase `TaskManager` en el script principal.
- **Entornos Virtuales**: Se utilizó `uv` para crear un entorno virtual aislado, asegurando que las dependencias del proyecto no entren en conflicto con otros proyectos de Python en el sistema.
- **Manejo de Entrada/Salida (I/O)**: La aplicación interactúa con el usuario a través de la línea de comandos, capturando entradas (`input()`) y mostrando información (`print()`), además de gestionar errores básicos de entrada.

## Tecnologías y Bibliotecas
- **Python 3.13**

## Requisitos Previos
- Tener `Python 3.13+` instalado en tu sistema.
- Se recomienda el gestor de entornos virtuales y paquetes `uv`.

## Instalación con UV

Sigue estos pasos para configurar el proyecto en tu máquina local:

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/TaskManager.git
    ```
2.  **Navega al directorio del proyecto:**
    ```bash
    cd TaskManager
    ```
3.  **Crea un entorno virtual:**
    ```bash
    uv venv
    ```
4.  **Arracta directamente - Este paso deberia instalar las dependencias e iniciar el entorno virtual autmaticamente**
    ```bash
    uv run main.py
    ```
5.  **Opcional en caso de error - Instala las dependencias con este comando primero**
    ```bash
    uv sync
    ```

Ahora aparecerá un menú interactivo que te permitirá elegir entre las diferentes opciones disponibles.

## Autor
- [Ricardo Chavez](https://github.com/richiechz-dev)