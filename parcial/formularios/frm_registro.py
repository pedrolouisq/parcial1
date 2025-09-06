import tkinter as tk
from tkinter import messagebox

class FrmRegistro(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.gestor = parent.gestor
        
        self.title("Registrar Usuario")
        self.geometry("300x350")
        
        self.crear_widgets()
    
    def crear_widgets(self):
        tk.Label(self, text="Nombre:").pack(pady=2)
        self.entry_nombre = tk.Entry(self, width=25)
        self.entry_nombre.pack(pady=2)
        
        tk.Label(self, text="Apellidos:").pack(pady=2)
        self.entry_apellidos = tk.Entry(self, width=25)
        self.entry_apellidos.pack(pady=2)
        
        tk.Label(self, text="Email:").pack(pady=2)
        self.entry_email = tk.Entry(self, width=25)
        self.entry_email.pack(pady=2)
        
        tk.Label(self, text="Nickname:").pack(pady=2)
        self.entry_nickname = tk.Entry(self, width=25)
        self.entry_nickname.pack(pady=2)
        
        tk.Label(self, text="Contraseña:").pack(pady=2)
        self.entry_clave = tk.Entry(self, width=25, show="*")
        self.entry_clave.pack(pady=2)
        
        tk.Label(self, text="Confirmar Contraseña:").pack(pady=2)
        self.entry_confirmar = tk.Entry(self, width=25, show="*")
        self.entry_confirmar.pack(pady=2)
        
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Registrar", command=self.registrar_usuario, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cancelar", command=self.cancelar, width=10).pack(side=tk.LEFT, padx=5)
    
    def registrar_usuario(self):
        nombre = self.entry_nombre.get()
        apellidos = self.entry_apellidos.get()
        email = self.entry_email.get()
        nickname = self.entry_nickname.get()
        clave = self.entry_clave.get()
        confirmar = self.entry_confirmar.get()
        
        if not all([nombre, apellidos, email, nickname, clave, confirmar]):
            messagebox.showerror("Error", "Complete todos los campos")
            return
        
        if clave != confirmar:
            messagebox.showerror("Error", "Contraseñas no coinciden")
            return
        
        exito = self.gestor.guardar_usuario(nombre, apellidos, email, nickname, clave)
        
        if exito:
            self.destroy()
            self.parent.mostrar_login()
    
    def cancelar(self):
        self.destroy()
        self.parent.mostrar_login()