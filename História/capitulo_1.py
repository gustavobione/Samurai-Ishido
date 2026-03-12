# capitulo_1.py
import time
import random


def slow_print(texto, atraso=0.03):
    for char in texto:
        print(char, end="", flush=True)
        time.sleep(atraso)
    print("\n")


def rolar_teste(atributo_nome, valor_atributo, dificuldade=25):
    """Rola 1d20 + Atributo para testar o sucesso de uma ação."""
    d20 = random.randint(1, 20)
    total = d20 + valor_atributo
    print(f"\n[Rolando teste de {atributo_nome.capitalize()}]")
    time.sleep(1)
    print(
        f"[d20: {d20} + {atributo_nome.capitalize()}: {valor_atributo} = {total}] (Dificuldade: {dificuldade})"
    )
    time.sleep(1)
    return total >= dificuldade


def cena_estrada(jogador):
    slow_print("Você escolhe a Antiga Estrada Imperial.")
    slow_print(
        "O que Kazunari descrevia como um caminho de pedras brancas e cerejeiras, "
        "agora é uma trilha de lama negra ladeada por árvores mortas e retorcidas."
    )
    slow_print(
        "Após algumas horas de descida, você ouve vozes ásperas e o choro de uma criança."
    )
    slow_print(
        "Escondido nos arbustos, você vê três Guardas de Cinza — humanos com a pele pálida "
        "e olhos negros, corrompidos pela magia de Kuroi. Eles estão extorquindo um mercador e sua filha."
    )

    print("\nO que você faz?")
    print(
        "1 - [Kenjutsu] Sacar a Kagekiri e atacar os guardas de frente pela honra do mercador."
    )
    print(
        "2 - [Destreza] Esgueirar-se pelas sombras e evitar o conflito. A missão é mais importante."
    )
    print(
        "3 - [Conhecimento] Observar os guardas para lembrar dos ensinamentos de Kazunari sobre corrupção."
    )

    escolha = input("\nEscolha (1, 2 ou 3): ").strip()

    if escolha == "1":
        slow_print(
            f"\nVocê salta dos arbustos, a Kagekiri brilhando com uma luz fantasmagórica!"
        )
        jogador["honra"] += 2
        print("[Honra +2] Um samurai não ignora os indefesos.")

        if rolar_teste("kenjutsu", jogador["kenjutsu"], 24):
            slow_print(
                "SUCESSO! Seus movimentos são como o vento. A lâmina corta a feitiçaria "
                "que anima os guardas antes que possam reagir. Eles viram pó e o mercador foge agradecido."
            )
        else:
            slow_print(
                "FALHA! Você mata dois, mas o terceiro crava uma adaga enferrujada no seu flanco "
                "antes de cair."
            )
            dano = random.randint(3, 8)
            jogador["vitalidade"] -= dano
            print(
                f"Você perdeu {dano} de Vitalidade. (HP Atual: {jogador['vitalidade']})"
            )

    elif escolha == "2":
        slow_print(
            "\nVocê abaixa a cabeça, ignora os gritos e se move silenciosamente pela floresta morta."
        )
        jogador["honra"] -= 3
        print("[Honra -3] A covardia mancha a sua alma.")

        if rolar_teste("destreza", jogador["destreza"], 22):
            slow_print(
                "SUCESSO! Você passa como um fantasma, preservando suas forças para os perigos reais."
            )
        else:
            slow_print(
                "FALHA! Um galho estala sob seu pé. Um dos guardas atira uma flecha envenenada às cegas "
                "que rasga seu ombro."
            )
            dano = random.randint(2, 6)
            jogador["vitalidade"] -= dano
            print(
                f"Você perdeu {dano} de Vitalidade. (HP Atual: {jogador['vitalidade']})"
            )

    elif escolha == "3":
        slow_print(
            "\nVocê respira fundo, fechando os olhos e lembrando das noites frias na fogueira."
        )
        if rolar_teste("conhecimento", jogador["conhecimento"], 23):
            slow_print(
                "SUCESSO! Você lembra: Guardas de Cinza são cegos na luz do sol, eles enxergam "
                "pelo calor. Você cobre seu corpo com a lama gelada do chão e passa direto por eles "
                "sem ser notado, deixando o mercador à própria sorte."
            )
            jogador["honra"] -= 1
            print("[Honra -1] Uma tática engenhosa, mas fria.")
        else:
            slow_print(
                "FALHA! Você tenta lembrar, mas a raiva nubla sua mente. Você demora demais e eles "
                "te farejam. Uma luta desesperada se inicia."
            )
            dano = random.randint(4, 10)
            jogador["vitalidade"] -= dano
            print(
                f"Você os derrota com dificuldade, mas sofre ferimentos. Perdeu {dano} de Vitalidade."
            )
    else:
        print("Opção inválida. Hesitar em batalha é sangrar.")
        jogador["vitalidade"] -= 2
        cena_estrada(jogador)  # Reinicia a cena se digitar errado

    return jogador


