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
    opcao_info_vacina = 0
    while opcao_info_vacina != 4:
        print("Informações sobre vacinas")
        print("Escolha uma opção:")
        print("1. Ver informações sobre vacina A:")
        print("2. Ver informações sobre vacina B:")
        print("3. Ver informações sobre vacina C:")
        print("4. Sair")

        opcao_info_vacina = int(input("Digite o número da opção desejada: "))
        if opcao_info_vacina < 0 or opcao_info_vacina > 4:
            print("Por favor, digite uma opção válida (1 a 4)")
        else:
            if opcao_info_vacina == 1:
                print("Informações sobre a vacina A: ...")
            elif opcao_info_vacina == 2:
                print("Informações sobre a vacina B: ...")
            elif opcao_info_vacina == 3:
                print("Informações sobre a vacina C: ...")

# Função para exibir estatísticas de vacinação
def estatisticas_vacinacao():
    opcao_estat_vacina = 0
    while opcao_estat_vacina != 4:
        print("Informações sobre vacinas")
        print("Escolha uma opção:")
        print("1. Ver estatísticas sobre vacina A:")
        print("2. Ver estatísticas sobre vacina B:")
        print("3. Ver estatísticas sobre vacina C:")
        print("4. Sair")

        opcao_estat_vacina = int(input("Digite o número da opção desejada: "))
        if opcao_estat_vacina < 0 or opcao_estat_vacina > 4:
            print("Por favor, digite uma opção válida (1 a 4)")
        else:
            if opcao_estat_vacina == 1:
                print("Estatísticas sobre a vacina A: ...")
            elif opcao_estat_vacina == 2:
                print("Estatísticas sobre a vacina B: ...")
            elif opcao_estat_vacina == 3:
                print("Estatísticas sobre a vacina C: ...")

# Função para exibir locais de vacinação próximos
def locais_vacinacao():
    opcao_locais_vacina = 0
    while opcao_locais_vacina != 4:
        print("Informações sobre vacinas")
        print("Escolha uma opção:")
        print("1. Ver pontos de vacincação A:")
        print("2. Ver pontos de vacincação B:")
        print("3. Ver pontos de vacincação C:")
        print("4. Sair")

        opcao_locais_vacina = int(input("Digite o número da opção desejada: "))
        if opcao_locais_vacina < 0 or opcao_locais_vacina > 4:
            print("Por favor, digite uma opção válida (1 a 4)")
        else:
            if opcao_locais_vacina == 1:
                print("Pontos de vacincação A: ...")
            elif opcao_locais_vacina == 2:
                print("Pontos de vacincação B: ...")
            elif opcao_locais_vacina == 3:
                print("Pontos de vacincação C: ...")

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
