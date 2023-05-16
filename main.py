"""
Este módulo contém a classe Tarefa, que é a classe principal
do programa de gerenciamento de tarefas.

A classe Tarefa é responsável por criar a interface gráfica e
interagir com o módulo gerenciador_tarefas, que contém as
funções para adicionar, remover e ordenar as tarefas.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import gerenciador_tarefas as gt


class Tarefa:
    """
    Classe principal do programa de gerenciamento de tarefas.
    """

    def __init__(self, janela: tk.Tk):
        self.título = "Minhas tarefas"
        self.tamanho = "300x400"
        self.prioridade_ativa = tk.BooleanVar(value=False)
        self.texto_tarefa = tk.StringVar(value="")
        self.lista_de_tarefas = tk.StringVar(value=gt.get_lista_de_tarefas())

        # Configurações da janela
        janela.title(self.título)  # Título da janela
        janela.geometry(self.tamanho)  # Tamanho da janela

        # Criando os widgets, que são os objetos da interface
        # 1. Quadro principal para guardar os outros widgets
        quadro = ttk.Frame(janela)
        # 2. Quadro para guardar os widgets de adicionar tarefa
        quadro_adicionar_tarefa = ttk.Frame(quadro)
        # 3. Checkbox para selecionar a prioridade
        check_prioridade = tk.Checkbutton(
            quadro_adicionar_tarefa, text="Prioritária", variable=self.prioridade_ativa)
        # 4. Rótulo para o campo de tarefa
        rótulo_tarefa = ttk.Label(quadro_adicionar_tarefa, text="Tarefa:")
        # 5. Campo para digitar um tarefa
        campo_tarefa = ttk.Entry(
            quadro_adicionar_tarefa, textvariable=self.texto_tarefa)
        # 6. Botão de adicionar tarefa
        botão_adicionar_tarefa = ttk.Button(
            quadro, text="Adicionar tarefa",
            command=self.adiciona_tarefa)
        # 7. Quadro para guardar a lista de tarefas
        quadro_lista_tarefas = ttk.Frame(quadro)
        # 8. Lista de tarefas para mostrar as tarefas
        self.list_box_lista_tarefas = tk.Listbox(
            quadro_lista_tarefas, listvariable=self.lista_de_tarefas, selectmode="extended")
        # 9. Botão de remover tarefa
        botão_remover_tarefa = ttk.Button(
            quadro, text="Remover tarefa", command=self.remove_tarefa)

        # Organizando os widgets na janela
        quadro.grid(column=0, row=0)
        quadro_adicionar_tarefa.grid(
            column=0, row=0, columnspan=3, padx=10, pady=10)
        rótulo_tarefa.grid(column=0, row=0)
        campo_tarefa.grid(column=1, row=0, sticky="ew")
        check_prioridade.grid(column=2, row=0, sticky="e")
        botão_adicionar_tarefa.grid(column=1, row=1)
        quadro_lista_tarefas.grid(column=0, columnspan=3, row=2)
        self.list_box_lista_tarefas.grid(column=0, row=0)
        botão_remover_tarefa.grid(column=1, row=3, pady=10)

    def atualiza_tarefas(self):
        """
        Atualiza a lista de tarefas na interface.
        """
        print("Atualizando tarefas")
        try:
            gt.ordena_por_prioridade()
        except (NotImplementedError, ValueError) as error:
            messagebox.showerror(
                "Erro", str(error))
        self.lista_de_tarefas.set(gt.get_lista_de_tarefas())

    def adiciona_tarefa(self):
        """
        Adiciona uma tarefa na lista de tarefas.
        """
        print("Botão de adicionar tarefa clicado")
        print("Prioridade ativa:", self.prioridade_ativa.get())
        print("Texto da tarefa:", self.texto_tarefa.get())
        try:
            gt.adicionar_tarefa(self.prioridade_ativa.get(),
                                self.texto_tarefa.get())
        except (NotImplementedError, ValueError) as error:
            messagebox.showerror(
                "Erro", str(error))
        self.atualiza_tarefas()

    def remove_tarefa(self):
        """
        Remove uma ou mais tarefas da lista de tarefas ativamente selecionadas.
        """
        print("Botão de remover tarefa clicado")
        índices = self.list_box_lista_tarefas.curselection()
        print("Tentando remover tarefa com índices", índices)
        try:
            gt.remove_tarefas(índices)
        except (NotImplementedError, ValueError) as error:
            messagebox.showerror(
                "Erro", str(error))
        self.atualiza_tarefas()


if __name__ == "__main__":
    janela_principal = tk.Tk()
    # Instancia a classe tarefa, chama o construtor e passa a janela como parâmetro
    Tarefa(janela_principal)

    # Inicia o loop principal da janela para que ela fique aberta
    janela_principal.mainloop()
