# import tkinter as tk
# from tkinter import scrolledtext
# from michatbot import responder_chatbot  # Importar la función del chatbot

# def enviar_mensaje(event=None):
#     mensaje_usuario = entrada_texto.get()

#     if mensaje_usuario.strip() == "":
#         return

#     chat_ventana.insert(tk.END, "\n", "espacio")
#     chat_ventana.insert(tk.END, "Tú: " + mensaje_usuario + "\n", "usuario")

#     entrada_texto.delete(0, tk.END)

#     respuesta_chatbot = responder_chatbot(mensaje_usuario)
#     chat_ventana.insert(tk.END, "Chatbot: " + respuesta_chatbot + "\n", "chatbot")

#     chat_ventana.yview(tk.END)

# ventana = tk.Tk()
# ventana.title("Chatbot")
# ventana.geometry("400x500")

# chat_ventana = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, height=20, padx=10, pady=10)
# chat_ventana.pack(pady=10, padx=10)
# chat_ventana.config(state=tk.NORMAL)

# chat_ventana.tag_configure("usuario", foreground="white", background="#007acc", justify='right', lmargin1=20, lmargin2=20, rmargin=20)
# chat_ventana.tag_configure("chatbot", foreground="black", background="#d9f99d", justify='left', lmargin1=20, lmargin2=20, rmargin=20)
# chat_ventana.tag_configure("espacio", spacing1=10, spacing2=10)

# entrada_texto = tk.Entry(ventana, width=40)
# entrada_texto.pack(pady=10, padx=10)

# entrada_texto.bind("<Return>", enviar_mensaje)

# boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
# boton_enviar.pack(pady=10)

# ventana.mainloop()

import tkinter as tk

# Función que maneja la interacción con el chatbot
def enviar_mensaje(event=None):  # Añadimos 'event' para detectar el Enter
    mensaje_usuario = entrada_texto.get()

    if mensaje_usuario.strip() == "":
        return  # Si el texto está vacío, no hace nada

    # Mostrar el mensaje del usuario (fondo claro, texto blanco, alineado a la derecha)
    chat_ventana.insert(tk.END, "Tú: " + mensaje_usuario + "\n", "usuario")

    # Limpiar el cuadro de texto
    entrada_texto.delete(0, tk.END)
    
    # Respuesta del chatbot
    respuesta_chatbot = responder_chatbot(mensaje_usuario)
    
    # Mostrar la respuesta del chatbot (fondo verde claro, texto negro, alineado a la izquierda)
    chat_ventana.insert(tk.END, "Chatbot: " + respuesta_chatbot + "\n", "chatbot")

    # Desplazar automáticamente el área de chat hacia abajo
    chat_ventana.yview(tk.END)

# Función para generar una respuesta básica del chatbot
def responder_chatbot(mensaje):
    mensaje = mensaje.lower()

    # Respuestas predefinidas del chatbot
    if "hola" in mensaje:
        return "¡Hola! ¿Cómo puedo ayudarte hoy?"
    elif "adiós" in mensaje or "bye" in mensaje:
        return "¡Hasta luego! Que tengas un buen día."
    elif "nombre" in mensaje:
        return "Me llamo Chatbot. ¿En qué puedo asistirte?"
    else:
        return "Lo siento, no entiendo tu pregunta."

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Chatbot")
ventana.geometry("400x500")

# Crear el área de chat (scrollable)
chat_ventana = tk.Text(ventana, wrap=tk.WORD, height=20, padx=5, pady=5)
chat_ventana.pack(pady=10, padx=10)
chat_ventana.config(state=tk.NORMAL)  # Habilitar edición

# Definir estilos de texto
chat_ventana.tag_configure("usuario", foreground="white", background="#007acc", justify='right')  # Fondo azul claro y texto blanco
chat_ventana.tag_configure("chatbot", foreground="black", background="#d9f99d", justify='left')  # Fondo verde claro y texto negro

# Crear la entrada de texto para el usuario
entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack(pady=10, padx=10)

# Detectar la tecla "Enter" para enviar el mensaje
entrada_texto.bind("<Return>", enviar_mensaje)

# Botón para enviar el mensaje
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
boton_enviar.pack(pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
