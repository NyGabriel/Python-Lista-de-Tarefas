import tkinter as tk

# Passo 2: Criando a Classe da Lista de Tarefas
class ToDoListApp:
    def __init__(self):
        # Passo 3: Configurando a Interface Gráfica
        self.root = tk.Tk()
        self.root.title("Lista de Tarefas")

        self.label = tk.Label(self.root, text="Digite sua tarefa:")
        self.label.pack()

        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack()

        self.add_button = tk.Button(self.root, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack()

        self.tasks_listbox = tk.Listbox(self.root, width=50)
        self.tasks_listbox.pack()

        self.remove_button = tk.Button(self.root, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.pack()

    # Passo 4: Criando as Funções da Lista de Tarefas
    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            tk.messagebox.showwarning("Aviso", "A tarefa não pode estar vazia.")

    def remove_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(selected_task_index)
        except IndexError:
            tk.messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para remover.")

    def update_tasks_listbox(self):
        # Esta função seria usada para atualizar a lista de tarefas se estivesse armazenada externamente
        pass

# Passo 5: Executando o Programa Principal
if __name__ == "__main__":
    app = ToDoListApp()
    app.root.mainloop()
