from tkinter import *

def JuntarLinks():
    url = links.get()
        
    if url != '':
        resposta_link["text"] = 'Link Enviado'
        resposta_link["foreground"] = "green"
    else:
        resposta_link["text"] = 'Link Não Enviado'
        resposta_link["foreground"] = "red"


def ReceberDados():
    chave = key.get()
    url = links.get()
    domain = dominio.get()

    if chave == '' or url == '' or domain == '':
        resposta["text"] = 'Campos não preenchidos'
        resposta["foreground"] = "red"
    elif chave != '' and url != '' and domain !=  '':
        resposta["text"] = 'Recebido'
        resposta["foreground"] = "green"


def Chat():
    chave = key.get()
    urls = links.get()
    domain = dominio.get()
    url = urls

    print(chave)
    print(urls)
    print(domain)

janela = Tk()
janela.title("Parametros")
janela.geometry("400x400")

inicio = Label(janela, text='Configuração de Parametros para treinar o seu chat')
inicio.grid(column=0, row=0, padx=60, pady=10)

texto = Label(janela, text='Digite sua Key OpenIA')
texto.grid(column=0, row=1, padx=60, pady=10)

key = Entry(janela)
key.place(x=100, y=90, width=200)

texto2 = Label(janela, text='Digite seus links')
texto2.grid(column=0, row=3, padx=60, pady=50)

links = Entry(janela)
links.place(x=100, y=170, width=200)

texto3 = Label(janela, text='Qual o dominio?')
texto3.grid(column=0, row=4, padx=60, pady=10)

dominio = Entry(janela)
dominio.place(x=100, y=250, width=200)

resposta = Label(janela, text="")
resposta.grid(column=0, row=5,pady=50)

resposta_link = Label(janela, text="")
resposta_link.grid(column=0, row=6)

Button(janela, text='Enviar', command=ReceberDados).place(x=160, y=350)
Button(janela, text='Gerar Chat', command=Chat).place(x=300,y=350)

janela.mainloop()

