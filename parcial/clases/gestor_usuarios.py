from tkinter import messagebox
from clases.usuario import Usuario

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []
    
    def guardar_usuario(self, nombre, apellidos, email, nickname, clave):
        for usuario in self.usuarios:
            if usuario.nickname == nickname:
                messagebox.showerror("Error", "usuario ya existe")
                return False
        
        nuevo_usuario = Usuario(nombre, apellidos, email, nickname, clave)
        self.usuarios.append(nuevo_usuario)
        messagebox.showinfo("Exito", "Usuario registrado")
        return True
    
    def validar_usuario(self, nickname, clave):
        for usuario in self.usuarios:
            if usuario.nickname == nickname and usuario.clave == clave:
                return usuario
        return None