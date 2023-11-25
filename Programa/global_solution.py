# Função para exibir o menu principal
def exibir_menu():
    print("===== Plataforma de Sensibilização para Vacinação =====")
    print("Selecione uma opção:")
    print("1. Ver informações sobre vacinas")
    print("2. Ver estatísticas de vacinação")
    print("3. Ver locais de vacinação próximos")
    print("4. Sair")

# Função para obter a opção do usuário
def obter_opcao():
    opcao = int(input("Digite o número da opção desejada: "))
    if opcao < 1 or opcao > 4:
        print("Por favor, digite uma opção válida (1 a 4).")
    return opcao

# Função para exibir informações sobre vacinas
def informacoes_vacinas():
    # Informações sobre vacinas
    print("Informações sobre vacinas: ...")

# Função para exibir estatísticas de vacinação
def estatisticas_vacinacao():
    # Aqui você pode incluir estatísticas de vacinação
    print("Estatísticas de vacinação: ...")

# Função para exibir locais de vacinação próximos
def locais_vacinacao():
    # Aqui você pode adicionar a lógica para buscar locais de vacinação próximos
    print("Locais de vacinação próximos: ...")

# Execução do programa
opcao = 0
while opcao != 4:
    exibir_menu()
    opcao = obter_opcao()

    if opcao == 1:
        informacoes_vacinas()
    elif opcao == 2:
        estatisticas_vacinacao()
    elif opcao == 3:
        locais_vacinacao()

print("Obrigado por usar a plataforma de sensibilização para vacinação.")
