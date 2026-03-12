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
    print(f"Sua resistência ao mundo aumentou! (+{aumento_hp} de HP Máximo)")
    print(f"O calor da fogueira fechou feridas superficiais (+{cura_descanso} de Cura).")
    print(f"♥ Seu HP agora é: {jogador['vitalidade']}/{jogador['max_vitalidade']}")

    print("\nAo olhar para as chamas, em qual ensinamento você foca para aprimorar seu espírito?")
    print("1 - [O Caminho da Espada] O peso do combate real afiou seus cortes. (+3 em Kenjutsu)")
    print("2 - [O Caminho do Vento] Escapar da morte acelerou seus reflexos. (+3 em Destreza)")
    print("3 - [O Caminho da Mente] Os horrores do mundo expandiram sua compreensão. (+3 em Conhecimento)")

    escolha = input("\nEscolha sua evolução (1, 2 ou 3): ").strip()

    if escolha == "1":
        jogador["kenjutsu"] = jogador.get("kenjutsu", 10) + 3
        slow_print("\nSeus braços estão mais firmes. O metal parece menos pesado e seus golpes cortam o ar com facilidade.")
    elif escolha == "2":
        jogador["destreza"] = jogador.get("destreza", 10) + 3
        slow_print("\nSeu corpo memorizou as garras do perigo. Você sente que pode se mover pelas sombras como um fantasma.")
    elif escolha == "3":
        jogador["conhecimento"] = jogador.get("conhecimento", 10) + 3
        slow_print("\nA escuridão não assusta mais. Os padrões da feitiçaria e as fraquezas dos Yokais agora fluem na sua mente.")
    else:
        slow_print("\nVocê apenas esvazia a mente. A intuição cega guiará seus próximos passos de forma equilibrada.")
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
            "Você encontra um casebre de madeira apodrecida nos limites da Vila de Kiku, "
            "afastado o bastante para acender uma pequena fogueira que não solta fumaça na neblina."
        )
        slow_print(
            "A exaustão da sua primeira batalha real cobra o preço nos seus músculos. Você limpa o "
            "sangue negro dos Guardas de Cinza da sua lâmina usando um pano velho."
        )
        slow_print(
            "Os olhos vazios e aterrorizados dos camponeses da vila assombram sua mente. Kazunari, "
            "seu mestre, falava de um império glorioso guiado pela justiça, mas a realidade que você "
            "encontrou é construída sobre lama, corrupção e escravidão humana."
        )
    elif rota == "caverna":
        slow_print(
            "Abrigado em uma fenda estreita no desfiladeiro vertical, o vento noturno uiva do lado "
            "de fora como milhares de espíritos em agonia. Você usa o que resta das suas forças "
            "para acender uma fogueira minúscula com fungos secos."
        )
        slow_print(
            "O cheiro pútrido de enxofre e o lodo ácido que o Tsuchigumo expeliu ainda impregnam suas roupas. "
            "Enfrentar uma fera demoníaca daquele tamanho no escuro absoluto provou que as lendas de horror "
            "que seu mestre contava eram todas reais... e letais."
        )
        slow_print(
            "Você percebeu da pior maneira que o mundo lá fora não pertence mais aos homens; ele foi entregue aos monstros."
        )

    slow_print(
        "A teoria dos treinos no topo da montanha congelada tornou-se a brutal prática da sobrevivência. "
        "Sua mente e seu corpo estão sendo forçados a se adaptar rapidamente à crueldade do império de Kuroi Shin'en."
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
            "Você se abriga sob as raízes colossais e retorcidas no limite leste da Floresta Murmurante. "
            "O ar aqui já não cheira a musgo, mas carrega o bafo quente e sufocante que anuncia a proximidade "
            "da Província vulcânica de Tetsu."
        )
        slow_print(
            "Sentado na terra seca, você raspa a lama do pântano e o sangue demoníaco de suas botas. "
            "A lembrança dos Ronins corrompidos que abandonaram o código samurai por poder e "
            "o som do chicote do Kappa escravista ainda queimam em seu peito."
        )
        slow_print(
            "A desonra manchou o mundo inteiro, e o peso de ser a única lâmina capaz de limpá-la começa a pesar nos seus ombros."
        )
    elif rota == "copas":
        slow_print(
            "Você decide não arriscar o chão e descansa amarrado aos galhos mais altos do dossel, pouco antes "
            "que a imensidão verde dê lugar às rochas afiadas e negras do basalto vulcânico."
        )
        slow_print(
            "O calor distante das forjas do vulcão já aquece a noite fria, mas são as provações do dia que o mantêm acordado. "
            "As ilusões cruéis da feitiçaria, que usaram a voz e o rosto do seu velho mestre para tentar matá-lo, "
            "foram um teste de fogo para o seu coração."
        )
        slow_print(
            "E o duelo silencioso e violento com o imponente Daitengu provou uma verdade complexa: nem todos os Yokais "
            "são servos malignos de Kuroi. Alguns apenas seguem suas próprias, e antigas, leis de vento e aço."
        )

    slow_print(
        "Com a grandiosidade maligna da Floresta para trás, seu espírito forjou uma nova e impenetrável camada de resiliência. "
        "Você respira fundo as cinzas no ar, fundindo suas memórias em pura força de vontade."
    )

    jogador = menu_evolucao(jogador)
    return jogador

