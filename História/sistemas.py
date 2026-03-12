# sistemas.py
import time
import random

def slow_print(texto, atraso=0.03):
    """Imprime o texto aos poucos para dar um efeito de RPG de terminal."""
    for char in texto:
        print(char, end="", flush=True)
        time.sleep(atraso)
    print("\n")

def menu_evolucao(jogador):
    """Exibe as opções de evolução, aumenta o HP máximo e cura um valor específico."""
    
    # 1. EVOLUÇÃO DO HP MÁXIMO (Rola 1d6 e adiciona permanentemente)
    aumento_hp = random.randint(1, 6)
    
    # Se o jogador não tinha o atributo "max_vitalidade", define agora baseado na vitalidade atual.
    max_vitalidade_atual = jogador.get("max_vitalidade", jogador.get("vitalidade", 15))
    jogador["max_vitalidade"] = max_vitalidade_atual + aumento_hp
    
    # 2. CURA DO DESCANSO (Rola 1d6 extra porque ele parou na fogueira)
    cura_descanso = random.randint(1, 6)
    
    # Aumenta a vida atual com o que ganhou de máximo + o bônus do descanso
    cura_total = aumento_hp + cura_descanso
    jogador["vitalidade"] += cura_total
    
    # Trava a vida atual para não ultrapassar o novo teto máximo
    if jogador["vitalidade"] > jogador["max_vitalidade"]:
        jogador["vitalidade"] = jogador["max_vitalidade"]
    
    print("\n[Meditação Concluída]")
    print(f"Sua resistência física aumentou! (+{aumento_hp} de HP Máximo)")
    print(f"A fogueira fechou algumas feridas superficiais (+{cura_descanso} de Cura).")
    print(f"♥ Seu HP agora é: {jogador['vitalidade']}/{jogador['max_vitalidade']}")

    print("\nAo olhar para as chamas, em qual ensinamento você foca para aprimorar seu espírito?")
    print("1 - [O Caminho da Espada] O peso do combate real afiou seus cortes. (+3 em Kenjutsu)")
    print("2 - [O Caminho do Vento] Escapar da morte acelerou seus reflexos. (+3 em Destreza)")
    print("3 - [O Caminho da Mente] Os horrores do mundo expandiram sua compreensão. (+3 em Conhecimento)")

    escolha = input("\nEscolha sua evolução (1, 2 ou 3): ").strip()

    if escolha == "1":
        jogador["kenjutsu"] = jogador.get("kenjutsu", 10) + 3
        slow_print("\nSeus braços estão mais firmes. A Kagekiri parece mais leve e mortal em suas mãos.")
    elif escolha == "2":
        jogador["destreza"] = jogador.get("destreza", 10) + 3
        slow_print("\nSeu corpo memorizou o perigo. Você sente que pode se mover quase imperceptível nas sombras.")
    elif escolha == "3":
        jogador["conhecimento"] = jogador.get("conhecimento", 10) + 3
        slow_print("\nOs padrões da feitiçaria e os costumes obscuros agora são mais claros para a sua mente.")
    else:
        slow_print("\nVocê apenas esvazia a mente. A intuição guiará seus próximos passos de forma equilibrada.")
        jogador["kenjutsu"] = jogador.get("kenjutsu", 10) + 1
        jogador["destreza"] = jogador.get("destreza", 10) + 1
        jogador["conhecimento"] = jogador.get("conhecimento", 10) + 1
    
    return jogador

def evoluir_capitulo_1(jogador):
    print("\n" + "="*60)
    slow_print("                    O DESCANSO DO GUERREIRO - FIM DO ATO I")
    print("="*60 + "\n")

    rota = jogador.get("rota_cap1", "estrada")

    if rota == "estrada":
        slow_print(
            "Você encontra um casebre abandonado nos limites da Vila de Kiku, "
            "seguro o bastante para acender uma pequena fogueira que não solta fumaça."
        )
        slow_print(
            "A exaustão cobra seu preço. Você limpa o sangue negro dos Guardas de Cinza da sua lâmina. "
            "Os olhos vazios e aterrorizados dos camponeses da vila assombram sua mente. "
            "Kazunari falava de um império glorioso, mas a realidade é feita de lama e escravidão humana."
        )
    elif rota == "caverna":
        slow_print(
            "Abrigado em uma fenda estreita no desfiladeiro, o vento uiva lá fora como espíritos em agonia. "
            "Você acende uma fogueira minúscula com fungos secos."
        )
        slow_print(
            "O cheiro de enxofre e o lodo ácido do Tsuchigumo ainda impregnam suas roupas. "
            "Enfrentar uma fera daquele tamanho no escuro provou que os contos de ninar de Kazunari "
            "eram reais... e mortais. O mundo lá fora não é dos homens, é dos monstros."
        )

    slow_print(
        "A teoria do topo da montanha tornou-se a prática da sobrevivência. "
        "Sua mente e seu corpo estão se adaptando rapidamente à brutalidade do mundo de Kuroi Shin'en."
    )

    jogador = menu_evolucao(jogador)
    return jogador

def evoluir_capitulo_2(jogador):
    print("\n" + "="*60)
    slow_print("                    O DESCANSO DO GUERREIRO - FIM DO ATO II")
    print("="*60 + "\n")

    rota = jogador.get("rota_cap2", "chao")

    if rota == "chao":
        slow_print(
            "Você se abriga sob as raízes colossais e retorcidas da fronteira da Floresta Murmurante. "
            "O ar aqui é quente, anunciando a proximidade da Província vulcânica de Tetsu."
        )
        slow_print(
            "Você lava a lama do pântano de suas botas. A lembrança dos Ronins corrompidos que "
            "abandonaram o código samurai, e a crueldade do Kappa escravista, queimam em seu peito. "
            "A desonra manchou o mundo inteiro, e você é a única lâmina capaz de limpá-la."
        )
    elif rota == "copas":
        slow_print(
            "Você descansa nos galhos mais altos antes que as árvores deem lugar às rochas afiadas "
            "de basalto negro. O calor das forjas distantes já aquece a noite fria."
        )
        slow_print(
            "As ilusões cruéis da feitiçaria testaram seu coração, tentando usar o rosto do seu mestre. "
            "E o duelo com o orgulhoso Daitengu provou que nem todos os Yokais servem a Kuroi, "
            "alguns apenas seguem suas próprias leis ancestrais de aço e vento."
        )

    slow_print(
        "Com a Floresta para trás, seu espírito forjou uma nova camada de resiliência. "
        "Você respira fundo, fundindo suas memórias em pura força de vontade."
    )

    jogador = menu_evolucao(jogador)
    return jogador