"""Test file for testing the functions in main.py file"""

import unittest  # for creating the test case
import sys  # for adding the parent directory to the path
from pathlib import Path  # for getting the path of the main.py file
# add the parent directory to the path in order to run it from the run command in vscode
MAIN_FILE_FOLDER = Path(__file__).parents[1].as_posix()
sys.path.insert(1, MAIN_FILE_FOLDER)
import gerenciador_tarefas as gt  # nopep8 pylint: disable=wrong-import-position


class TestFunction(unittest.TestCase):
    """Class for testing the main.py file"""

    def setUp(self):
        """Inicializa os casos de teste"""
        gt.lista_de_tarefas: list[dict[str]] = []

    def test_adiciona_tarefas_lista_vazia(self):
        """Testa se é possível adicionar uma tarefa à lista vazia"""
        tarefa = {"prioridade": True, "tarefa": "Tarefa 1"}
        gt.adicionar_tarefa(tarefa["prioridade"], tarefa["tarefa"])
        self.assertEqual(gt.lista_de_tarefas, [tarefa])

    def test_adiciona_tarefas_lista_elementos(self):
        """Testa se é possível adicionar uma tarefa à lista com alguns elementos"""
        tarefas = [
            {"prioridade": True, "tarefa": "Tarefa 1"},
            {"prioridade": False, "tarefa": "Tarefa 2"},
            {"prioridade": True, "tarefa": "Tarefa 3"}
        ]
        for tarefa in tarefas:
            gt.adicionar_tarefa(tarefa["prioridade"], tarefa["tarefa"])
        self.assertEqual(gt.lista_de_tarefas, tarefas)

    def test_adiciona_tarefa_prioridade_inválida(self):
        """Testa se é possível adicionar uma tarefa à com prioridade inválida"""
        tarefa = {"prioridade": "prioridade inválida", "tarefa": "Tarefa 1"}
        self.assertRaises(ValueError, gt.adicionar_tarefa,
                          tarefa["prioridade"], tarefa["tarefa"])

    def test_adiciona_tarefa_já_existente(self):
        """Testa se é possível adicionar uma tarefa com mesmo nome de outra"""
        tarefa = {"prioridade": "prioridade inválida", "tarefa": "Tarefa 1"}
        gt.adicionar_tarefa(tarefa["prioridade"], tarefa["tarefa"])
        self.assertRaises(ValueError, gt.adicionar_tarefa,
                          tarefa["prioridade"], tarefa["tarefa"])

    def test_remove_tarefa_lista_vazia(self):
        """Testa se é possível remover uma tarefa da lista vazia"""
        self.assertRaises(ValueError, gt.remove_tarefas, (0,))

    def test_remove_tarefa_lista_com_elementos(self):
        """Testa se é possível remover uma tarefa da lista sem ter o elemento nela"""
        tarefa = {"prioridade": True, "tarefa": "Tarefa 1"}
        gt.adicionar_tarefa(tarefa["prioridade"], tarefa["tarefa"])
        self.assertRaises(ValueError, gt.remove_tarefas, (1,))

    def test_remove_tarefa_lista_várias(self):
        """Testa se é possível remover várias tarefas da lista"""
        tarefas = [
            {"prioridade": True, "tarefa": "Tarefa 1"},
            {"prioridade": False, "tarefa": "Tarefa 2"},
            {"prioridade": True, "tarefa": "Tarefa 3"},
            {"prioridade": False, "tarefa": "Tarefa 4"},
        ]
        for tarefa in tarefas:
            gt.adicionar_tarefa(tarefa["prioridade"], tarefa["tarefa"])
        gt.remove_tarefas((1, 3))
        self.assertEqual(gt.lista_de_tarefas, [tarefas[0], tarefas[2]])

    def test_ordena_prioridade(self):
        """
        Testa se é possível ordenar as tarefas por prioridade
        """
        tarefas = [
            {"prioridade": True, "tarefa": "C"},
            {"prioridade": False, "tarefa": "B"},
            {"prioridade": True, "tarefa": "A"},
            {"prioridade": False, "tarefa": "D"}
        ]
        for tarefa in tarefas:
            gt.adicionar_tarefa(tarefa["prioridade"], tarefa["tarefa"])
        gt.ordena_por_prioridade()
        self.assertEqual(gt.lista_de_tarefas, [
                         tarefas[2], tarefas[0], tarefas[1], tarefas[3]])


if __name__ == "__main__":
    unittest.main()
