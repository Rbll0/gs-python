# Função para exibir o menu principal
def exibir_menu():
    print("===== Plataforma de Sensibilização para Vacinação =====")
    print("Selecione uma opção: ")
    print("1. Ver informações sobre vacinas ou doenças")
    print("2. Ver locais das UBS de vacinação no centro de São Paulo")
    print("3. Ver telefones das UBS de vacinação no centro de São Paulo")
    print("4. Sair do programa")


# Função para obter a opção do usuário
def obter_opcao():
    opcao = int(input("Digite o número da opção desejada: "))
    if opcao < 1 or opcao > 4:
        print("Por favor, digite uma opção válida (1 a 4).")
    return opcao


# Função para exibir informações sobre vacinas ou doenças
def informacoes_vacinas():
    opcao_info_vacina = 0
    while opcao_info_vacina != 11:
        print("INFORMAÇÕES SOBRE VACINAS")
        print("Escolha uma opção: ")
        print("1. A Poliomielite voltou?")
        print("2. Sarampo mata?")
        print("3. A meningite deixa sequelas?")
        print("4. Quando tomar vacina contra febre amarela?")
        print("5. A vacina contra o sarampo é 100% eficaz?")
        print("6. A vacina contra a poliomielite tem quantas doses?")
        print("7. Quais são as reações da vacina contra o sarampo?")
        print("8. O que é vírus inativado?")
        print("9. Tem vacina contra Rotavírus?")
        print("10. Quem toma a tríplice viral tem que tomar a vacina contra a Varicela?")
        print("11. Sair do programa")

        opcao_info_vacina = int(input("Digite o número da opção desejada: "))
        if opcao_info_vacina < 1 or opcao_info_vacina > 11:
            print("Por favor, digite uma opção válida (1 a 11)")
        else:
            if opcao_info_vacina == 1:
                print("Mundialmente, ainda existem casos de poliomielite, a chamada paralisia infantil. A poliomielite continua restrita a determinadas regiões como em países de áreas de conflito, como Afeganistão e Paquistão. Mas diante disso, todos os países permanecem em risco até que a doença seja completamente erradicada do mundo. Até lá, a melhor maneira de os países minimizarem o risco e as consequências da infecção da poliomielite é manter elevados níveis de imunidade da população por meio de alta cobertura vacinal e do fortalecimento da vigilância da doença. O Estado de São Paulo não tem a confirmação de casos de poliomielite desde 1988. No entanto, em razão dos baixos índices de cobertura vacinal para a população dos territórios paulista e brasileiro, e a presença da doença em países de áreas de conflito como Afeganistão e Paquistão, existe risco considerado alto e muito alto de retorno da poliomielite em mais de 80% dos municípios. Para garantir que todos os países fiquem livres da poliomielite, é essencial vacinar todas as crianças.")
            elif opcao_info_vacina == 2:
                print("O sarampo é uma doença aguda causada por um vírus altamente transmissível, que pode levar a complicações. Casos graves são mais comuns em menores de 5 anos de idade, sobretudo crianças desnutridas, em adultos maiores de 20 anos, em indivíduos com doenças que provocam a baixa imunidade e outras condições de vulnerabilidade. As complicações que podem ocorrer são otite média, broncopneumonia, diarreia e encefalite. Mortes podem decorrer de complicações, especialmente pneumonia, infecção nos pulmões e a encefalite, infecção no sistema nervoso central que provoca inflamação do cérebro.")
            elif opcao_info_vacina == 3:
                print("A meningite é uma inflamação das membranas que envolvem o sistema nervoso central, especificamente cérebro, bulbo, cerebelo e medula espinhal. Em geral, os sintomas mais comuns são febre alta, cefaléia (dor de cabeça) e rigidez de nuca, principalmente em crianças maiores e adultos. Podem desenvolver em dias ou poucas horas. Destacam-se, entre outros sinais e sintomas, vômitos, recusa alimentar, sonolência, irritabilidade e convulsões, principalmente em recém-nascidos e lactentes. Vale ressaltar que a meningite pode ser causada por agentes de diferentes classes, como bactérias, fungos e vírus. As meningites bacterianas são consideradas um grave problema de saúde pública em função da sua alta letalidade e sequelas que levam a perda auditiva, dificuldade de aprendizado, alterações de linguagem, motoras e visuais e amputação de membros. O meningococo, em particular, pode levar a doença disseminada e choque. Já a meningite viral é, em geral, mais frequente, menos grave e a recuperação ocorre somente com cuidados gerais para alívio de sintomas. A gravidade da meningite e o tipo de tratamento estão diretamente relacionados ao agente causador.")
            elif opcao_info_vacina == 4:
                print("A vacina da febre amarela é recomendada desde 2019 em todo o território nacional para pessoas a partir de 9 meses de idade. Crianças que iniciam o esquema antes de 5 anos de idade devem receber duas doses da vacina, sendo a primeira dose aos 9 meses e a segunda dose aos 4 anos de idade. Pessoas que iniciam o esquema depois dos 5 anos de idade devem receber uma única dose de vacina, por toda a vida. No entanto, caso a pessoa tenha recebido apenas uma dose da vacina de febre amarela antes de completar 5 anos de idade, deverá receber uma dose adicional, independentemente da idade em que o indivíduo se vacine. É importante que pessoas que vão se deslocar para áreas de mata, beira de rios, pesqueiros, fazer turismo ecológico, localidades de circulação viral conhecida (em humanos ou em macacos) verifiquem suas carteiras de vacinação. Se não houver registro da vacina de febre amarela, precisam se vacinar com 10 (dez) dias de antecedência da viagem para melhor proteção. Em municípios com circulação comprovada do vírus da febre amarela (casos de febre amarela em humanos ou em macacos), a vacinação deve ser considerada também para crianças com idade entre 6 e 9 meses, não sendo esta dose válida para a rotina. Esta recomendação deverá seguir norma específica. A vacinação de pessoas com 60 anos ou mais de idade poderá ser realizada, em especial para os residentes ou viajantes das localidades com evidência de circulação do vírus da febre amarela (casos de febre amarela em humanos ou macacos), sempre associada à avaliação do risco relacionado às comorbidades nessa faixa etária. Para os viajantes internacionais, a vacinação é recomendada conforme a situação epidemiológica de risco do país de destino e/ou pela exigência de comprovação da vacinação contra a febre amarela para entrada em alguns países, devendo ser administrada com pelo menos 10 dias de antecedência.")
            elif opcao_info_vacina == 5:
                print("A vacina contra o sarampo é altamente eficaz para a prevenção da doença, com proteção de 99% das crianças que recebem duas doses da vacina, conforme indicado no calendário de vacinação. A proteção para quem tomou as duas doses é válida para sempre. No entanto, se a pessoa foi vacinada quando a imunização era feita em vacina única para sarampo, e não a tríplice viral, aos 9 meses, práticas que já não são mais consideradas seguras e que foram abolidas entre o começo dos anos 1990 e o começo dos anos 2000 (dependendo do estado), vale passar pelo processo novamente. No Brasil as vacinas utilizadas para prevenção do sarampo são: tríplice viral (contra sarampo, caxumba e rubéola) e tetra viral (contra sarampo, caxumba, rubéola e varicela).")
            elif opcao_info_vacina == 6:
                print("O número de doses a ser administrado em cada esquema vacinal, depende do calendário estabelecido para a faixa etária da pessoa a ser vacinada. Assim, teremos: Para crianças que iniciam o esquema com menos de 7 anos de idade: três doses de vacina inativada contra poliomielite (VIP), com intervalo de dois meses entre cada dose; início aos 2 meses de idade. As duas doses de reforço são feitas com vacina oral bivalente contra poliomielite, sendo a primeira aos 15 meses e a segunda aos 4 anos de idade; para crianças maiores de 7 anos de idade e adolescentes (até 19 anos de idade) ainda não vacinadas: o esquema consta de três doses de VIP, com intervalos de dois meses entre cada dose. Importante: viajantes que se deslocam para área de risco de poliomielite, mesmo que completamente vacinados, se a última dose de VIP foi administrada há mais de 12 meses, deverão receber uma dose de VIP, preferencialmente, quatro semanas antes da viagem.")
            elif opcao_info_vacina == 7:
                print("As vacinas contra o sarampo são altamente eficazes, de maneira geral, têm baixa reação e são bem toleradas. Os Eventos Supostamente Atribuíveis à Vacinação ou Imunização (ESAVI) podem ser devidos a reações a qualquer componente das vacinas ou manifestações clínicas semelhantes às causadas pelo vírus selvagem (replicação do vírus vacinal), geralmente com menor intensidade, chamada popularmente de “sarampinho”. É importante ressaltar que o sarampinho é um quadro leve.")
            elif opcao_info_vacina == 8:
                print("O vírus inativado é o vírus morto, ou seja, existem vacinas inativadas que são feitas com vírus modificado com substâncias químicas ou agentes físicos ou apenas com parte deles, não sendo possível seu adoecimento.")
            elif opcao_info_vacina == 9:
                print("Rotavírus é um microorganismo (vírus) que provoca doença aguda, caracterizada por diarreia que pode provocar quadros graves, principalmente em crianças muito pequenas ou com outros problemas de saúde. A vacina disponível é oral (líquida), monovalente, contendo a cepa humana de rotavírus G1P [8] atenuada. A vacina contra o rotavírus é indicada a partir de 2 meses, sendo duas doses, uma aos 2 meses e outra aos 4 meses com intervalo mínimo de 30 dias entre elas. A primeira dose pode ser aplicada a partir de 1 mês e 15 dias (seis semanas) até 3 meses e 15 dias de idade. O esquema vacinal não pode ser iniciado em crianças com mais de 3 meses e 15 dias de idade. A segunda dose pode ser aplicada a partir de 3 meses e 15 dias até no máximo 7 meses e 29 dias de idade, respeitando-se o intervalo mínimo de quatro semanas da primeira dose.")
            elif opcao_info_vacina == 10:
                print("A vacina tríplice viral é a mistura de três vacinas contra sarampo, rubéola e caxumba. Atualmente, é recomendada para crianças menores de 7 anos de idade, com administração de duas doses da vacina contra a varicela, sendo a primeira dose administrada aos 15 meses de idade com a vacina tetra viral (SCR + Varicela) e a segunda dose aos 4 anos com a vacina monovalente contra a varicela. No entanto, caso a criança por algum motivo perca a oportunidade de receber a vacina na idade recomendada, a vacina contra a varicela poderá ser administrada até 6 anos, 11 meses e 29 dias.")
            elif opcao_info_vacina == 11:
                print("Obrigado por usar a plataforma de sensibilização para vacinação.")


