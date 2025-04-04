import unittest
from TaskManager import TaskManager

class Tests(unittest.TestCase):
  
  def test_add_task(self):
    expect = 'Tarefa adicionada'

    result = TaskManager().add_task('Estudar para prova')
    
    self.assertEqual(result, expect)

if __name__ == '__main__':
  unittest.main()