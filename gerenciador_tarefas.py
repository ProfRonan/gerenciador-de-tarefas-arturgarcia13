"""
Modulo que implementa um gerenciador de tarefas
"""

lista_de_tarefas: list[dict[str]] = [
    {"prioridade": True, "tarefa": "Estudar Python"},
    {"prioridade": False, "tarefa": "Tomar banho"},
    {"prioridade": False, "tarefa": "Assistir série"},
]


def adicionar_tarefa(prioridade: bool, tarefa: str):
    """
    Adiciona uma tarefa na lista de tarefas
    Lança exceções caso a prioridade seja inválida ou a tarefa já exista

    Args:
        prioridade (bool): True se a tarefa tem prioridade alta, False caso contrário
        tarefa (str): string que representa a tarefa
    """
    if not isinstance(prioridade, bool):
        raise ValueError("Prioridade inválida")
    for dicionario in lista_de_tarefas:
        if dicionario["tarefa"] == tarefa:
            raise ValueError("Tarefa já existe")
    lista_de_tarefas.append({"prioridade": prioridade, "tarefa": tarefa})


def remove_tarefas(índices: tuple[int]):
    """

    Remove várias tarefas da lista de tarefas de uma vez, dado uma tupla de índices
    Lança exceções caso a tarefa não exista

    Args:
        índices (tuple[int]): tupla de inteiros que representam os índices das tarefas
                             que devem ser removidas da lista.
    """
    tamanho_de_tarefas = len(lista_de_tarefas)
    índices = sorted(list(índices), reverse=True)
    for i in índices:
        if i >= 0 and i < tamanho_de_tarefas:
            lista_de_tarefas.pop(i)
        else:
            raise ValueError("Tarefa não existe")

def encontra_tarefa(tarefa: str) -> int:
    """
    Encontra o índice de uma tarefa na lista de tarefas
    Lança exceções caso a tarefa não exista

    Args:
        tarefa (str): string que representa a tarefa
    """
    for index, dicionario in enumerate(lista_de_tarefas):
        if dicionario["tarefa"] == tarefa:
            return index
    raise ValueError("Tarefa não existe")

def ordena(dicionario):
    primeiro = 0 if dicionario['prioridade'] else 1
    return (primeiro, dicionario['tarefa'])

def ordena_por_prioridade():
    """
    Ordena a lista de tarefas por prioridade com as tarefas prioritárias no
    início da lista, seguidas pelas tarefas não prioritárias.
    As tarefas prioritárias devem ser ordenadas por ordem alfabética e as
    tarefas não prioritárias devem ser ordenadas por ordem alfabética.
    """
    # Ordenar as tarefas prioritárias por ordem alfabética
    lista_de_tarefas.sort(key=ordena)

def get_lista_de_tarefas():
    """
    Retorna somente o texto das tarefas da lista de tarefas
    """
    texts = []
    for tarefa in lista_de_tarefas:
        texto = tarefa["tarefa"]
        prioridade = tarefa["prioridade"]
        texts.append(f"{'*' if prioridade else ''} {texto}")
    return tuple(texts)