# Função para exibir locais das UBS de vacinação no centro de São Paulo
def locais_vacinacao():
    enderecos = [
        "R. HUMAITÁ, 520 - BELA VISTA - CEP: 01321-010",
        "R. ALMIRANTE MARQUES LEÃO, 684 - BELA VISTA - CEP: 01330-010",
        "R. TENENTE PENA, 8 - BOM RETIRO - CEP: 01127-020",
        "AV. LACERDA FRANCO, 791 - CAMBUCI - CEP: 01536-000",
        "R. BORACEA, 270 - SANTA CECÍLIA - CEP: 01135-010",
        "R. VITORINO CARMILO, 599 - CAMPOS ELÍSEOS - CEP: 01153-000",
        "PRAÇA PATRIARCA, 100 - CENTRO - CEP: 01002-010",
        "R. FREDERICO ALVARENGA, 259 - PQ DOM PEDRO - CEP: 01020-030"
    ]

    opcao_locais_vacina = 0
    while opcao_locais_vacina != 9:
        print("ENDEREÇOS DE UBS NO CENTRO DE SÃO PAULO (REDE PÚBLICA)")
        print("Digite o número da opção desejada (ou 9 para sair): ")

        for i, endereco in enumerate(enderecos, start=1):
            print(f"{i}. Ver endereço {i}")

        opcao_locais_vacina = int(input())

        if opcao_locais_vacina < 1 or opcao_locais_vacina > 9:
            print("Por favor, digite uma opção válida (1 a 9)")
        elif opcao_locais_vacina != 9:
            print(f"Endereço: {enderecos[opcao_locais_vacina - 1]}")


