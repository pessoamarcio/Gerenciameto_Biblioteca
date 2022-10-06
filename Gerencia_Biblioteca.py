livros_disponiveis = []
livros_emprestados = []
usuarios = []

##layout 
print(100 * '-')
print("********************BIBLIOTECA********************")
print(100 * '-')
print("")

##opções de menu
def opcoes():
    print("")
    print("MENU\n")
    print("Cadastro de usuário? Digite 1")
    print("Cadastro novos livros? Digite 2")
    print("Empréstimos de livros? Digite 3")
    print("Devolução de livros? Digite 4")
    print("Relatório? Digite 5\n")

opcoes()

##para forçar o usuario voltar ao menu ou encerrar
def inicio():
    resposta = input("\nDeseja voltar ao inicio? (S) ou (N) ")
    if resposta.upper() == 'S':         ##Formata para maiusculo
        opcoes()
        servico()
    elif resposta.upper() == 'N':
        print("Até a próxima!")
    else:
        print("\nFavor inserir uma opção válida! (S) ou (N)")
        print("")
        inicio()

##cadastro de usuario
def usuario():
    novo_usuario = input("Insira o nome do novo usuário: ")
    usuarios.append(novo_usuario)   ##inserir ao final da lista
    print("Usuário cadastrado com sucesso!\n")
    print('\nO usuário cadastrado é: ', novo_usuario)
    ("")
    inicio()


##cadastramento dos livros
def livros():
    novo_livro = input("Nome do novo livro: ")
    livros_disponiveis.append(novo_livro)
    print("Livro cadastrado com sucesso!")
    print('O livro cadastrado foi: ', novo_livro)
    ("")
    inicio()


##Liha de cg para emprestimo de livros
def emprestimo_livro():
    emprestimo = input("Qual livro será emprestado? ")
    if emprestimo in livros_disponiveis:
        livros_disponiveis.remove(emprestimo) ##remove primeira ocorrentica. !!ATENÇÃO parar este metodo!!
        livros_emprestados.append(emprestimo) ##anexa objeto ao final da lista
        print("Emprestado! Por favor cuide muito bem dele.")
        inicio()
    elif emprestimo in livros_emprestados:
        print("Livro se encontra emprestado!")
        inicio()
    else:
        print("Livro não se encontra no acervo!")
        inicio()


##para devolução de livros
def devolucao_de_livros():
    devolucao = input("Qual livro será devolvido? ")
    if devolucao in livros_emprestados:
        livros_emprestados.remove(devolucao)    ##!!ATENÇÃO neste metodo!!
        livros_disponiveis.append(devolucao)
        print("Obrigado!")
        inicio()
    else:
        print("Livro não cadastrado.")
        inicio()


##Gerar algum relatorio
def relatorio():
    print("")
    print(f"Os livros: {livros_disponiveis} estão disponíveis para empréstimos.\n")
    print(f"Estes: {livros_emprestados}, não estão disponíveis para empréstimos.\n")
    print(f"Os usuários registrados são: {usuarios}")
    print("")
    inicio()

##Retornar as funções
def servico():
    tipo_de_servico = input("Digite a opção desejada: ")
    if tipo_de_servico == '1':
        usuario()
    elif tipo_de_servico == '2':
        livros()
    elif tipo_de_servico == '3':
        emprestimo_livro()
    elif tipo_de_servico == '4':
        devolucao_de_livros()
    elif tipo_de_servico == '5':
        relatorio()
    else:
        print("Favor inserir uma entrada válida! De 1 a 5.\n")
        servico()

servico()