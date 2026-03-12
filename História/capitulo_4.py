# capitulo_4.py
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
        max_hp = jogador.get("max_vitalidade", jogador.get("vitalidade", 100))
        print(f"♥ Seu HP: {jogador['vitalidade']}/{max_hp}  |  🛡️ Sua Defesa: {defesa_jogador}  |  💀 HP do Inimigo: {hp_inimigo}")
        
        # Menu de ataque dinâmico baseado no status das espadas
        if jogador.get("espada_quebrada", False):
            print("1 - [Atacar] Dar um soco desesperado com o cabo inútil (Dano Mínimo).")
        elif jogador.get("duas_espadas_longas", False):
            print("1 - [Arte Nitoryu: Eclipse] Atacar com o Sol Negro e a Lua Prateada (Dano Maciço + Roubo de Vida).")
        else:
            print("1 - [Atacar] Desferir golpe com a lâmina.")
            
        print("2 - [Fugir] Tentar escapar (Teste de Destreza).")
        
        acao = input("Ação (1 ou 2): ").strip()
        
        if acao == "1":
            if jogador.get("espada_quebrada", False):
                layout.imprimir_lento("> Sua espada está QUEBRADA! Você bate com o cabo, causando quase nada de dano!")
                dano_jogador = random.randint(1, 3) 
                layout.imprimir_lento(f"> Causou {dano_jogador} de dano ao inimigo.")
                hp_inimigo -= dano_jogador
                
            elif jogador.get("duas_espadas_longas", False):
                # Mecânica Épica: Sol e Lua
                bonus_arma = jogador.get("bonus_dano_arma", 6)
                # Dano ampliado pela fúria de duas espadas
                dano_jogador = random.randint(5, 12) + (jogador.get("kenjutsu", 10) // 2) + bonus_arma
                
                layout.imprimir_lento(f"> A Kagekiri (Sol Negro) incinera a guarda do inimigo! Causou {dano_jogador} de dano bruto.")
                hp_inimigo -= dano_jogador
                
                # Roubo de vida da Lua Prateada (Cura 50% do dano causado)
                cura_lunar = dano_jogador // 2
                jogador["vitalidade"] = min(max_hp, jogador["vitalidade"] + cura_lunar)
                layout.imprimir_lento(f"> A Mizukiri (Lua Prateada) brilha intensamente! A essência do inimigo cura suas feridas (+{cura_lunar} HP).")
                
            else:
                bonus_arma = jogador.get("bonus_dano_arma", 0)
                dano_jogador = random.randint(3, 10) + (jogador.get("kenjutsu", 10) // 3) + bonus_arma
                layout.imprimir_lento(f"> Você desferiu um golpe preciso! Causou {dano_jogador} de dano ao inimigo.")
                hp_inimigo -= dano_jogador
            
            if hp_inimigo <= 0:
                layout.imprimir_lento(f"\nO inimigo desaba. Você sobreviveu ao {nome_inimigo}!")
                return "vitoria"
        
        elif acao == "2":
            if rolar_teste("destreza", jogador.get("destreza", 10), 20):
                layout.imprimir_lento("> Você mergulha na água turva e escapa com vida!")
                return "fuga"
            else:
                layout.imprimir_lento("> Você escorrega na lama e o inimigo bloqueia sua fuga!")
        else:
            layout.imprimir_lento("> Você hesita!")
            
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
                layout.imprimir_lento(f"> 💥 O golpe rasga sua carne! Você perde {dano_sofrido} de HP.")
                jogador["vitalidade"] -= dano_sofrido
            else:
                if jogador.get("duas_espadas_longas", False):
                    layout.imprimir_lento(f"> ⚔️ Você cruza o Sol e a Lua e defende o impacto esmagador sem dar um passo para trás!")
                else:
                    layout.imprimir_lento(f"> 💨 Você rola pela lama e esquiva do golpe por um triz!")
            
    if jogador["vitalidade"] <= 0: return "morte"


# ==========================================
# CENA 1: A VULNERABILIDADE E OS CAMINHOS DE MIZU
# ==========================================
def cena_caminhos_mizu(jogador):
    layout.cabecalho("OS ARROZAIS TURVOS E O PESO DO FRACASSO")

    layout.imprimir_lento(
        "A Província de Mizu é um cemitério afogado. Sem a Kagekiri, a escuridão parece "
        "pressionar o seu corpo. A água fria bate na sua cintura. Você sente a ausência da "
        "sua lâmina não apenas na mão, mas na alma."
    )
    
    if not jogador.get("penalidade_espada_aplicada"):
        jogador["kenjutsu"] -= 10
        jogador["penalidade_espada_aplicada"] = True
        print("\n" + "!"*50)
        print(" [Aviso: Sem uma lâmina para aparar golpes e atacar, seu Kenjutsu foi reduzido em -10!]")
        print(" [Sua Defesa passiva despencou. O combate agora é letal.]")
        print("!"*50 + "\n")

    layout.imprimir_lento(
        "Diante de você, o rio lamacento se divide. "
        "À esquerda, enormes Portões Torii erguem-se da água. O ar lá vibra com uma poderosa aura mágica Yokai. "
        "À direita, os restos de uma Vila de Pescadores em chamas, afundando na lama sob ataque de saqueadores."
    )

    print("\nPara onde você se arrastará na escuridão?")
    print("1 - [O Enigma Místico] Seguir para os Portões Torii. Enfrentar os deuses da água sem espada.")
    print("2 - [A Furtividade] Seguir para a Vila Flutuante. Tentar salvar inocentes sem poder lutar de frente.")

    escolha_rota = input("\nEscolha o caminho (1 ou 2): ").strip()

    if escolha_rota == "1":
        layout.imprimir_lento(
            "\nVocê escolhe os portões. A água borbulha violentamente e dezenas de metros de escamas "
            "esverdeadas emergem. É um Mizuchi Maior, um dragão de rio com DUAS cabeças de serpente.\n"
            "Cabeça Esquerda (Voz sibilante): 'Um ronin quebrado... as águas ocultam o ferreiro exilado.'\n"
            "Cabeça Direita (Voz grave): 'Apenas um portão leva ao mestre. O outro leva à morte.'\n"
            "Cabeça Esquerda: 'Nós sabemos o caminho. Mas eu só digo mentiras.'\n"
            "Cabeça Direita: 'E eu só digo verdades. Você tem direito a uma única pergunta a uma das cabeças.'"
        )

        print("\nO combate é suicídio. Como você resolve o enigma?")
        print("1 - [Conhecimento] Fazer a clássica pergunta lógica: 'Se eu perguntasse à outra cabeça qual o caminho seguro, o que ela diria?'.")
        print("2 - [Honra] Erigir a postura do clã Shiro, mostrar os estilhaços e exigir respeito pela sua linhagem.")

        escolha_dragao = input("\nEscolha (1 ou 2): ").strip()

        if escolha_dragao == "1":
            if rolar_teste("conhecimento", jogador["conhecimento"], 18):
                layout.imprimir_lento(
                    "SUCESSO! A cabeça sibila. 'Ela diria para ir pela direita...'. Sendo a mentirosa, "
                    "você sabe que a resposta foi invertida. O caminho real é a ESQUERDA. O dragão, fascinado, "
                    "cospe uma escama cintilante aos seus pés e afunda."
                )
                jogador.setdefault("inventario", []).append("Escama de Mizuchi")
                print("[Item Adicionado: Escama de Mizuchi (Protege contra magias de água/gelo)]")
                jogador["honra"] += 1
            else:
                layout.imprimir_lento("FALHA! Sua pergunta é confusa. As cabeças riem: 'Patético!' Elas disparam um jato de água fervente!")
                jogador["vitalidade"] -= 10
                print("Você toma 10 de dano e é arrastado pela correnteza para o lado esquerdo!")

        elif escolha_dragao == "2":
            if jogador.get("honra", 10) >= 15:
                layout.imprimir_lento(
                    "As cabeças paralisam ao ver o aço meteorítico, mesmo quebrado. 'A honra do Xogum ainda respira. "
                    "Passe, herdeiro.' Elas se curvam e revelam o caminho da esquerda, entregando-lhe uma bênção."
                )
                jogador.setdefault("inventario", []).append("Escama de Mizuchi")
                print("[Item Adicionado: Escama de Mizuchi (Protege contra magias de água/gelo)]")
            else:
                layout.imprimir_lento(
                    "As cabeças riem. 'Suas ações não têm a honra necessária para suportar essa autoridade, covarde!' "
                    "O dragão chicoteia você com a cauda!"
                )
                iniciar_combate(jogador, "Mizuchi Decepcionado", hp_inimigo=30, min_dano=5, max_dano=10)

    else:
        layout.imprimir_lento(
            "\nVocê se arrasta pela lama até a vila. Homens-sapo (Bandidos Corrompidos) estão saqueando "
            "as palafitas e amarrando pescadores."
        )
        print("\nSem sua Kagekiri, um combate direto contra 10 saqueadores é a morte. O que você faz?")
        print("1 - [Destreza] Nadar por baixo das casas e sabotar os pilares, derrubando os bandidos na água para os crocodilos.")
        print("2 - [Conhecimento] Roubar uma tocha e botar fogo nos próprios juncos de arroz, criando fumaça para os moradores fugirem.")

        escolha_vila = input("\nEscolha (1 ou 2): ").strip()

        if escolha_vila == "1":
            if rolar_teste("destreza", jogador["destreza"], 20):
                layout.imprimir_lento(
                    "SUCESSO! Você remove os pinos como um fantasma aquático. O deque desaba. Os bandidos "
                    "caem gritando no rio cheio de feras. Um dos aldeões, antes de fugir, joga um amuleto "
                    "em suas mãos em agradecimento."
                )
                jogador.setdefault("inventario", []).append("Amuleto da Maré")
                print("[Item Adicionado: Amuleto da Maré (Aumenta destreza em ambientes com água)]")
                jogador["honra"] += 2
            else:
                layout.imprimir_lento("FALHA! Um dos sapos nota sua sombra na água e atira um arpão rústico em seu ombro!")
                jogador["vitalidade"] -= 8
                print("Você toma 8 de dano e precisa fugir arrastando-se pela lama.")
        else:
            if rolar_teste("conhecimento", jogador["conhecimento"], 19):
                layout.imprimir_lento(
                    "SUCESSO! A fumaça espessa de palha molhada cega os inimigos. O caos reina. Você guia "
                    "as crianças para a margem segura."
                )
                jogador["honra"] += 2
            else:
                layout.imprimir_lento("FALHA! A palha está molhada demais. O fogo apaga. Você atrai a atenção de três bandidos armados!")
                iniciar_combate(jogador, "Trio de Homens-Sapo", hp_inimigo=35, min_dano=4, max_dano=8)

    return jogador


# ==========================================
# CENA 2: A FORJA CELESTIAL E A DUALIDADE
# ==========================================
def cena_forja_sagrada(jogador):
    if jogador["vitalidade"] <= 0: return jogador

    layout.cabecalho("A CAVERNA DE CRISTAL E AS LÂMINAS GÊMEAS")

    layout.imprimir_lento(
        "Seguindo o rio até sua nascente secreta, você encontra uma colossal cortina d'água escondida "
        "por salgueiros chorões brancos. Atravessando-a, você entra num santuário divino.\n"
        "Ao lado de uma fonte de água incandescente, um homem idoso e cego, com braços maiores que troncos, "
        "martela uma bigorna de jade. Mestre Kajiya, o maior forjador do Japão.\n"
        "Ele para. 'Você traz o cheiro de desespero e poeira vulcânica... "
        "mas no seu bolso, canta o aço das estrelas. Mostre-me.'\n"
        "Você deposita os três estilhaços da Kagekiri na bigorna.\n"
        "'A lâmina não falhou. Ela apenas não foi feita para lutar sozinha', o Mestre diz calmamente. "
        "'Beba das Águas Sagradas enquanto eu moldo a verdadeira natureza do clã Shiro.'"
    )
    
    jogador["vitalidade"] = jogador.get("max_vitalidade", 100)
    print("\n[Mística] Você bebe das águas brilhantes. Suas feridas se fecham. Suas cicatrizes somem.")
    print(f"♥ Vitalidade totalmente restaurada! (HP: {jogador['vitalidade']})")
    time.sleep(1)

    layout.imprimir_lento(
        "Por três dias, as marteladas de Kajiya ecoam. Ao amanhecer do quarto dia, ele se aproxima "
        "com duas bainhas imponentes. Duas katanas longas e perfeitas.\n"
        "1. A **Kagekiri** (Corta-Sombras), fundida com os minérios do vulcão. Ela agora é o **Sol Negro**, "
        "uma lâmina cor de ônix projetada para rasgar armaduras com calor e força bruta.\n"
        "2. A **Mizukiri** (Corta-Águas), forjada das areias azuis do rio. Ela é a **Lua Prateada**, "
        "uma lâmina fluida abençoada com a magia do rio capaz de sugar a essência vital dos inimigos a cada corte.\n"
        "'Você lutou com uma mão em honra ao seu mestre. Mas você tem dois braços, Ishido. "
        "Domine o Sol e a Lua. O Estilo Nitoryu. Levante-se.'"
    )

    jogador["espada_quebrada"] = False
    jogador["duas_espadas_longas"] = True
    
    jogador["kenjutsu"] += 15 
    jogador["destreza"] += 3 
    jogador["bonus_dano_arma"] = 6 
    jogador["penalidade_espada_aplicada"] = False

    print("\n" + "*"*55)
    print("      ⚔️ RENASCIMENTO: A ARTE DO ECLIPSE ⚔️")
    print(" [Atributos Restaurados e Elevados: Kenjutsu +5, Destreza +3]")
    print(" [Bônus Passivo: +6 de Dano Base]")
    print(" [Habilidade Adquirida: 'Luar' (Cura 50% do Dano Causado!)]")
    print("*"*55 + "\n")

    return jogador


# ==========================================
# CENA 3: O CLÍMAX - TESTANDO O SOL E A LUA
# ==========================================
def cena_boss_aquatico(jogador):
    if jogador["vitalidade"] <= 0: return jogador

    layout.cabecalho("A INVASÃO DO SENHOR DAS ÁGUAS TURVAS")

    layout.imprimir_lento(
        "Assim que você prende as duas katanas no obi (cinto), a caverna treme violentamente. "
        "A cachoeira sagrada na entrada fica negra como piche.\n"
        "A água irrompe. Um gigantesco Nushi (Guardião Corrompido do Rio) rasteja para dentro. "
        "Ele tem o corpo de uma serpente de água lamacenta e empunha uma âncora de navio imensa.\n"
        "'EU SINTO O CHEIRO DA MAGIA ANTIGA!', ele ruge, a água apodrecendo o solo do santuário. "
        "'O Mago Kuroi ordenou a morte do ferreiro cego!'\n"
        "Mestre Kajiya recua. Você dá um passo à frente. O Sol Negro em sua mão direita absorve a luz, "
        "enquanto a Lua Prateada na mão esquerda brilha intensamente. Você sorri."
    )

    tem_amuleto = "Amuleto da Maré" in jogador.get("inventario", [])
    tem_escama = "Escama de Mizuchi" in jogador.get("inventario", [])

    dano_maximo_boss = 16

    if tem_amuleto or tem_escama:
        print("\n[Vantagem de Equipamento]")
        if tem_amuleto:
            print("- O Amuleto da Maré estabiliza seus pés na água. (+2 na Defesa Passiva!)")
            jogador["bonus_defesa"] = jogador.get("bonus_defesa", 0) + 2
        if tem_escama:
            print("- A Escama do Dragão anula o miasma aquático. (Ataques do Boss causarão menos dano máximo!)")
            dano_maximo_boss -= 3

    # COMBATE FINAL DO CAPÍTULO 4
    resultado = iniciar_combate(jogador, "Nushi das Águas Turvas", hp_inimigo=90, min_dano=6, max_dano=dano_maximo_boss)

    if resultado == "morte" or jogador["vitalidade"] <= 0: return jogador

    layout.divisoria()
    layout.imprimir_lento(
        "Com um movimento de tesoura fulminante, você dispara a Arte do Eclipse. "
        "O Sol Negro derrete e estilhaça a âncora do monstro. Num piscar de olhos, a Lua Prateada "
        "atravessa o pescoço da fera, banhando sua lâmina em luz e finalizando o combate.\n"
        "A água sagrada chove pelo santuário, purificando o pântano ao redor. "
        "Mestre Kajiya cai de joelhos, sentindo a energia da natureza voltar ao normal. "
        "'O guerreiro perfeito... O império de Kuroi finalmente conhecerá o medo.'"
    )

    return jogador


# ==========================================
# GESTOR DO CAPÍTULO 4
# ==========================================
def jogar(jogador):
    layout.cabecalho("CAPÍTULO 4: AS ÁGUAS DO LAMENTO")

    if jogador.get("espada_quebrada", False):
        print("\n[Aviso do Sistema: Você está desarmado. Entrar em combates sem usar Conhecimento ou Destreza será letal.]")

    jogador = cena_caminhos_mizu(jogador)
    if jogador["vitalidade"] <= 0: return jogador
    
    jogador = cena_forja_sagrada(jogador)
    if jogador["vitalidade"] <= 0: return jogador

    jogador = cena_boss_aquatico(jogador)
    
    layout.imprimir_lento("\nO rio agora flui limpo, carregando as cinzas para longe. O caminho para a Torre do Abismo está escancarado.")
    
    return jogador