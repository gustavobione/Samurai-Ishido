# capitulo_3.py
import time
import random
import layout

def rolar_teste(atributo_nome, valor_atributo, dificuldade=20):
    d20 = random.randint(1, 20)
    total = d20 + valor_atributo
    print(f"\n[Rolando teste de {atributo_nome.capitalize()}]")
    time.sleep(1)
    print(f"[d20: {d20} + {atributo_nome.capitalize()}: {valor_atributo} = {total}] (Dificuldade: {dificuldade})")
    time.sleep(1)
    return total >= dificuldade

def iniciar_combate(jogador, nome_inimigo, hp_inimigo, min_dano, max_dano):
    layout.imprimir_lento(f"\n⚔️ COMBATE INICIADO: {nome_inimigo.upper()} ⚔️")
    
    bonus_armadura = jogador.get("bonus_defesa", 0)
    mod_defesa = (jogador.get("destreza", 10) + jogador.get("kenjutsu", 10)) // 4
    defesa_jogador = 10 + mod_defesa + bonus_armadura
    bonus_ataque_inimigo = max_dano // 2
    
    while hp_inimigo > 0 and jogador["vitalidade"] > 0:
        layout.divisoria()
        max_hp = jogador.get("max_vitalidade", jogador["vitalidade"])
        print(f"♥ Seu HP: {jogador['vitalidade']}/{max_hp}  |  🛡️ Sua Defesa: {defesa_jogador}  |  💀 HP do Inimigo: {hp_inimigo}")
        
        # O menu de combate reage se a espada estiver quebrada!
        if jogador.get("espada_quebrada", False):
            print("1 - [Atacar] Dar um soco desesperado com o cabo quebrado da arma (Dano Mínimo).")
        else:
            print("1 - [Atacar] Desferir golpe corpo-a-corpo com a lâmina.")
            
        print("2 - [Fugir] Tentar escapar (Teste de Destreza).")
        
        acao = input("Ação (1 ou 2): ").strip()
        
        if acao == "1":
            if jogador.get("espada_quebrada", False):
                layout.imprimir_lento("> Sua espada está QUEBRADA! Você acerta um golpe contundente fraco!")
                dano_jogador = random.randint(1, 3) # Dano pífio
            else:
                bonus_arma = jogador.get("bonus_dano_arma", 0)
                dano_jogador = random.randint(3, 10) + (jogador.get("kenjutsu", 10) // 3) + bonus_arma
                
            layout.imprimir_lento(f"> Causou {dano_jogador} de dano ao inimigo.")
            hp_inimigo -= dano_jogador
            
            if hp_inimigo <= 0:
                layout.imprimir_lento(f"\nCom muito esforço, você derrotou o {nome_inimigo}!")
                return "vitoria"
        
        elif acao == "2":
            if rolar_teste("destreza", jogador.get("destreza", 10), 20):
                layout.imprimir_lento("> Você usa o ambiente e recua para as sombras. Fuga bem-sucedida!")
                return "fuga"
            else:
                layout.imprimir_lento("> Você tenta recuar, mas o inimigo bloqueia seu caminho!")
        else:
            layout.imprimir_lento("> Ação inválida! Você hesita e perde a iniciativa!")
            
        # Turno do inimigo
        if hp_inimigo > 0:
            layout.imprimir_lento(f"\n[Turno do Inimigo: {nome_inimigo}]")
            dado_ataque = random.randint(1, 20)
            total_ataque = dado_ataque + bonus_ataque_inimigo
            time.sleep(0.5)
            print(f" 🎲 O inimigo ataca! (Rolou {dado_ataque} + Bônus {bonus_ataque_inimigo} = {total_ataque}) vs Sua Defesa ({defesa_jogador})")
            time.sleep(0.5)
            
            if total_ataque >= defesa_jogador:
                dano_sofrido = random.randint(min_dano, max_dano)
                layout.imprimir_lento(f"> 💥 O {nome_inimigo} rompe sua guarda e acerta o golpe! Você perde {dano_sofrido} de HP.")
                jogador["vitalidade"] -= dano_sofrido
            else:
                if dado_ataque <= 5:
                    layout.imprimir_lento(f"> 💨 O {nome_inimigo} erra grosseiramente o alvo. Você sai ileso!")
                else:
                    layout.imprimir_lento(f"> ⚔️ O {nome_inimigo} ataca, mas você desvia no último segundo!")
            
    if jogador["vitalidade"] <= 0: return "morte"


# ==========================================
# ROTA 1: AS MINAS INFERIORES
# ==========================================
def cena_minas(jogador):
    layout.cabecalho("AS MINAS DE ENXOFRE E O PESO DO AÇO")

    layout.imprimir_lento(
        "Você desce para as Minas Inferiores. O calor é nauseante, e o eco de picaretas soa como um lamento.\n"
        "Dezenas de humanos escravizados quebram pedras enquanto Magistrados de Ferro os chicoteiam."
    )
    
    print("\nUm dos guardas chuta um ancião exausto. O que você faz?")
    print("1 - [Kenjutsu] Iniciar um massacre sangrento para libertar os escravos.")
    print("2 - [Destreza] Criar uma distração arremessando pedras, e esgueirar-se em silêncio.")
    print("3 - [Conhecimento] Sabotar o duto de gás vulcânico para asfixiar os guardas, sem sujar as mãos.")

    escolha = input("\nEscolha (1, 2 ou 3): ").strip()

    if escolha == "1":
        jogador["honra"] += 2
        layout.imprimir_lento("\nO brilho da Kagekiri traz esperança aos escravos!")
        if rolar_teste("kenjutsu", jogador["kenjutsu"], 22):
            layout.imprimir_lento("SUCESSO! Você perfura as frestas das armaduras. Três caem mortos, o resto foge!")
        else:
            layout.imprimir_lento("FALHA! A armadura deles é grossa. Um guarda te joga no chão!")
            iniciar_combate(jogador, "Pelotão de Ferro", hp_inimigo=40, min_dano=3, max_dano=7)
    elif escolha == "2":
        jogador["honra"] -= 1
        layout.imprimir_lento("\nVocê engole sua empatia e avança furtivamente após jogar as pedras.")
        if not rolar_teste("destreza", jogador["destreza"], 20):
            layout.imprimir_lento("FALHA! Você pisa em uma corrente. Um cão de guarda corre na sua direção!")
            iniciar_combate(jogador, "Cão das Forjas", hp_inimigo=30, min_dano=2, max_dano=6)
    else:
        layout.imprimir_lento("\nVocê quebra a válvula do cano de gás vulcânico.")
        if rolar_teste("conhecimento", jogador["conhecimento"], 21):
            layout.imprimir_lento("SUCESSO! O gás asfixia os guardas. Os escravos fogem em segurança.")
        else:
            layout.imprimir_lento("FALHA! O cano explode na sua cara! Você inala fumaça tóxica.")
            jogador["vitalidade"] -= 5
            iniciar_combate(jogador, "Magistrado Asfixiado", hp_inimigo=35, min_dano=3, max_dano=7)

    if jogador["vitalidade"] <= 0: return jogador
    
    layout.divisoria()
    layout.imprimir_lento(
        "Em um canto da mina, você encontra os restos de um velho ferreiro e recolhe uma de "
        "suas engrenagens para a Kagekiri, adaptando o balanço da arma."
    )
    jogador["kenjutsu"] = jogador.get("kenjutsu", 10) + 1
    print("[Melhoria: Balanço Adaptado (+1 Kenjutsu)]")

    jogador["rota_final_cap3"] = "rio"
    return jogador

# ==========================================
# ROTA 2: A FORJA PRINCIPAL
# ==========================================
def cena_forja(jogador):
    layout.cabecalho("OS PORTÕES PRINCIPAIS E O DEMÔNIO DA BIGORNA")

    layout.imprimir_lento(
        "Você invade a Forja Principal. Rios de magma iluminam um Kama-Oni gigante bebendo ferro derretido.\n"
        "Ele sorri com dentes oxidados: 'A lâmina do herói vai derreter na minha bigorna!'"
    )

    print("\nComo você passa pelo gerente da escravidão?")
    print("1 - [Kenjutsu] Desafiá-lo abertamente para um duelo mortal.")
    print("2 - [Destreza] Correr pelas correntes e tentar derrubar magma nele.")
    
    escolha = input("\nEscolha (1 ou 2): ").strip()

    if escolha == "1":
        jogador["honra"] += 3
        if rolar_teste("kenjutsu", jogador["kenjutsu"], 24):
            layout.imprimir_lento("SUCESSO! Você desliza a lâmina pelo martelo dele e corta seus dedos. Ele recua sangrando!")
            iniciar_combate(jogador, "Kama-Oni (Ferido)", hp_inimigo=30, min_dano=2, max_dano=6)
        else:
            layout.imprimir_lento("FALHA! A martelada treme a montanha e o arremessa longe!")
            iniciar_combate(jogador, "Kama-Oni Bruto", hp_inimigo=50, min_dano=5, max_dano=10)
    else:
        if rolar_teste("destreza", jogador["destreza"], 23):
            layout.imprimir_lento("SUCESSO! Toneladas de magma caem sobre ele. Sua casca endurece e ele morre paralisado em pedra!")
        else:
            layout.imprimir_lento("FALHA! Você escorrega da corrente e queima o braço no magma (-5 HP)!")
            jogador["vitalidade"] -= 5
            iniciar_combate(jogador, "Kama-Oni Furioso", hp_inimigo=50, min_dano=5, max_dano=10)

    if jogador["vitalidade"] <= 0: return jogador

    layout.imprimir_lento("\nNa base da forja do Oni derrotado, você acha lingotes raros e raspa sua própria Kagekiri neles.")
    jogador["kenjutsu"] = jogador.get("kenjutsu", 10) + 1
    print("[Melhoria: Fio Afiado (+1 Kenjutsu)]")

    jogador["rota_final_cap3"] = "rio"
    return jogador

# ==========================================
# ROTA 3: A TRILHA DA FUMAÇA
# ==========================================
def cena_fumaca(jogador):
    layout.cabecalho("OS DUTOS DE FUMAÇA E A ESCALADA MORTAL")

    layout.imprimir_lento(
        "Você ignora o chão e escala as chaminés vulcânicas verticais, invisível para as patrulhas.\n"
        "Subitamente, a fumaça cria olhos brancos. Um Enenra (Yokai de Fumaça) tenta sufocá-lo!"
    )

    print("\nO ar está acabando. O monstro é intangível. Como agir?")
    print("1 - [Conhecimento] Fazer um selo de vento Onmyodo para dissipá-lo.")
    print("2 - [Destreza] Criar uma faísca raspando a espada na pedra para explodir o gás.")

    escolha = input("\nEscolha (1 ou 2): ").strip()

    if escolha == "1":
        if rolar_teste("conhecimento", jogador["conhecimento"], 22):
            layout.imprimir_lento("SUCESSO! O mantra expulsa o demônio do duto. O caminho está limpo.")
        else:
            layout.imprimir_lento("FALHA! A fumaça entra nos pulmões. Você tosse sangue (-5 HP)!")
            jogador["vitalidade"] -= 5
    else:
        if rolar_teste("destreza", jogador["destreza"], 23):
            layout.imprimir_lento("SUCESSO! A mini explosão queima o monstro e o impulsiona para a saída!")
        else:
            layout.imprimir_lento("FALHA! A explosão queima suas roupas e atira você contra a parede (-6 HP).")
            jogador["vitalidade"] -= 6

    if jogador["vitalidade"] <= 0: return jogador
    jogador["rota_final_cap3"] = "montanha"
    return jogador

# ==========================================
# O CLÍMAX DO CAPÍTULO E A QUEDA DO HERÓI
# ==========================================
def cena_climax(jogador):
    if jogador["vitalidade"] <= 0: return jogador
    
    layout.cabecalho("O CORAÇÃO DO VULCÃO E A NOITE ESCURA")

    layout.imprimir_lento(
        "Independente do caminho tomado, todas as passagens de saída o forçam a cruzar a "
        "câmara central onde o magma é drenado da montanha.\n"
        "Lá está o General de Magma, o guardião mestre das Forjas. Seu corpo é feito de rocha derretida e "
        "ódio humano destilado. Ele ruge, fazendo o chão de pedra tremer, e avança!"
    )
    
    # O combate épico
    resultado = iniciar_combate(jogador, "General de Magma", hp_inimigo=60, min_dano=5, max_dano=12)
    if resultado == "morte" or jogador["vitalidade"] <= 0: return jogador
    
    # A QUEDA DA ESPADA
    layout.cabecalho("O ESTILHAÇAR DA ESPERANÇA")

    layout.imprimir_lento(
        "O General cai de joelhos, o magma esfriando em seu peito onde você cravou sua espada. "
        "Ofegante, você puxa a Kagekiri para finalizar o serviço...\n"
        "...Mas o aço de meteorito sagrado, acostumado ao frio eterno do Monte Shiro, sofreu "
        "um estresse térmico fatal ao mergulhar no sangue demoníaco a milhares de graus.\n"
        "Com um som agudo e ensurdecedor, a Kagekiri se parte. A lâmina lendária explode "
        "em vários estilhaços brilhantes. O General vira cinzas, mas o preço foi incalculável. "
        "Sua arma, a herança do seu mestre, está destruída."
    )
    
    jogador["espada_quebrada"] = True
    
    layout.imprimir_lento(
        "Os alarmes do vulcão começam a soar. O estrondo do monstro caindo atrai Guardas Negros "
        "para o local. Você olha para o cabo inútil em sua mão. Sem sua espada, você é apenas um alvo."
    )
    
    # A FUGA SEM ARMAS
    print("\nOs passos se aproximam. Como você foge da montanha desarmado?")
    print("1 - [Destreza] 'O vento sobrevive à queda'. Escorregar pelos dutos de rejeito até a base do vulcão.")
    print("2 - [Conhecimento] 'A mente oculta o corpo'. Misturar-se às cinzas e aos escravos mortos para sair com os destroços.")
    
    escolha_fuga = input("\nEscolha (1 ou 2): ").strip()
    
    layout.imprimir_lento("O desespero dita suas ações. O coração bate no pescoço...")
    if escolha_fuga == "1" and rolar_teste("destreza", jogador["destreza"], 22):
        layout.imprimir_lento("SUCESSO! Você despenca pelas tubulações quentes no escuro, fugindo da morte certa.")
    elif escolha_fuga == "2" and rolar_teste("conhecimento", jogador["conhecimento"], 22):
        layout.imprimir_lento("SUCESSO! Engolindo seu orgulho, você rola na fuligem e finge ser um cadáver jogado aos esgotos. Você escapa invisível.")
    else:
        layout.imprimir_lento("FALHA! Durante a fuga caótica, lanças e brasas encontram sua carne! Você tropeça e rola encosta abaixo.")
        dano = random.randint(8, 15)
        jogador["vitalidade"] -= dano
        print(f"Você perdeu {dano} de Vitalidade e capota para fora das fronteiras de Tetsu.")

    if jogador["vitalidade"] <= 0: return jogador

    # A MEMÓRIA DA ESPERANÇA
    layout.divisoria()
    layout.imprimir_lento(
        "Mutilado, queimado e com as mãos tremendo em volta de um cabo de espada quebrado, "
        "você desaba nas bordas de um novo território.\n"
        "O calor sufocante fica para trás. Você sente lama fria sob seu rosto e o cheiro "
        "de água estagnada e arrozais infinitos. A Província de Mizu.\n"
        "A escuridão ameaça levar sua consciência, mas uma memória antiga de Kazunari o mantém "
        "acordado: 'Se a lâmina falhar, Ishido, busque as águas rasas de Mizu. O maior forjador do mundo, "
        "Mestre Kajiya, foi exilado lá há trinta anos. Se ele ainda viver, apenas ele pode moldar o meteorito.'\n"
        "Você aperta os estilhaços no bolso. A caçada ao mago Kuroi terá que esperar. "
        "Agora, sua única missão é sobreviver à úmida província sem poder lutar."
    )

    return jogador

# ==========================================
# GESTOR DO CAPÍTULO 3
# ==========================================
def jogar(jogador):
    layout.cabecalho("CAPÍTULO 3: AS FORJAS DA DESONRA")

    layout.imprimir_lento("Você caminha sob a abóboda vulcânica da Província de Tetsu. Diante de você, 3 entradas.")

    print("\nOpções de Infiltração:")
    print("1 - As Minas Inferiores (Foco: Passar sorrateiramente pelos escravos e sabotagem).")
    print("2 - Os Portões da Forja (Foco: Confronto letal e brutalidade direta).")
    print("3 - A Trilha da Fumaça (Foco: Escalada vertical secreta e asfixiante).")

    escolha_caminho = input("\nPor onde você se infiltrará no vulcão? (1, 2 ou 3): ").strip()

    if escolha_caminho == "1":
        jogador = cena_minas(jogador)
    elif escolha_caminho == "2":
        jogador = cena_forja(jogador)
    elif escolha_caminho == "3":
        jogador = cena_fumaca(jogador)
    else:
        print("Sua indecisão te custa caro. Você inala fumaça tóxica.")
        jogador["vitalidade"] -= 3
        return jogar(jogador)

    if jogador["vitalidade"] <= 0: return jogador
    
    # O CLÍMAX E A QUEDA DA ESPADA
    jogador = cena_climax(jogador)
    
    return jogador