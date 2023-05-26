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
    if len(índices) < 0 or len(índices) >= len(lista_de_tarefas):
            raise ValueError("Tarefa não existe")
    for index in índices:
        del lista_de_tarefas[index]

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


def ordena_por_prioridade():
    """
    Ordena a lista de tarefas por prioridade com as tarefas prioritárias no
    início da lista, seguidas pelas tarefas não prioritárias.
    As tarefas prioritárias devem ser ordenadas por ordem alfabética e as
    tarefas não prioritárias devem ser ordenadas por ordem alfabética.
    """
    global lista_de_tarefas
    lista = lista_de_tarefas
    # Ordenar as tarefas tarefas prioritárias no começo da lista
    for i, tarefa in enumerate(lista):
        if tarefa["prioridade"]:
            lista.insert(0, lista.pop(i))
    # Encontrar o index da primeira tarefa sem prioridade
    indice = int([index for index, elemento in enumerate(lista) if not elemento["prioridade"]].pop(0))
    # Ordenar as tarefas prioritárias por ordem alfabética
    lista_ordenada_true = sorted(lista[0:indice], key=lambda dicionario: dicionario["tarefa"])
    for i, dicionário in enumerate(lista[0:indice]):
        for dict in lista_ordenada_true:
            if dict["tarefa"] == dicionário["tarefa"]:
                del lista[i]
                lista.insert(0, dict)
        break
    # Ordenar as tarefas não prioritárias por ordem alfabética
    lista_ordenada_false = sorted(lista[indice:-1], key=lambda dicionario: dicionario["tarefa"])
    '''for task in lista_ordenada_false:
        lista_de_tarefas.insert(indice, task)'''



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
