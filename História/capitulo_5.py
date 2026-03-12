# capitulo_5.py
import time
import random

def slow_print(texto, atraso=0.03):
    for char in texto:
        print(char, end="", flush=True)
        time.sleep(atraso)
    print("\n")

def rolar_teste(atributo_nome, valor_atributo, dificuldade=20):
    d20 = random.randint(1, 20)
    total = d20 + valor_atributo
    print(f"\n[Rolando teste de {atributo_nome.capitalize()}]")
    time.sleep(1)
    print(f"[d20: {d20} + {atributo_nome.capitalize()}: {valor_atributo} = {total}] (Dificuldade: {dificuldade})")
    time.sleep(1)
    return total >= dificuldade

def iniciar_combate_torre(jogador, nome_inimigo, hp_inimigo, min_dano, max_dano):
    """Combate especial do Cap 5: Inclui hordas e o Roubo de Vida Lunar."""
    slow_print(f"\n⚔️ COMBATE INICIADO: {nome_inimigo.upper()} ⚔️")
    
    bonus_armadura = jogador.get("bonus_defesa", 0)
    mod_defesa = (jogador.get("destreza", 10) + jogador.get("kenjutsu", 10)) // 4
    defesa_jogador = 10 + mod_defesa + bonus_armadura
    bonus_ataque_inimigo = max_dano // 2
    
    while hp_inimigo > 0 and jogador["vitalidade"] > 0:
        print("\n" + "-"*50)
        max_hp = jogador.get("max_vitalidade", jogador["vitalidade"])
        print(f"♥ Seu HP: {jogador['vitalidade']}/{max_hp}  |  🛡️ Sua Defesa: {defesa_jogador}  |  💀 HP Inimigo: {hp_inimigo}")
        
        print("1 - [Arte Nitoryu: Eclipse] Atacar com o Sol e a Lua (Ataque Múltiplo + Roubo de Vida).")
        print("2 - [Fugir] Tentar escapar para a sala anterior (Teste de Destreza).")
        
        acao = input("Ação (1 ou 2): ").strip()
        
        if acao == "1":
            # Dano Massivo do Daisho
            bonus_arma = jogador.get("bonus_dano_arma", 6)
            dano_jogador = random.randint(5, 12) + (jogador.get("kenjutsu", 10) // 2) + bonus_arma
            
            slow_print(f"> A Kagekiri queima como um sol escuro! Você causa {dano_jogador} de dano ao inimigo.")
            hp_inimigo -= dano_jogador
            
            # MECÂNICA DO LUAR: Roubo de Vida (Cura 50% do dano causado)
            cura_lunar = dano_jogador // 2
            jogador["vitalidade"] = min(max_hp, jogador["vitalidade"] + cura_lunar)
            slow_print(f"> A Mizukiri brilha com o luar! O sangue inimigo revitaliza você (+{cura_lunar} HP).")
            
            if hp_inimigo <= 0:
                slow_print(f"\nOs corpos caem aos seus pés. Você sobreviveu ao combate!")
                return "vitoria"
        
        elif acao == "2":
            if rolar_teste("destreza", jogador.get("destreza", 10), 22):
                slow_print("> Você usa as sombras e recua para a sala anterior. Fuga bem-sucedida!")
                return "fuga"
            else:
                slow_print("> Você tenta recuar, mas a horda bloqueia a porta!")
        else:
            slow_print("> Ação inválida! Você hesita!")
            
        # Turno do Inimigo
        if hp_inimigo > 0:
            slow_print(f"\n[Turno Inimigo: {nome_inimigo}]")
            dado_ataque = random.randint(1, 20)
            total_ataque = dado_ataque + bonus_ataque_inimigo
            time.sleep(0.5)
            print(f" 🎲 O inimigo ataca! (Rolou {dado_ataque} + Bônus {bonus_ataque_inimigo}) vs Sua Defesa ({defesa_jogador})")
            time.sleep(0.5)
            
            if total_ataque >= defesa_jogador:
                dano_sofrido = random.randint(min_dano, max_dano)
                slow_print(f"> 💥 O ataque rompe sua guarda! Você perde {dano_sofrido} de HP.")
                jogador["vitalidade"] -= dano_sofrido
            else:
                slow_print(f"> ⚔️ Suas duas espadas giram como um redemoinho, bloqueando o ataque perfeito!")
            
    if jogador["vitalidade"] <= 0: return "morte"


# ==========================================
# CENA 1: A ENTRADA E O LABIRINTO (ANDAR INFERIOR)
# ==========================================
def labirinto_andar_1(jogador):
    print("\n" + "="*60)
    slow_print("          A TORRE DO ABISMO - O LABIRINTO DAS SOMBRAS")
    print("="*60 + "\n")

    slow_print(
        "Você cruza os antigos portões da Província Central. Onde outrora ficava o majestoso Castelo "
        "do seu pai, o Xogum, agora se ergue a Torre do Abismo. Uma estrutura colossal de obsidiana viva, "
        "com veias pulsantes de magia negra que sobem até as nuvens tempestuosas."
    )
    slow_print(
        "Kuroi Shin'en sabe que você está aqui. O palácio foi torcido magicamente em um labirinto mortal."
    )
    
    # Variáveis de controle do Labirinto
    progresso_andar = False
    porta_direita_limpa = False
    porta_esquerda_limpa = False

    while not progresso_andar and jogador["vitalidade"] > 0:
        print("\n" + "-"*50)
        slow_print("Você está no Hall das Ilusões (Andar 1). Existem três corredores massivos.")
        print("1 - O Corredor da Esquerda (Cheira a ervas antigas e sangue pisado).")
        print("2 - O Corredor da Direita (Ecoa com o som de múltiplas armaduras batendo).")
        print("3 - A Grande Escadaria Central (Selada por uma porta com escrituras arcanas).")
        
        escolha = input("\nPara onde você segue? (1, 2 ou 3): ").strip()
        
        if escolha == "1":
            if porta_esquerda_limpa:
                slow_print("Você já saqueou este corredor. Não há mais nada além de cadáveres.")
            else:
                slow_print("\nVocê entra no Corredor da Esquerda. É a antiga Enfermaria da Guarda.")
                slow_print("De repente, o chão cede! Paredes com espetos se fecham na sua direção!")
                if rolar_teste("destreza", jogador.get("destreza", 10), 23):
                    slow_print(
                        "SUCESSO! Você salta pelas paredes, quicando entre as lâminas mortais "
                        "e aterrissa no final da sala ileso."
                    )
                    slow_print(
                        "No altar preservado, você encontra um frasco brilhante com o brasão Shiro. "
                        "Um Elixir Imperial ancestral!"
                    )
                    jogador["max_vitalidade"] += 15
                    jogador["vitalidade"] = jogador["max_vitalidade"]
                    slow_print("[Loot Épico: Elixir Imperial bebido! (+15 HP Máximo e Cura Total!)]")
                    porta_esquerda_limpa = True
                else:
                    dano = random.randint(10, 18)
                    jogador["vitalidade"] -= dano
                    slow_print(f"FALHA! Você é rasgado pelos espetos antes de conseguir rolar para fora (-{dano} HP). A armadilha destrói a sala. Beco sem saída.")
                    porta_esquerda_limpa = True # Destruída
                    
        elif escolha == "2":
            if porta_direita_limpa:
                slow_print("Apenas as cinzas dos mortos-vivos restam neste corredor.")
            else:
                slow_print("\nVocê entra no Antigo Arsenal. Três Guardas de Elite Reanimados e dois Mastins Demônios se viram para você!")
                slow_print("Eles atacam em sincronia. Uma horda implacável!")
                resultado = iniciar_combate_torre(jogador, "Horda do Arsenal (5 Inimigos)", hp_inimigo=85, min_dano=6, max_dano=14)
                
                if resultado == "vitoria":
                    slow_print("Com sua fúria lunar, você dizimou o esquadrão inteiro. Em uma arca trancada, você encontra poeira de cristal.")
                    jogador.setdefault("inventario", []).append("Pó de Estrela")
                    print("[Item Adicionado: Pó de Estrela (Aumenta os sentidos mágicos no futuro)]")
                    porta_direita_limpa = True
                elif resultado == "fuga":
                    slow_print("Você foge de volta para o Hall Principal, ofegante.")
                    
        elif escolha == "3":
            slow_print("\nVocê se aproxima da porta da Escadaria Central. Ela não tem fechadura, apenas uma charada Yokai entalhada a fogo.")
            slow_print(
                "'Sou a fome que não tem estômago. Devoro a madeira, derreto o aço, e o vento me dá asas. "
                "Mas se a água me tocar, eu morro. O que sou eu?'"
            )
            print("1 - O Sangue")
            print("2 - O Fogo")
            print("3 - O Medo")
            print("4 - [Usar Conhecimento] Tentar decifrar as runas ao redor para burlar o enigma.")
            
            resposta = input("\nQual a sua resposta? ").strip()
            
            if resposta == "2":
                slow_print("SUCESSO! A porta de pedra se fragmenta em cinzas. O caminho para o Andar Superior está aberto!")
                progresso_andar = True
            elif resposta == "4":
                if rolar_teste("conhecimento", jogador.get("conhecimento", 10), 24):
                    slow_print("SUCESSO! Sua mente afiada reconhece o feitiço de selamento. Você usa o cabo da espada para raspar a runa central, destrancando a porta!")
                    progresso_andar = True
                else:
                    slow_print("FALHA! As runas brilham em vermelho e disparam um relâmpago arcano no seu peito!")
                    jogador["vitalidade"] -= 10
                    print("Você toma 10 de dano mágico e é arremessado para trás.")
            else:
                slow_print("Resposta incorreta! A porta cospe uma bola de chamas em você!")
                jogador["vitalidade"] -= 10
                print("Você toma 10 de dano por queimaduras.")
        else:
            print("Você perde tempo andando em círculos.")

    return jogador

# ==========================================
# CENA 2: A ASCENSÃO E O TERROR DUPLO
# ==========================================
def labirinto_andar_2(jogador):
    if jogador["vitalidade"] <= 0: return jogador

    print("\n" + "="*60)
    slow_print("          O JARDIM DE CARNE E A DUPLA ABOMINAÇÃO")
    print("="*60 + "\n")

    slow_print(
        "Você sobe as escadas e chega ao Pátio Interno. O que era um lindo jardim zen com lago de carpas "
        "foi corrompido. As árvores choram seiva vermelha e as pedras flutuam com gravidade zero."
    )
    slow_print(
        "O silêncio é quebrado por asas batendo e cascos pesados. Do céu escuro, mergulham DUAS abominações "
        "conjuntas criadas para proteger os aposentos de Kuroi."
    )
    slow_print(
        "À sua esquerda pousa um Tengu da Tempestade (Senhor dos Ventos). À sua direita, aterrissa um "
        "Gashadokuro (Um esqueleto gigante de 5 metros forjado com os ossos dos samurais mortos)."
    )
    
    print("\nO ataque deles será simultâneo. A vida e a morte se fundem neste combate. Como iniciar a luta?")
    print("1 - [Kenjutsu] Avançar frontalmente rodopiando as duas espadas como um tornado de lâminas.")
    print("2 - [Conhecimento] Focar primeiro no elo de magia necromântica do esqueleto gigante.")
    
    tem_po_estrela = "Pó de Estrela" in jogador.get("inventario", [])
    if tem_po_estrela:
        print("3 - [Item] Lançar o 'Pó de Estrela' no ar para cegar o Tengu e expor os pontos fracos de ambos.")

    escolha = input("\nEscolha (1, 2" + (" ou 3" if tem_po_estrela else "") + "): ").strip()
    
    vantagem_boss = False

    if escolha == "1":
        if rolar_teste("kenjutsu", jogador["kenjutsu"], 25):
            slow_print("SUCESSO! O impacto da sua investida decepa a perna do esqueleto e corta a asa do Tengu antes da luta começar!")
            vantagem_boss = True
        else:
            slow_print("FALHA! O vendaval do Tengu te atira contra o punho do Esqueleto Gigante!")
            jogador["vitalidade"] -= 12
            print("Você perde 12 HP pelo esmagamento!")

    elif escolha == "2":
        if rolar_teste("conhecimento", jogador["conhecimento"], 24):
            slow_print("SUCESSO! Você nota um selo de papel no crânio do monstro de osso. Você arremessa uma adaga improvisada e rasga o selo, cortando o HP da criatura pela metade!")
            vantagem_boss = True
        else:
            slow_print("FALHA! Você tenta focar, mas a velocidade do Tengu é monstruosa. Ele rasga suas costas com garras afiadas!")
            jogador["vitalidade"] -= 10
            print("Você perde 10 HP na emboscada!")
            
    elif escolha == "3" and tem_po_estrela:
        slow_print("Você arremessa o pó estelar! A magia residual cega os monstros e interrompe a sincronia deles. Você tem a vantagem absoluta!")
        vantagem_boss = True
        jogador.get("inventario").remove("Pó de Estrela")
        jogador["honra"] += 1

    # Define a dificuldade do combate duplo
    if vantagem_boss:
        hp_dupla = 80
        dano_max = 14
    else:
        hp_dupla = 110
        dano_max = 20 # Letal se ele não defender bem!

    if jogador["vitalidade"] > 0:
        resultado = iniciar_combate_torre(jogador, "Tengu & Gashadokuro (Dupla)", hp_inimigo=hp_dupla, min_dano=8, max_dano=dano_max)
        
        if resultado == "morte" or jogador["vitalidade"] <= 0: return jogador
        
        slow_print("\nVocê crava a Kagekiri no peito do Tengu e gira a Mizukiri explodindo o crânio do gigante.")
        slow_print("A magia se desfaz. As portas imensas no fundo do jardim se abrem sozinhas, rangendo como almas atormentadas.")
        
    return jogador

# ==========================================
# CENA 3: A ANTECÂMARA E O FIM DA ESCALADA
# ==========================================
def transicao_boss(jogador):
    if jogador["vitalidade"] <= 0: return jogador
    
    print("\n" + "="*60)
    slow_print("          A ANTECÂMARA DO ABISMO")
    print("="*60 + "\n")

    slow_print(
        "Banhado no sangue e fuligem de dezenas de bestas, você cruza as portas duplas e adentra "
        "a Antecâmara do Salão do Trono."
    )
    slow_print(
        "O corredor final é forrado de estátuas dos antigos Xoguns da sua linhagem. Todos com os "
        "rostos deformados pela corrupção. A respiração pesa. A presença arcana é tão forte "
        "que o próprio ar vibra em roxo e preto."
    )
    slow_print(
        "No final do corredor majestoso repousa um portão de ouro negro. Atrás dele, "
        "no topo da torre, o Feiticeiro Kuroi Shin'en detém o poder absoluto do Disco do Abismo."
    )
    
    slow_print(
        "Você olha para as suas duas lâminas. Elas pulsam em harmonia com as batidas do seu coração. "
        "Há vinte anos, Kazunari fugiu desta mesma sala com você, apenas um bebê em prantos. "
        "Hoje, o herdeiro voltou. E ele não está chorando."
    )
    
    slow_print("\nO Labirinto foi vencido. O destino de Takenoko será decidido no confronto final.")

    return jogador


# ==========================================
# GESTOR DO CAPÍTULO 5
# ==========================================
def jogar(jogador):
    print("\n" + "=" * 75)
    slow_print("                   CAPÍTULO 5: A TORRE DO ABISMO", 0.05)
    print("=" * 75)

    slow_print(
        "\nO estilo Nitoryu tornou você uma lenda letal nas planícies, mas a torre que perfura as "
        "nuvens exige mais do que apenas aço. Exige a mente fria de um verdadeiro samurai."
    )

    jogador = labirinto_andar_1(jogador)
    if jogador["vitalidade"] <= 0: return jogador
    
    jogador = labirinto_andar_2(jogador)
    if jogador["vitalidade"] <= 0: return jogador
    
    jogador = transicao_boss(jogador)
    
    return jogador