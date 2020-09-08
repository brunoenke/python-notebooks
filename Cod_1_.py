from tkinter import *

#sistema de segurançã
#versão 1.0 / 2019


class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
  
        self.titulo = Label(self.primeiroContainer, text="Login")
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo.pack()
  
        self.nomeLabel = Label(self.segundoContainer,text="Nome ", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.senhaLabel = Label(self.terceiroContainer, text="Senha ", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
  
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
  
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "10")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()
  
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
  
    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        #aqui ------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        if usuario == "john" and senha == "123":
            self.mensagem["text"] = "Autenticado"

            #tela login 1
            root.destroy()

            # aqui -= Segunda tela ***
            # Home ------------======================================= tela 2

            janela = Tk()
            janela.title("Home")

            #Inicia tela do menu Iniciar
            def bt_iniciar():
                janela2 = Tk()
                janela2.title("Teste")
                janela2["bg"] = "red"
                janela2.geometry("700x300+0+0")
                janela2.mainloop()
            #Encerra tela do menu iniciar

            #botao 2
            def bt_consulta():
                janela2 = Tk()
                janela2.title("Teste")
                janela2["bg"] = "black"
                janela2.geometry("700x300+0+0")
                janela2.mainloop()

            #botao 3
            def bt_definir():
                janela2 = Tk()
                janela2.title("Teste")
                janela2["bg"] = "green"
                janela2.geometry("700x300+0+0")
                janela2.mainloop()    

            #botao 4
            def bt_confg():
                janela2 = Tk()
                janela2.title("Teste")
                janela2["bg"] = "blue"
                janela2.geometry("700x300+0+0")
                janela2.mainloop()    

            #botao 5
            def bt_sobre():
                janela2 = Tk()
                janela2.title("Teste")
                janela2["bg"] = "pink"
                janela2.geometry("700x300+0+0")
                janela2.mainloop()  

            #Chama o processo de encerrar o programa
            #==================================================================
            def bt_sair():
                janela.destroy()
                #root.destroy()
            #==================================================================

            #Cria os botoes na tela principal
            #==================================================================
            btIniciar = Button(janela, text='Iniciar', width=10, command=bt_iniciar)
            btIniciar.place(x=0, y=0)
            btConsultar = Button(janela, text='Consultar', width=10, command=bt_consulta)
            btConsultar.place(x=100, y=0)
            btDefinir = Button(janela, text='Definir', width=10, command=bt_definir)
            btDefinir.place(x=200, y=0)
            btConfiguracoes = Button(janela, text='Config', width=10, command=bt_confg)
            btConfiguracoes.place(x=300, y=0)
            btSobre = Button(janela, text='Sobre', width=10, command=bt_sobre)
            btSobre.place(x=400, y=0)
            btSair = Button(janela, text='Sair', width=10, command=bt_sair)
            btSair.place(x=500, y=0)
            #Encerra os botões na tela principal
            #==================================================================

            janela.geometry("1024x768+0+0")
            janela.mainloop()

        else:
            self.mensagem["text"] = ("Erro na autenticação")
            

root = Tk()
root.title("System")
Application(root)
root.mainloop()


