import tkinter as tk
import os
from tkinter import ttk,messagebox,simpledialog
from banco_master import inserir_lista,buscar_listas,atualizar_nome
tarefas=[]
global lista_atual
def __init__():
    box_lixeira.delete(0,tk.END)
    if not os.path.exists("lixeira.txt"):
        return
    with open("lixeira.txt","x",encoding="utf-8"):
        pass
def carregar_tarefas():
    frame_lista.delete(0,tk.END)
    if not os.path.exists(lista_atual):
        return
    with open(lista_atual,"r",encoding="utf-8") as arquivo:
        for linha in arquivo:
            if linha.strip():
                frame_lista.insert(tk.END,linha.strip())
def ao_selecionar(event):
    global lista_atual
    lista_atual=combo.get()
    carregar_tarefas()
    mostrar_botoes()
def criar_lista():
    global lista_atual
    nome_lista=simpledialog.askstring("Nova Lista","Insira o Nome da lista")
    if not nome_lista:
        return
    if nome_lista in buscar_listas():
        messagebox.showerror("Erro","O nome já existe")
        return
    inserir_lista(nome_lista)
    combo["values"]=buscar_listas()
    combo.set(nome_lista)
    messagebox.showinfo("Sucesso",f"A lista {nome_lista} foi Criada!")
def renomear_lista():
    lista_atual=combo.get()
    nome_novo=simpledialog.askstring("Renomear Lista","Insira o Novo Nome da lista")
    if not nome_novo:
        return
    if nome_novo==lista_atual:
        messagebox.showerror("Erro","O novo nome não pode ser igual ao antigo")
        return
    if nome_novo in buscar_listas():
        messagebox.showerror("Erro","O nome já existe")
        return
    atualizar_nome(nome_novo,lista_atual)
    if os.path.exists(lista_atual):
        os.rename(lista_atual,nome_novo)
    lista_atual=nome_novo
    combo["values"]=buscar_listas()
    combo.set(nome_novo)
def lixeira():
    global box_lixeira 
    box_lixeira=tk.Toplevel(main)
    box_lixeira.geometry("200x300")
    box_lixeira.grid_columnconfigure(0,weight=1,uniform="col")
    box_lixeira.grid_columnconfigure(1,weight=1,uniform="col")
    titulo=tk.Label(box_lixeira,text="Lixeira",font=("Arial",15))
    titulo.grid(row=0,column=0,columnspan=2)
    box_lixeira.grid_rowconfigure(1,weight=1)
    frame_lixeira=tk.Listbox(box_lixeira,bd=0.5,relief="ridge")
    frame_lixeira.grid(row=1,column=0,columnspan=2,sticky="nsew")
    with open("lixeira.txt","r","utf=8") as arquivo:
        for linha in arquivo:
            if linha.strip():
                box_lixeira.insert(tk.END,linha.strip())
def recuperar_tarefa():
    pass
def nova_tarefa():
    if len(buscar_listas())==0:
        messagebox.showerror("Erro","É preciso criar uma lista antes!")
        return
    if lista_atual is None:
        messagebox.showerror("Erro","Selecione uma lista!")
        return
    tarefa=simpledialog.askstring("Nova Tarefa","Insira o Nome da tarefa")
    if not tarefa:
        return
    with open(lista_atual,"a",encoding="utf-8") as arquivo:
        arquivo.write(tarefa+"\n")
    frame_lista.insert(tk.END,tarefa)
def mostrar_botoes():
    botao_editar.place(in_=frame_lista,relx=1.0,rely=0,anchor="ne",x=-7,y=-32)
    botao_lixeira.place(in_=frame_lista,relx=0.0,rely=-0.01,anchor="nw",x=5,y=-27)
def hover_editar(event):
    global balao
    x=event.x_root+15
    y=event.y_root+15
    balao=tk.Toplevel(main)
    balao.overrideredirect(True)
    balao.geometry(f"+{x}+{y}")
    texto =tk.Label(balao,text="Renomear Lista",bg="#ffffe0", relief="solid", bd=1)
    texto.pack()
def hover_lixeira(event):
    global balao2
    x=event.x_root+15
    y=event.y_root+15
    balao2=tk.Toplevel(main)
    balao2.overrideredirect(True)
    balao2.geometry(f"+{x}+{y}")
    texto2=tk.Label(balao2,text="Lixeira",bg="#ffffe0",relief="solid", bd=1)
    texto2.pack()
def hover_esconder(event):
    global balao,balao2
    balao.destroy()
    balao2.destroy()
    
main=tk.Tk()
main.title("Lista de tarefas")
main.geometry("400x600")
main.grid_columnconfigure(0, weight=1,uniform="col")
main.grid_columnconfigure(1, weight=1,uniform="col")
main.grid_rowconfigure(2,weight=1)
titulo=tk.Label(main,text="Tarefas",font=("Arial",15))
titulo.grid(row=0,column=0,columnspan=2)
combo=ttk.Combobox(main,values=buscar_listas(),state="readonly",width=50,justify="center",cursor="hand2")
combo.set("Listas")
combo.grid(row=1,column=0,columnspan=2)
combo.bind("<<ComboboxSelected>>",ao_selecionar)
frame_lista=tk.Listbox(main,bd=0.5,relief="ridge")
frame_lista.grid(row=2,column=0,columnspan=2,sticky="nsew")
botao_editar=tk.Button(main,text="✏",font=("Arial",12),relief="flat",border=0.5,cursor="hand2",command=renomear_lista)
botao_editar.bind("<Enter>",hover_editar)
botao_editar.bind("<Leave>",hover_esconder)
botao_lixeira=tk.Button(main,text="🗑",font=("Arial",12),relief="flat",border=0.5,cursor="hand2",command=lixeira)
botao_lixeira.bind("<Enter>",hover_lixeira)
botao_lixeira.bind("<Leave>",hover_esconder)
botao_add=tk.Button(main,text="Adicionar Tarefa",font=("Arial",15),bg="#e0385f",relief="flat",bd=0,cursor="hand2",command=nova_tarefa)
botao_add.grid(row=3,column=0,sticky="ew",pady=5,padx=15,)
botao_criar=tk.Button(main,text="Criar Lista",font=("Arial",15),bg="#47a4d6",relief="flat",bd=0,cursor="hand2",command=criar_lista)
botao_criar.grid(row=3,column=1,sticky="ew",pady=5,padx=15,)
main.mainloop()