def evoluir_capitulo_3(jogador):
    print("\n" + "="*60)
    slow_print("                    O DESCANSO DO GUERREIRO - A QUEDA")
    print("="*60 + "\n")

    slow_print(
        "Encharcado pela neblina gelada da Província de Mizu, seus dedos trêmulos e queimados mal conseguem "
        "produzir a faísca necessária para acender a lenha úmida. O calor minguado do fogo é o único conforto."
    )
    slow_print(
        "Com lágrimas de frustração e dor, você abre um trapo sujo sobre o barro. Lentamente, você alinha os "
        "pedaços rachados, estilhaçados e escuros da sagrada Kagekiri no chão."
    )
    slow_print(
        "A fumaça, o horror, as lutas contra os Onis gigantes e o magma inclemente das Forjas de Tetsu "
        "cobraram o preço mais alto possível. Pela primeira vez desde que você era uma criança chorando nos braços "
        "de Kazunari, você não tem o aço divino para te proteger. Você está vulnerável."
    )
    slow_print(
        "A escuridão dos pântanos ao seu redor murmura com as vozes de criaturas aquáticas à espreita, "
        "farejando o cheiro do seu sangue."
    )
    slow_print(
        "Mas a dor acorda algo primordial. Um samurai desarmado ainda é, e sempre será, um samurai. "
        "O desespero absoluto que você sente agora não o consome, mas aguça seus sentidos para a "
        "sobrevivência como nenhuma vitória épica jamais fez."
    )
    
    return menu_evolucao(jogador)

def evoluir_capitulo_4(jogador):
    print("\n" + "="*60)
    slow_print("                    O DESCANSO DO GUERREIRO - A TEMPESTADE PRESTES A CAIR")
    print("="*60 + "\n")

    slow_print(
        "A poucos metros do Rio purificado, você acende uma fogueira fora da Caverna do Mestre Kajiya. "
        "O cheiro de sândalo e água limpa enche a noite. A luz laranja e vibrante das chamas reflete diretamente "
        "nas lâminas gêmeas que repousam elegantemente no seu colo."
    )
    slow_print(
        "O Sol Negro exala um calor letal, enquanto a Lua Prateada parece derramar uma luz líquida e calmante. "
        "Sobreviver à lama, aos enigmas do Dragão e à crueldade sem a proteção da sua espada original ensinou-lhe a paciência "
        "e a maleabilidade incontrolável da água."
    )
    slow_print(
        "A fraqueza momentânea lapidou o seu orgulho cego, transformando-o em foco absoluto. E agora, com a glória "
        "do estilo Nitoryu fluindo como uma tempestade retida em seus dois braços, você sabe que não há Yokai, "
        "corrupção, feitiçaria ou lorde no mundo capaz de deter a sua caminhada."
    )
    slow_print(
        "O Mago Negro Kuroi Shin'en está sentado no trono roubado do seu pai, no ápice da Torre do Abismo, "
        "completamente alheio à tempestade de aço e vingança que marchará contra seus portões ao amanhecer. "
        "É a véspera do seu julgamento final."
    )
    
    return menu_evolucao(jogador)