# Função para exibir telefones das UBS de vacinação no centro de São Paulo
def telefones_vacinacao():
    telefones = [
        "Tel: 3241-1632/ 3241-1163",
        "Tel: 3284-4601/ 3541-3704",
        "Tel: 3222-0619/ 3224-9903",
        "Tel: 3276-6480/ 3209-3304",
        "Tel: 3392-1281/ 3392-1882",
        "Tel: 3826-0096/ 3826-7970",
        "Tel: 3242-3756/ 3241-5515",
        "Tel: 3101-2344/ 3101-3013"
    ]

    opcao_telefones_vacinacao = 0
    while opcao_telefones_vacinacao != 9:
        print("TELEFONES DAS UBS")
        print("Digite o número da opção desejada (ou 9 para sair): ")

        for i, telefone in enumerate(telefones, start=1):
            print(f"{i}. Ver telefone {i}")

        opcao_telefones_vacinacao = int(input())

        if opcao_telefones_vacinacao < 1 or opcao_telefones_vacinacao > 9:
            print("Por favor, digite uma opção válida (1 a 9)")
        elif opcao_telefones_vacinacao != 9:
            print(f"Telefone: {telefones[opcao_telefones_vacinacao - 1]}")


# Execução do programa
opcao = 0
while opcao != 4:
    exibir_menu()
    opcao = obter_opcao()

    if opcao == 1:
        informacoes_vacinas()
    elif opcao == 2:
        locais_vacinacao()
    elif opcao == 3:
        telefones_vacinacao()

print("Obrigado por usar a plataforma de sensibilização para vacinação.")
