"""
Clase TaskManager
Al crear una instancia permite utilizar los metodos:
    - add_task
    - complete_task
    - show_tasks
"""
def log_action(func):
    """
    Este decorador imprime un mensaje antes y después de ejecutar
    una función del gestor de tareas.
    """
    def wrapper(*args, **kwargs):
        print(f"--- Acción iniciada: {func.__name__} ---")
        result = func(*args, **kwargs)
        print(f"--- Acción finalizada: {func.__name__} ---")
        return result
    return wrapper


class TaskManager:
    # Este es el constructor que va a inicilizarse cada vez que se cree una instancia de la clase TaskManager
    # El constructor inicializa el estado del objeto
    # Con self creamos estos atributos
    # Creamos una lista de diccionarios
    def __init__(self):
        self.tasks = []
        self.next_id_task = 1

    # Creamos las funciones de la clase
    @log_action
    def add_task(self, description):
        # Creamos la tarea
        task = {
            "id": self.next_id_task,
            "description": description,
            "status": False,
        }
        # Agregamos la tarea a la lista con el metodo append
        self.tasks.append(task)
        # Autoincrementamos el id para la siguente tarea
        self.next_id_task = self.next_id_task + 1
        print("Tarea Agregada")

    @log_action
    def complete_task(self, id_task):
        for task in self.tasks:
            if task["id"] == id_task:
                task["status"] = True
                return
        print("No se encontro la tarea")

    @log_action
    def show_tasks(self):
        print("Lista de tareas")
        if self.tasks:
            for task in self.tasks:
                if task["status"] == True:
                    print(
                        f"Id: {task['id']} / Desc: {task['description']} / Estado: Completada"
                    )
                else:
                    print(
                        f"Id: {task['id']} / Desc: {task['description']} / Estado: No Completada"
                    )
        else:
            print("No hay tareas que mostrar")
            
''' WIP - metodo eliminar tarea
    def delete_task(self, id_task):
        #for task in self.tasks:
           #if task["id"] == id_task:
        for i in range(len(self.tasks)):
            element = self.tasks[i]
            if element['id'] == id_task:
                self.tasks.pop(i)
'''              