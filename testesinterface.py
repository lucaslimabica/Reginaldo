import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Reginaldo Beta Version")
        self.configure(bg='#FFAE69')
        self.app_state = None

        container = ttk.Frame(self)
        container.pack(fill='both', expand=True)

        self.frames = {}
        # Inicialização dos frames
        for F in (HomePage, EtapasFunisPage, CamposPage, AtividadesPage, UsersPage, TemplatesPage, APIsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self, app_state=self.app_state)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class HomePage(ttk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state
        self.configure(style='TFrame', padding=20)
        label = ttk.Label(self, text="Página Inicial", style='TLabel')
        label.pack(pady=10)

        label2 = ttk.Label(self, text="Digite seu token de API:", style='TLabel')
        label2.pack(pady=10, padx=10)

        entry = ttk.Entry(self, style='TEntry')
        entry.pack(pady=5, padx=10)

        button = ttk.Button(self, text="Enviar", style='TButton')
        button.pack(pady=5)

class EtapasFunisPage(ttk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state
        self.configure(style='TFrame', padding=20)
        label = ttk.Label(self, text="Etapas Funis", style='TLabel')
        label.pack(pady=10)

class CamposPage(ttk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state
        self.configure(style='TFrame', padding=20)
        label = ttk.Label(self, text="Campos", style='TLabel')
        label.pack(pady=10)

class AtividadesPage(ttk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state
        self.configure(style='TFrame', padding=20)
        label = ttk.Label(self, text="Atividades", style='TLabel')
        label.pack(pady=10)

class UsersPage(ttk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state
        self.configure(style='TFrame', padding=20)
        label = ttk.Label(self, text="Usuários", style='TLabel')
        label.pack(pady=10)

class TemplatesPage(ttk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state
        self.configure(style='TFrame', padding=20)
        label = ttk.Label(self, text="Templates", style='TLabel')
        label.pack(pady=10)

class APIsPage(ttk.Frame):
    def __init__(self, parent, controller, app_state):
        super().__init__(parent)
        self.controller = controller
        self.app_state = app_state
        self.configure(style='TFrame', padding=20)
        label = ttk.Label(self, text="APIs", style='TLabel')
        label.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
