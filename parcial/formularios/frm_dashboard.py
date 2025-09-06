import tkinter as tk

class FrmDashboard(tk.Toplevel):
    def __init__(self, parent, usuario):
        super().__init__(parent)
        self.usuario = usuario
        self.parent = parent
        
        self.title("Dashboard")
        self.geometry("300x250")
        
        self.crear_widgets()
    
    def crear_widgets(self):
        tk.Label(self, text="BIENVENIDO/A", font=("Arial", 14)).pack(pady=10)
        
        # Imagen simulada
        tk.Label(self, text="[Imagen de Usuario]", relief="solid", width=20, height=5).pack(pady=5)
        
        tk.Label(self, text=f"Nombre: {self.usuario.nombre} {self.usuario.apellidos}").pack(pady=2)
        tk.Label(self, text=f"Email: {self.usuario.email}").pack(pady=2)
        tk.Label(self, text=f"Nickname: {self.usuario.nickname}").pack(pady=2)
        
        tk.Button(self, text="Cerrar Sesion", command=self.cerrar_sesion, width=15).pack(pady=10)
    
    def cerrar_sesion(self):
        self.destroy()
        self.parent.mostrar_login()