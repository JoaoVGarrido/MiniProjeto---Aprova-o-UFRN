alunos = list()
    
#Funções

def cadastrar_aluno():
    lista_temp = list()
    nome = input("\nDigite o nome do aluno: ")
    lista_temp.append(nome)  # Adiciona o nome
    lista_temp.append([0, 0, 0])  # Adiciona a lista de notas
    alunos.append(lista_temp.copy())  # Adiciona a lista temporária à lista de alunos
    print(f"\nAluno {lista_temp[0]} cadastrado com sucesso!")

def adicionar_notas():
    lista_notas = list()
    for i in range(3):
        notas = float(input(f"Digite a nota da unidade {i+1} do aluno: "))
        lista_notas.append(notas)
    return lista_notas

#Programa Principal

while True:
    print("\n=== Menu ===")
    print("1. Cadastrar Aluno")
    print("2. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_aluno()
    elif opcao == 2:
        break
    else:
        print("Opção inválida!")
