import tkinter as tk
from tkinter import messagebox
from clases.gestor_usuarios import GestorUsuarios
from formularios.frm_registro import FrmRegistro
from formularios.frm_dashboard import FrmDashboard

class FrmLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        self.gestor = GestorUsuarios()
        self.title("Login - Pedro Moreno y Moises Magallanes")
        self.geometry("300x200")
        
        # Centrar la ventana
        self.center_window()
        self.crear_widgets()
    
    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
    
    def crear_widgets(self):
        tk.Label(self, text="Nickname:").pack(pady=5)
        self.entry_nickname = tk.Entry(self, width=20)
        self.entry_nickname.pack(pady=5)
        
        tk.Label(self, text="Contraseña:").pack(pady=5)
        self.entry_clave = tk.Entry(self, width=20, show="*")
        self.entry_clave.pack(pady=5)
        
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="Ingresar", command=self.validar_usuario, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Registrar", command=self.abrir_registro, width=10).pack(side=tk.LEFT, padx=5)
    
    def validar_usuario(self):
        nickname = self.entry_nickname.get()
        clave = self.entry_clave.get()
        
        if not nickname or not clave:
            messagebox.showerror("Error", "Complete todos los campos")
            return
        
        usuario = self.gestor.validar_usuario(nickname, clave)
        
        if usuario:
            self.withdraw()
            dashboard = FrmDashboard(self, usuario)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
    
    def abrir_registro(self):
        self.withdraw()
        registro = FrmRegistro(self)
    
    def mostrar_login(self):
        self.deiconify()