def cena_caverna(jogador):
    slow_print(
        "Você escolhe as Cavernas da Mandíbula, um atalho escuro que corta a montanha por dentro."
    )
    slow_print(
        "O ar aqui cheira a enxofre e sangue velho. O silêncio é absoluto, quebrado apenas "
        "pelo gotejar da água gelada."
    )
    slow_print(
        "No meio da escuridão, dois olhos amarelos se abrem. Um Tsuchigumo, um Yokai aranha "
        "do tamanho de uma carroça, bloqueia a passagem com sua teia de fios cortantes."
    )

    print("\nO que você faz?")
    print(
        "1 - [Kenjutsu] Desferir o 'Corte da Lótus', focando toda sua força para decepar as pernas da fera."
    )
    print(
        "2 - [Destreza] Correr pelas paredes da caverna usando as estalactites para saltar por cima do Yokai."
    )
    print(
        "3 - [Conhecimento] Fazer o selo de mãos Onmyodo que Kazunari lhe ensinou para espantar demônios menores."
    )

    escolha = input("\nEscolha (1, 2 ou 3): ").strip()

    if escolha == "1":
        slow_print(f"\nVocê empunha a Kagekiri com as duas mãos e avança rugindo!")
        if rolar_teste("kenjutsu", jogador["kenjutsu"], 26):
            slow_print(
                "SUCESSO! Um corte limpo e brilhante. A lâmina meteorítica destrói a essência do Yokai, "
                "que derrete em uma poça de lodo negro. O caminho está livre."
            )
            jogador["honra"] += 1
            print("[Honra +1] Fúria e precisão.")
        else:
            slow_print(
                "FALHA! A carapaça do monstro é dura demais. Sua espada resvala e ele o atinge "
                "com uma pata afiada antes de recuar para as sombras."
            )
            dano = random.randint(5, 12)
            jogador["vitalidade"] -= dano
            print(
                f"Você perdeu {dano} de Vitalidade. (HP Atual: {jogador['vitalidade']})"
            )

    elif escolha == "2":
        slow_print("\nVocê guarda a espada e se prepara para o salto acrobático.")
        if rolar_teste("destreza", jogador["destreza"], 25):
            slow_print(
                "SUCESSO! Você quica na parede úmida, gira no ar passando milímetros acima das quelíceras "
                "da criatura e aterrissa suavemente do outro lado da teia. O Yokai silva, frustrado."
            )
        else:
            slow_print(
                "FALHA! A pedra esfarela sob sua bota. Você cai na beirada da teia e a aranha o morde "
                "enquanto você luta para se soltar."
            )
            dano = random.randint(6, 10)
            jogador["vitalidade"] -= dano
            print(f"O veneno queima suas veias. Você perdeu {dano} de Vitalidade.")

    elif escolha == "3":
        slow_print(
            "\nVocê crava a espada no chão, une os dedos polegar e indicador e canta o mantra da purificação."
        )
        if rolar_teste("conhecimento", jogador["conhecimento"], 24):
            slow_print(
                "SUCESSO! As palavras antigas ecoam na caverna. O Yokai recua, apavorado pela aura "
                "que emana de você, e se esconde no teto. Você passa ileso."
            )
        else:
            slow_print(
                "FALHA! Você troca uma sílaba do mantra. A magia falha em chamas escuras. "
                "O monstro, enfurecido pelo barulho, investe violentamente contra você."
            )
            dano = random.randint(4, 12)
            jogador["vitalidade"] -= dano
            print(
                f"Você sofreu {dano} de dano antes de afugentá-lo com cortes selvagens."
            )
    else:
        print("Opção inválida. A escuridão não espera indecisos.")
        jogador["vitalidade"] -= 2
        cena_caverna(jogador)

    return jogador


def jogar(jogador):
    print("\n" + "=" * 75)
    slow_print("                   CAPÍTULO 1: A QUEDA DO MUNDO", 0.05)
    print("=" * 75)

    slow_print(
        f"\nA descida da montanha é árdua. A temperatura aumenta, mas a sensação de morte no ar "
        f"torna o clima sufocante. Na base do cume principal, a trilha se divide em duas."
    )

    print("\nOpções de Caminho:")
    print(
        "1 - A Estrada Imperial (Caminho aberto, probabilidade de encontrar humanos e patrulhas)."
    )
    print("2 - As Cavernas da Mandíbula (Atalho imerso em escuridão, covil de feras).")

    escolha_caminho = input("\nPor onde você seguirá? (1 ou 2): ").strip()

    print("\n" + "-" * 50)

    if escolha_caminho == "1":
        jogador = cena_estrada(jogador)
    elif escolha_caminho == "2":
        jogador = cena_caverna(jogador)
    else:
        print("Sem saber para onde ir, você vagueia e perde o equilíbrio nas pedras.")
        jogador["vitalidade"] -= 1
        return jogar(jogador)  # Retorna para tentar novamente

    print("-" * 50)
    slow_print(
        "\nApós sobreviver ao obstáculo, a fumaça de fogueiras atinge o seu nariz."
    )
    slow_print("As árvores se abrem, revelando a Vila de Kiku (Crisântemo Murcho).")
    slow_print(
        "O que sobrou da vila, na verdade. As casas de madeira estão apodrecidas, e os camponeses "
        "olham para você com olhos vazios, como gado esperando o abate."
    )

    return jogador
