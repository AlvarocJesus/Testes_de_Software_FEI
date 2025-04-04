class TaskManager:
  def __init__(self):
    self.tasks = []
  
  def add_task(self, task):
    if task:
      self.tasks.append(task)
      return "Tarefa adicionada"
    return "Tarefa invalida"
  
  def remove_task(self, task):
    if task in self.tasks:
      self.tasks.remove(task)
      return "Tarefa removida"
    return "Tarefa nao encontrada"
  
  def list_tasks(self):
    return self.tasks if self.tasks else "Nenhuma tarefa cadastrada"

# Exemplo de uso
# tm = TaskManager()
# print(tm.add_task("Estudar para prova"))
# print(tm.list_tasks())
# print(tm.remove_task("Estudar para prova"))
# print(tm.list_tasks())