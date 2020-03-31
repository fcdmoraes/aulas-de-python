### TKINTER ###
###############
### o tkinter serve para criarmos janelas com widgets
### widgets podem ser botões, labels, frames, entradas de texto, entre outros
####################################################################################
### fique atento ao tkinter porque as funções precisam ser definidas antes do corpo principal

from tkinter import *

### aqui criamos nossa janela
janela = Tk()
### No tkinter nós podemos ter apenas uma janela principal Tk(). As outras deveram se chamar Toplevel.
### Quando a janela Tk() é fechada, todas as outras janelas também fecham

### com o .geometry podemos definir o tamanho dela.
### Se isso não é feito a janela se expande para conter o que estiver dentro dela
# janela.geometry("400x600")
### podemos alterar o título na janela
janela.title("título")
### o .tk_setPalette permite configurar as cores de fundo e de texto padrão de todos os widgets
janela.tk_setPalette(background = '#000050')

### essa função imprime 'Click' no terminal 
def imprime():
	print("Click")
### essa modifica o texto e o background do label chamado l3, que está definido mais adiante
def change():
	### para mudar uma propriedade de um widget, tratamos ele como um dicionário, onde a propriedade a ser alterada é passada como chave
	l3['text'] = 'Changed'
	l3['background'] = 'purple4'
### essa pega os valores de um Entry e um OptionMenu e imprime no terminal
def post():
	### o método .get() pode recuperar a informação digitada em um entry ou salva em uma variável do tkinter
	print(e1.get())
	print(var.get())

### Frames são partes da janela, que podem conter outros widgets dentro deles, inclusive outros frames
### Eles servem para podermos organizar melhor os elementos dentro nas nossas janelas
frame1 = Frame(janela, width = 200, height = 100, bg = 'blue')
frame1.pack(side = TOP, padx = 10)
### sempre que criamos um widget temos que dizer em que master (janela ou frame) ele vai ser criado
### depois precisamos posicionar ele no master através dos métodos pack, grid ou place
### o método pack é a maneira mais simples de colocar um widget em uma janela
### .pack(side = "top") insere o widget imediatamente abaixo do último widget posicionado
### ele é colocado alinhado horizontalmente
### .pack(side = "left") alinha à direita do último widget, centralizado verticalmente

frame2 = Frame(janela, width = 200, height = 100, bg = 'red', bd = 10, relief = RIDGE)
frame2.pack(side = BOTTOM, pady = 10)

### um botão pode executar uma ação ao ser clicado
### para executar a ação, passamos o nome da função a ser executada, sem passar nenhum argumento
### como consequência, a função não pode receber parâmetros
b1 = Button(frame1, text = "Click", font = ('helvetica', 18, ('italic','bold')), bg = 'gray',
 fg = 'white', activebackground = 'green', activeforeground = 'gold', width = 10, 
 anchor = 'w', command = imprime)
b1.pack(side = LEFT)
### os botões, assim como os outros widgets, podem receber uma série de configurações

b2 = Button(frame1, text = "Close", font = ('helvetica', 18, ('italic','bold')), bg = 'gray',
 fg = 'white', activebackground = 'green', activeforeground = 'gold', width = 10, 
 anchor = 'w', command = janela.destroy)
b2.pack(side = LEFT)

### Um Label é um widget que pode conter um texto ou uma cor 
l1 = Label(frame2, width = 10, bg = '#a0a000')
l1.grid(row = 0, column = 0)
### O grid permite inserir os widgets em tabelas. A largura/altura das linhas/colunas são definidas pelo maior
### widget na mesma linha/coluna. Quando a largura/altura for maior do que a do widget ele será colocado no centro.
### Isso pode ser alterado usando a função sticky que manda o widget grudar em um dos cantos. Para que ele grude em
### todos os cantos, podemos usar 'sticky = "nswe"'.
### Linhas e colunas vazias não ocupam nenhum espaço.
### Um widget pode ocupar n linhas/colunas usando o comando linespan/collumnspan.

l2 = Label(frame2, text = 'label', width = 10, bg = '#a000a0')
l2.grid(row = 0, column = 1)
l3 = Label(frame2, text = 'LABEL', width = 10, bg = 'green')
l3.grid(row = 1, column = 0, columnspan = 2, sticky = 'we')
Button(frame2, text = 'change', command = change).grid(row = 2, column = 0)
Button(frame2, text = 'post', command = post).grid(row = 2, column = 1)
### um Entry é um widget onde o usuário digitar algo
e1 = Entry(frame2)
e1.grid(row = 3, column = 0, columnspan = 2, sticky = 'we')

### agora faremos um OptionMenu. Ele se difere dos outros widgets na forma de se construído...
### para fazer um OptionMenu precisamos passar: o mestre, a variável que vai salvar a escolha e as opções que serão dadas ao usuário
### a variável que salva a escolha é uma variável especial do tkinter que pode ser StringVar, IntVar ou FloatVar
var = StringVar(janela)
### nós podemos definir o valor inicial dessa variável com um .set()
var.set("Escolha:")
### as opções do OprionMenu podem ser passadas diretamente ao criá-lo, ou de uma lista, usando um asterisco antes do nome da lista 
lista_escolhas = ['escolha 1', 'escolha 2', 'escolha 3']
OM = OptionMenu(frame2, var, *lista_escolhas)
OM.grid(row = 4, column = 0)

###### EVENTOS ######
### eventos são eventos de teclado, mouse ou configurações que o tkinter, ao detectar, responde executando uma ação
### as ações são definidas em funções que recebem um argumento referente ao evento ocorrido.
### no caso de um evento de mouse o argumento enviado pra função contém as posições x e y do mouse, com relação ao widget que rdetectou a ação
### no caso de um evento de teclado, o argumento contém informações sobre a tecla pressionada.
def binded(event):
	print(event.x, event.y)
def key_pressed(event):
	print(event.keysym)
def close(event):
	janela.destroy()
def open_window(event):
	noja_janela = Toplevel()
### os eventos e ações a serem executadas são definidas pelo método .bind(event,callback)
janela.bind('<Button-1>', binded)
janela.bind('<KeyRelease>', key_pressed)
janela.bind('<Control-w>', close)
janela.bind('<Control-o>', open_window)

janela.mainloop()

print("finish")