def evoluir_capitulo_5(jogador):
    print("\n" + "="*60)
    slow_print("                    O DESCANSO DO GUERREIRO - O LIMIAR DO ABISMO")
    print("="*60 + "\n")

    slow_print(
        "Na grandiosa Antecâmara do Trono, não há o conforto rústico das fogueiras. Há apenas o frio implacável "
        "do piso de mármore obsidiano e o olhar julgador das estátuas colossais dos antigos Xoguns da sua linhagem, "
        "todas deformadas e corrompidas pela magia das sombras."
    )
    slow_print(
        "Você senta em posição de lótus, cruzando as pernas de frente para os imensos Portões de Ouro Negro. "
        "A fadiga quase letal de ter rasgado seu caminho através de hordas infernais, abominações duplas e "
        "armadilhas arcanas começa a desaparecer. O sangue escuro dos monstros escorre lentamente pelas canaletas da torre."
    )
    slow_print(
        "O Sol Negro e a Lua Prateada estão fincadas no mármore ao seu lado. O silêncio é absoluto. "
        "Esta é a sua última e mais profunda meditação. A jornada inteira culmina nestes segundos."
    )
    slow_print(
        "O sacrifício do braço de Kazunari. As lágrimas dos camponeses na vila. As correntes nas Forjas de Tetsu. "
        "O dragão nos arrozais. A libertação de Takenoko e a honra manchada de sangue de seu pai. "
        "Tudo, absolutamente tudo, se resume à entidade diabólica que o aguarda atrás dessa porta."
    )
    
    print("\n[Bênção dos Ancestrais] A aura dos Xoguns mortos reverbera através das lâminas e o fortalece de forma divina.")
    aumento_hp = random.randint(5, 12)
    jogador["max_vitalidade"] += aumento_hp
    jogador["vitalidade"] = jogador["max_vitalidade"] 
    print(f"♥ Vitalidade Máxima e Atual restauradas ao ápice! (+{aumento_hp} HP Máximo)")
    
    print("\nOnde você canalizará todo o espírito de guerra do seu Clã para o duelo contra Kuroi Shin'en?")
    print("1 - [A Fúria do Demônio] O ataque perfeito que reduz montanhas a pó. (+5 Kenjutsu)")
    print("2 - [A Fluidez da Água] A agilidade que desvia a própria magia cósmica. (+5 Destreza)")
    print("3 - [O Olho da Mente] A clareza para enxergar os fios da feitiçaria do Disco do Abismo. (+5 Conhecimento)")
    
    escolha = input("\nEscolha o Transe Final (1, 2 ou 3): ").strip()
    if escolha == "1": 
        jogador["kenjutsu"] += 5
        slow_print("Seu espírito se inflama em pura intenção assassina.")
    elif escolha == "2": 
        jogador["destreza"] += 5
        slow_print("Seu corpo e a gravidade entram em harmonia perfeita.")
    elif escolha == "3": 
        jogador["conhecimento"] += 5
        slow_print("Sua mente afiada como vidro corta os véus da ilusão do castelo.")
    else:
        jogador["kenjutsu"] += 2
        jogador["destreza"] += 2
        jogador["conhecimento"] += 2
        slow_print("A intuição de mil séculos flui de forma equilibrada em seu sangue.")
    
    return jogador