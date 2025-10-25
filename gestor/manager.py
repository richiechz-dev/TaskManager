"""Crear una clase

Debe contener 4 funciones
1. Agregar nueva tarea
2. Marcar como completada
3. Mostrar todas las tareas
4. Eliminar tarea
"""


class TaskManager:
    # Este es el constructor que va a inicilizarse cada vez que se cree una instancia de la clase TaskManager
    # El constructor inicializa el estado del objeto
    # Con self creamos estos atributos
    # Creamos una lista de diccionarios
    def __init__(self):
        self.tasks = []
        self.next_id_task = 1

    # Creamos las funciones de la clase
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

    def complete_task(self, id_task):
        for task in self.tasks:
            if task["id"] == id_task:
                task["status"] = True
                return
        print("No se encontro la tarea")

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
