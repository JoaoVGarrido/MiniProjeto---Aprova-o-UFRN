alunos = list()
    
#Funções

def cadastrar_aluno():
    lista_temp = list()
    nome = input("\nDigite o nome do aluno: ")
    lista_temp.append(nome)  # Adiciona o nome
    lista_temp.append([0, 0, 0, 0])  # Adiciona a lista de notas
    alunos.append(lista_temp.copy())  # Adiciona a lista temporária à lista de alunos
    print(f"\nAluno {lista_temp[0]} cadastrado com sucesso!")

def pesquisar_aluno(alunos_list):
    nome_aluno = input("\nDigite o nome do aluno: ")
    posição = -1
    for aluno in alunos_list:
        posição += 1
        if aluno[0] == nome_aluno:
            return posição
    print(f"\nAluno {nome_aluno} não encontrado!")

def exibir_aluno(posição, alunos_list):
    print(f"\nAluno: {alunos_list[posição][0]}")
    print(f"Unidade 1: {alunos_list[posição][1][0]}")
    print(f"Unidade 2: {alunos_list[posição][1][1]}")
    print(f"Unidade 3: {alunos_list[posição][1][2]}")
    print(f"Reposição: {alunos_list[posição][1][3]}")
    return 

def adicionar_notas(alunos_list):
    lista_notas = list()
    posição_aluno = pesquisar_aluno(alunos_list)
    exibir_aluno(posição_aluno, alunos_list)
    und = int(input("\nDigite o número da unidade que deseja adicionar notas (4 é reposição): "))
    

#Programa Principal

while True:
    print("\n=== Menu ===")
    print("1. Cadastrar Aluno")
    print("2. Adicionar Notas")
    print("3. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        cadastrar_aluno()
    elif opcao == 2:
        adicionar_notas(alunos)
    elif opcao == 3:
        break
    else:
        print("Opção inválida!")
