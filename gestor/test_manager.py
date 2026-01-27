import pytest
from gestor.manager import TaskManager

# Unicamente se uso IA para generar estos test

def test_add_task_creates_task():
    tm = TaskManager()
    tm.add_task("Mi primera tarea")
    assert len(tm.tasks) == 1
    task = tm.tasks[0]
    assert task["id"] == 1
    assert task["description"] == "Mi primera tarea"
    assert task["status"] is False

def test_complete_task_marks_as_completed():
    tm = TaskManager()
    tm.add_task("Tarea A")
    tm.add_task("Tarea B")
    # marcar la primera como completada
    tm.complete_task(1)
    assert tm.tasks[0]["status"] is True
    # la otra debe seguir sin completar
    assert tm.tasks[1]["status"] is False

def test_complete_task_not_found_prints_message(capsys):
    tm = TaskManager()
    tm.add_task("Tarea X")
    # intentar completar un id inexistente
    tm.complete_task(999)
    captured = capsys.readouterr()
    assert "No se encontro la tarea" in captured.out

def test_show_tasks_output(capsys):
    tm = TaskManager()
    tm.add_task("T1")
    tm.add_task("T2")
    tm.complete_task(2)
    tm.show_tasks()
    captured = capsys.readouterr()
    # show_tasks imprime encabezado y el estado por tarea
    assert "Lista de tareas" in captured.out
    assert "T1" in captured.out
    assert "Estado: No Completada" in captured.out
    assert "T2" in captured.out
    assert "Estado: Completada" in captured.out