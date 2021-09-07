#importando Tkinter
# * serve para impotar todas as funções da biblioteca Tkinter

from tkinter import *
from tkinter import ttk
from tkinter.font import Font

#cores
azul = "#201f5e" # fundo da tela de saida
cinza = "#bababa" # cor dos botões numericos
branco = "#ffffff" # cor dos caracteres
preto = "#000000" # cor dos caracteres
verde = "#5af542" #cor dos botões de operações

janela = Tk() # iniciando a janela da interface
janela.title('CALCULADORA By Nicholas') # definindo titulo da janela
janela.geometry('235x310')  #configuração de tamanho de tela 
janela.config(bg=preto) # definindo fundo do app de preto

#criando frames
# nesse trecho estamos dividindo a tela
frame_tela = Frame(janela, width=235, height=50, bg=azul) #definindo tamanho do frame de saida de dados
frame_tela.grid(row=0, column=0) # localização do frame na janela

frame_corpo= Frame(janela, width=235, height=268) # definindo tamanho do frame dos botões 
frame_corpo.grid(row=1, column=0) 

# iniciando variavel todos_valores com valor vazio

todos_valores = ""

#criando funções e lógica do app


# função para entrada dos valores
def entrada_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event) # 
    # passando valor para tela
    valor_texto.set(todos_valores)
    
# função para calcular 

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    
# função para limpar tela

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")
    
# Criando labels
valor_texto = StringVar()

app_label = Label(frame_tela, 
                  textvariable = valor_texto,
                  width= 14, 
                  height= 2,
                  padx= 10 , 
                  relief=FLAT,
                  anchor="e", 
                  justify=RIGHT,
                  font=('Ivy 18 '), 
                  fg=branco,
                  bg=azul
                  )
app_label.place(x=0, y=0)


#criando botões

#primeira fila
bc = Button(frame_corpo,
            command= limpar_tela,
            text="C",
            width=11,
            height=2,
            bg=cinza,
            fg=preto,
            font=('Ivy 13 bold'),
            relief=RAISED,
            overrelief=RIDGE
            )
bc.place(x=2, y=0)
b_porcentagem = Button(frame_corpo,
                       command=lambda: entrada_valores('%'),
                       text="%",
                       width=5,
                       height=2,
                       bg=cinza,
                       fg=preto,
                       font=('Ivy 13 bold'),
                       relief=RAISED,
                       overrelief=RIDGE
                       )
b_porcentagem.place(x=115, y=0)
b_divide = Button(frame_corpo,
                  command=lambda: entrada_valores('/'),
                  text="/",
                  width=5, height=2,
                  bg=verde,
                  fg=preto,
                  font=('Ivy 13 bold'),
                  relief=RAISED,
                  overrelief=RIDGE
                  )
b_divide.place(x=178, y=0)

#segunda fila
b7 = Button(frame_corpo,
            command=lambda: entrada_valores('7'),
            text="7",
            width=5,
            height=2,
            bg=cinza,
            fg=preto,
            font=('Ivy 13 bold'),
            relief=RAISED,
            overrelief=RIDGE
            )
b7.place(x=2, y=52)
b8 = Button(frame_corpo,
            command=lambda: entrada_valores('8'),
            text="8",
            width=5,
            height=2,
            bg=cinza,
            fg=preto,
            font=('Ivy 13 bold'),
            relief=RAISED,
            overrelief=RIDGE
            )
b8.place(x=54, y=52)
b9 = Button(frame_corpo,
            command=lambda: entrada_valores('9'),
            text="9",
            width=5,
            height=2,
            bg=cinza,
            fg=preto,
            font=('Ivy 13 bold'),
            relief=RAISED,
            overrelief=RIDGE
            )
b9.place(x=115, y=52)
b_multiplica = Button(frame_corpo,
                      command=lambda: entrada_valores('*'),
                      text="*",
                      width=5,
                      height=2,
                      bg=verde,
                      fg=preto,
                      font=('Ivy 13 bold'),
                      relief=RAISED,
                      overrelief=RIDGE
                      )
b_multiplica.place(x=178, y=52)

#terceira fila
b4 = Button(frame_corpo,
            command=lambda: entrada_valores('4'),
            text="4",
            width=5,
            height=2,
            bg=cinza,
            fg=preto,
            font=('Ivy 13 bold'),
            relief=RAISED,
            overrelief=RIDGE
            )
b4.place(x=2, y=104)
b5 = Button(frame_corpo,
            command=lambda: entrada_valores('5'),
            text="5",
            width=5,
            height=2,
            bg=cinza,
            fg=preto,
            font=('Ivy 13 bold'),
            relief=RAISED,
            overrelief=RIDGE
            )
b5.place(x=54, y=104)
b6 = Button(frame_corpo,
            command=lambda: entrada_valores('6'),
            text="6",
            width=5,
            height=2,
            bg=cinza,
            fg=preto,
            font=('Ivy 13 bold'),
            relief=RAISED,
            overrelief=RIDGE
            )
b6.place(x=115, y=104)
b_subtrai = Button(frame_corpo,
                   command=lambda: entrada_valores('-'),
                   text="-",
                   width=5,
                   height=2,
                   bg=verde,
                   fg=preto,
                   font=('Ivy 13 bold'),
                   relief=RAISED,
                   overrelief=RIDGE
                   )
b_subtrai.place(x=178, y=104)

#quarta fila
b1 = Button(frame_corpo,
            command=lambda: entrada_valores('1'),
            text="1",
            width=5,
            height=2,
            bg=cinza,
            fg=preto,
            font=('Ivy 13 bold'),
            relief=RAISED,
            overrelief=RIDGE
            )
b1.place(x=2, y=156)
b2 = Button(frame_corpo,
            command=lambda: entrada_valores('2'),
            text="2",
            width=5,
            height=2,
            bg=cinza,
            fg=preto,
            font=('Ivy 13 bold'),
            relief=RAISED,
            overrelief=RIDGE
            )
b2.place(x=54, y=156)
b3 = Button(frame_corpo,
            command=lambda: entrada_valores('3'),
            text="3",
            width=5, 
            height=2,
            bg=cinza, 
            fg=preto,
            font=('Ivy 13 bold'), 
            relief=RAISED,
            overrelief=RIDGE
            )
b3.place(x=115, y=156)
b_soma = Button(frame_corpo,
                command=lambda: entrada_valores('+'),
                text="+",
                width=5,
                height=2,
                bg=verde,
                fg=preto,
                font=('Ivy 13 bold'),
                relief=RAISED,
                overrelief=RIDGE
                )
b_soma.place(x=178, y=156)


#quinta fila
b0 = Button(frame_corpo,
            command=lambda: entrada_valores('0'),
            text="0",
            width=11,
            height=2,
            bg=cinza,
            fg=preto,
            font=('Ivy 13 bold'),
            relief=RAISED,
            overrelief=RIDGE
            )
b0.place(x=2, y=208)
b_ponto = Button(frame_corpo,
                 command=lambda: entrada_valores('.'),
                 text=".",
                 width=5,
                 height=2,
                 bg=cinza,
                 fg=preto,
                 font=('Ivy 13 bold'),
                 relief=RAISED,
                 overrelief=RIDGE
                 )
b_ponto.place(x=115, y=208)
b_igualdade = Button(frame_corpo,
                     command = calcular,
                     text="=",
                     width=5,
                     height=2,
                     bg=verde,
                     fg=preto,
                     font=('Ivy 13 bold'),
                     relief=RAISED,
                     overrelief=RIDGE
                     )
b_igualdade.place(x=178, y=208)


janela.mainloop()  #mantem a janela aberta
