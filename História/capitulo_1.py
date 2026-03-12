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
    print(f"[d20: {d20} + {atributo_nome.capitalize()}: {valor_atributo} = {total}] (Dificuldade: {dificuldade})")
    time.sleep(1)
    return total >= dificuldade

def iniciar_combate(jogador, nome_inimigo, hp_inimigo, min_dano, max_dano):
    """Inicia um loop de combate simples."""
    slow_print(f"\n⚔️ COMBATE INICIADO: {nome_inimigo.upper()} ⚔️")
    
    while hp_inimigo > 0 and jogador["vitalidade"] > 0:
        print("\n" + "-"*40)
        print(f"♥ Seu HP: {jogador['vitalidade']}  |  💀 HP do Inimigo: {hp_inimigo}")
        print("1 - [Atacar] Desferir golpe com a Kagekiri.")
        print("2 - [Fugir] Tentar escapar (Teste de Destreza).")
        
        acao = input("Ação (1 ou 2): ").strip()
        
        if acao == "1":
            # Dano do jogador é baseado em um d10 + metade do Kenjutsu
            dano_jogador = random.randint(3, 10) + (jogador.get("kenjutsu", 10) // 2)
            slow_print(f"> Você avança e corta o inimigo! Causou {dano_jogador} de dano.")
            hp_inimigo -= dano_jogador
            
            if hp_inimigo <= 0:
                slow_print(f"Com um golpe final perfeito, você derrotou o {nome_inimigo}!")
                return "vitoria"
        
        elif acao == "2":
            # Tentativa de fuga no meio do combate
            if rolar_teste("destreza", jogador.get("destreza", 10), 22):
                slow_print("> Você joga poeira nos olhos do inimigo e recua para as sombras. Fuga bem-sucedida!")
                return "fuga"
            else:
                slow_print("> Você tenta recuar, mas o inimigo bloqueia seu caminho!")
        else:
            slow_print("> Ação inválida! Você hesita e perde a iniciativa!")
            
        # Turno do inimigo (se ainda estiver vivo)
        if hp_inimigo > 0:
            dano_sofrido = random.randint(min_dano, max_dano)
            slow_print(f"> O {nome_inimigo} contra-ataca brutalmente! Você perdeu {dano_sofrido} de Vitalidade.")
            jogador["vitalidade"] -= dano_sofrido
            
    if jogador["vitalidade"] <= 0:
        return "morte"

# ==========================================
# ROTA 1: ESTRADA IMPERIAL
# ==========================================
def cena_estrada(jogador):
    print("\n" + "="*60)
    slow_print("          A ESTRADA IMPERIAL E A VILA DE KIKU")
    print("="*60 + "\n")

    slow_print(
        "'A Estrada Imperial, meu jovem, era um rio de pétalas de cerejeira na primavera...', "
        "a voz cansada de Kazunari ecoa na sua mente enquanto você desce a encosta."
    )
    slow_print(
        "A realidade, porém, é um pesadelo. A pedra branca foi engolida por uma lama espessa "
        "que cheira a ferrugem. As cerejeiras estão mortas, seus galhos retorcidos parecem "
        "mãos esqueléticas implorando aos céus cinzentos."
    )
    slow_print(
        "Após algumas horas de marcha tensa, um som corta o silêncio: o choro de uma criança."
    )
    slow_print(
        "Você se esgueira por trás das raízes podres de uma árvore e observa. Três guerreiros bloqueiam a estrada. "
        "Eles vestem as armaduras distorcidas do antigo clã Shiro, mas a pele deles é cinza como cinzas de fogueira, "
        "e os olhos são poços de escuridão pura. Guardas de Cinza. Mortais corrompidos pela magia de Kuroi."
    )
    slow_print(
        "Eles estão revistando a carroça quebrada de um velho mercador. Um dos guardas ergue a neta "
        "do mercador pelos farrapos da roupa, rindo com uma voz que soa como pedras se chocando."
    )

    print("\nO que você faz?")
    print("1 - [Kenjutsu] A honra exige sangue. Sacar a Kagekiri e obliterar os traidores.")
    print("2 - [Destreza] A missão é maior que dois camponeses. Esgueirar-se pelas sombras e deixá-los para trás.")
    print("3 - [Conhecimento] Kazunari ensinou os pontos cegos dos mortos-vivos. Tentar uma tática de distração ilusória.")

    escolha = input("\nEscolha (1, 2 ou 3): ").strip()
    mercador_salvo = False

    if escolha == "1":
        slow_print("\nVocê respira fundo. A fúria aquece seu sangue. A Kagekiri desliza da bainha com um zumbido fantasmagórico.")
        jogador["honra"] += 2
        print("[Honra +2] Um samurai é o escudo dos indefesos.")

        if rolar_teste("kenjutsu", jogador["kenjutsu"], 24):
            slow_print(
                "SUCESSO! Você é um relâmpago azul na lama negra. O primeiro guarda perde a cabeça antes de piscar. "
                "O segundo tenta erguer a lança, mas a lâmina de meteorito corta a haste de ferro e o peito dele de uma só vez. "
                "O terceiro cai de joelhos, virando pó negro."
            )
            mercador_salvo = True
        else:
            slow_print(
                "FALHA! Sua lâmina corta o primeiro, mas a lama escorregadia trai seus pés. "
                "Um dos guardas acerta um golpe brutal de alabarda em suas costelas antes de você decapitá-lo! O sobrevivente avança!"
            )
            resultado = iniciar_combate(jogador, "Guarda de Cinza Restante", hp_inimigo=25, min_dano=4, max_dano=9)
            if resultado == "vitoria":
                mercador_salvo = True

    elif escolha == "2":
        slow_print("\nVocê aperta o cabo da espada, mas engole a raiva. Matar Kuroi salvará milhares. Você não pode arriscar agora.")
        jogador["honra"] -= 3
        print("[Honra -3] Os gritos da criança mancharão seus pesadelos.")

        if rolar_teste("destreza", jogador["destreza"], 22):
            slow_print(
                "SUCESSO! Você se move com o vento. Os guardas estão distraídos demais com a crueldade "
                "e não percebem a sua sombra deslizando pela floresta morta além da estrada."
            )
        else:
            slow_print(
                "FALHA! Um corvo grasna de repente e voa do seu esconderijo. O guarda joga a criança no chão "
                "e atira uma faca de arremesso que crava no seu ombro enquanto você foge! Eles o avistaram!"
            )
            resultado = iniciar_combate(jogador, "Patrulha de Cinza", hp_inimigo=35, min_dano=3, max_dano=7)
            mercador_salvo = False 

    elif escolha == "3":
        slow_print("\nVocê se lembra das noites frias. 'Criaturas de cinza enxergam a vida, não a luz', dizia o mestre.")
        if rolar_teste("conhecimento", jogador["conhecimento"], 23):
            slow_print(
                "SUCESSO! Você quebra uma pedra de enxofre que trazia do cume e a arremessa nas brasas da carroça. "
                "Uma fumaça mística ofusca os sentidos vitais dos guardas. Eles gritam, cegos. O mercador aproveita "
                "o caos e foge com a criança. Você passa despercebido."
            )
            jogador["honra"] -= 1
            print("[Honra -1] Tática engenhosa, mas sem a bravura de um embate direto.")
            mercador_salvo = True 
        else:
            slow_print(
                "FALHA! Você tenta criar o pó ofuscante, mas a umidade da lama estraga a mistura. "
                "Os guardas o farejam. Você é forçado a lutar contra oponentes enfurecidos de uma vez!"
            )
            resultado = iniciar_combate(jogador, "Guardas Enfurecidos", hp_inimigo=40, min_dano=5, max_dano=10)
            if resultado == "vitoria":
                mercador_salvo = True

    else:
        slow_print("A indecisão é a mãe da morte. Os guardas atiram em você antes do combate começar!")
        jogador["vitalidade"] -= 5
        iniciar_combate(jogador, "Patrulha de Cinza", hp_inimigo=35, min_dano=3, max_dano=8)
        mercador_salvo = False

    if jogador["vitalidade"] <= 0: return jogador

    # --- CONTINUAÇÃO DA TRAMA DA ESTRADA ---
    print("\n" + "-"*50)
    
    if mercador_salvo:
        slow_print(
            "Com a estrada segura, o velho mercador se joga aos seus pés, tremendo.\n"
            "'Meu lorde... eu não via as vestes de um samurai há décadas. Pensei que o clã Shiro estava extinto!'"
        )
        slow_print(
            "Ele vasculha os destroços da carroça e estende as mãos trêmulas para você. "
            "Nelas repousa um pedaço de jade bruto, pulsando com uma energia morna.\n"
            "'Tome, por favor. É uma Lágrima de Kami. Iria vender no mercado clandestino, mas pertence a um herói.'"
        )
        jogador.setdefault("inventario", []).append("Lágrima de Kami")
        print("[Item Adicionado: Lágrima de Kami (Pode curar feitiços ou ser usada em rituais)]")

    slow_print(
        "\nVocê continua a descida. Algumas horas depois, a neblina se dissipa ligeiramente, revelando a Vila de Kiku."
    )
    slow_print(
        "'A joia do norte', Kazunari a chamava. Hoje, não passa de um agrupamento de casebres apodrecidos. "
        "Os moradores andam de cabeça baixa, cobrindo os rostos. O medo empapuça o ar."
    )
    slow_print(
        "No centro da vila, a antiga casa de chá foi transformada em um posto de coleta de sangue para os Yokais."
        "Um magistrado humano, gordo e vestido com sedas roubadas, supervisiona a extorsão."
    )

    print("\nComo você vai cruzar a vila em direção à Floresta Murmurante?")
    print("1 - [Ação Direta] Caminhar até o centro, expor a Kagekiri e desafiar o Magistrado corrupto na frente de todos.")
    print("2 - [Furtividade] Ignorar o centro da vila. Usar os telhados e vielas para chegar aos portões da floresta em silêncio.")
    
    escolha_vila = input("\nEscolha (1 ou 2): ").strip()

    if escolha_vila == "1":
        slow_print("\nVocê caminha pesadamente. A cada passo, a aura da sua espada atrai os olhares apavorados dos camponeses.")
        slow_print(
            "O magistrado arregala os olhos ao ver a lâmina. Ele grita por guardas, mas o medo nos olhos dele é o verdadeiro prêmio. "
            "Você abre caminho a força, deixando uma mensagem clara: O Clã Shiro voltou."
        )
        jogador["honra"] += 3
        print("[Honra +3] A esperança foi reacendida no coração do povo.")
        slow_print("Você deixa a vila banhada em caos, adentrando os limites escuros da Floresta Murmurante.")

    elif escolha_vila == "2":
        slow_print("\nVocê é um fantasma. Saltando pelos telhados podres, você observa a miséria lá embaixo.")
        slow_print(
            "Embora seu coração sangre por não ajudar, você sabe que Kuroi Shin'en é o verdadeiro alvo. "
            "Você alcança os muros dos fundos da vila sem ser detectado, saltando para o barro do outro lado."
        )
        slow_print("A neblina densa da Floresta Murmurante o engole instantaneamente.")
    
    else:
        slow_print("Sua hesitação atrai a atenção de cães de guarda corrompidos, forçando-o a correr pelos becos e fugir para a floresta.")

    return jogador

# ==========================================
# ROTA 2: CAVERNAS DA MANDÍBULA
# ==========================================
def cena_caverna(jogador):
    print("\n" + "="*60)
    slow_print("          AS CAVERNAS DA MANDÍBULA E O ABISMO")
    print("="*60 + "\n")

    slow_print(
        "'A escuridão absoluta não é o fim da luz, Ishido. É o berço de coisas muito mais antigas que ela...'\n"
        "O aviso de Kazunari reverbera em sua mente enquanto a luz do dia fica para trás, engolida pelas rochas."
    )
    slow_print(
        "Você escolheu o atalho pelas Cavernas da Mandíbula. O ar aqui é denso, sufocante, "
        "com um cheiro metálico de sangue velho misturado a enxofre. Sob suas botas, não há apenas "
        "pedras, mas o som oco de ossos humanos triturados."
    )
    slow_print(
        "De repente, o gotejar da água para. O silêncio se torna absoluto."
    )
    slow_print(
        "No alto da escuridão, oito olhos amarelos e leitosos se abrem. Um Tsuchigumo, o temido Yokai "
        "aranha das lendas, do tamanho de uma carroça de guerra. Suas quelíceras estalam, e uma "
        "teia cujos fios brilham como arame afiado bloqueia completamente a passagem."
    )

    print("\nO que você faz?")
    print("1 - [Kenjutsu] 'Aço contra carapaça'. Focar toda a sua força no 'Corte da Lótus' para decepar as pernas da fera.")
    print("2 - [Destreza] 'O vento não é pego em redes'. Correr pelas paredes e estalactites, saltando sobre a teia e o monstro.")
    print("3 - [Conhecimento] 'A mente domina a fera'. Executar o selo Onmyodo do fogo fátuo para cegar e espantar o Yokai.")

    escolha = input("\nEscolha (1, 2 ou 3): ").strip()
    yokai_derrotado = False

    if escolha == "1":
        slow_print("\nCom um grito de guerra que ecoa na caverna, você empunha a Kagekiri com as duas mãos e avança!")
        jogador["honra"] += 1
        print("[Honra +1] Enfrentar um demônio de frente exige coragem inabalável.")

        if rolar_teste("kenjutsu", jogador["kenjutsu"], 25):
            slow_print(
                "SUCESSO! O aço de meteorito zune no ar escuro. Seu corte é um arco de luz azul "
                "perfeito. Duas das patas grossas do monstro são decepadas de uma só vez. O Tsuchigumo "
                "grita com um som humano e recua para as fendas do teto, pingando um lodo corrosivo. O caminho está livre."
            )
            yokai_derrotado = True
        else:
            slow_print(
                "FALHA! A carapaça do monstro é dura como ferro fundido. A Kagekiri resvala com faíscas. "
                "O impacto o desequilibra, e a fera avança furiosamente sobre você!"
            )
            resultado = iniciar_combate(jogador, "Tsuchigumo Colossal", hp_inimigo=50, min_dano=5, max_dano=12)
            if resultado == "vitoria": yokai_derrotado = True

    elif escolha == "2":
        slow_print("\nVocê embainha a espada parcialmente. O samurai verdadeiro sabe a hora de não derramar sangue inútil.")
        jogador["honra"] -= 1
        print("[Honra -1] Fugir de uma besta infernal o mantém vivo, mas mancha o orgulho.")

        if rolar_teste("destreza", jogador["destreza"], 24):
            slow_print(
                "SUCESSO! Você é uma sombra ágil. Quicando na parede úmida, você gira no ar, passando "
                "milímetros acima das presas envenenadas da criatura. Você aterrissa rolando do outro lado "
                "da teia impenetrável. A fera silva, frustrada por ter perdido a presa."
            )
        else:
            slow_print(
                "FALHA! O musgo na parede esfarela sob sua bota. Você perde o impulso e cai "
                "direto na borda da teia. Os fios cortam suas roupas como navalhas. O monstro te persegue!"
            )
            resultado = iniciar_combate(jogador, "Tsuchigumo Faminto", hp_inimigo=45, min_dano=4, max_dano=10)
            if resultado == "vitoria": yokai_derrotado = True

    elif escolha == "3":
        slow_print("\nVocê crava a espada na pedra, une os dedos polegar e indicador, e entoa o mantra de Kazunari.")
        if rolar_teste("conhecimento", jogador["conhecimento"], 23):
            slow_print(
                "SUCESSO! As palavras antigas ganham vida. Uma faísca azul salta de seus dedos e "
                "inflama o miasma da caverna. Uma luz cegante e purificadora explode. "
                "O Yokai, acostumado a décadas de escuridão, entra em pânico e foge se arrastando para as profundezas."
            )
            yokai_derrotado = True
        else:
            slow_print(
                "FALHA! Você troca uma única sílaba do mantra complexo. A magia implode em suas mãos "
                "com um estalo abafado, queimando seus dedos. O Yokai, enfurecido pelo barulho, investe."
            )
            resultado = iniciar_combate(jogador, "Tsuchigumo Enfurecido", hp_inimigo=40, min_dano=6, max_dano=14)
            if resultado == "vitoria": yokai_derrotado = True

    else:
        slow_print("Opção inválida. A escuridão não espera indecisos. A besta salta sobre você.")
        iniciar_combate(jogador, "Tsuchigumo", hp_inimigo=45, min_dano=5, max_dano=10)

    if jogador["vitalidade"] <= 0: return jogador

    # --- CONTINUAÇÃO DA TRAMA DA CAVERNA ---
    print("\n" + "-"*50)

    if yokai_derrotado:
        slow_print(
            "Com a passagem agora iluminada pela luz fraca que vem do fim do túnel, "
            "você nota algo preso em um antigo casulo espesso deixado pelo Tsuchigumo no chão."
        )
        slow_print(
            "Você rasga a seda com a espada. Lá dentro estão os restos mortais de um monge guerreiro de Takenoko. "
            "Nas mãos ósseas dele, um pequeno amuleto de bronze em forma de corvo ainda brilha intensamente."
        )
        jogador.setdefault("inventario", []).append("Sino do Corvo de Bronze")
        print("[Item Adicionado: Sino do Corvo de Bronze (Emite um som que revela ilusões de nível baixo)]")

    slow_print(
        "\nVocê avança em direção à luz. O ar frio atinge seu rosto, mas a visão do lado de fora o paralisa."
    )
    slow_print(
        "A caverna não leva à Vila de Kiku. O atalho cuspiu você no alto de um desfiladeiro vertiginoso. "
        "Lá embaixo, estendendo-se até o horizonte, está a vasta e assustadora Floresta Murmurante (Capítulo 2)."
    )
    slow_print(
        "A neblina no nível do solo pulsa como um coração doente. A descida pelo paredão de pedra é íngreme e mortal. "
        "O vento corta o desfiladeiro, trazendo sussurros de espíritos perdidos na floresta abaixo."
    )

    print("\nComo você decide iniciar sua descida para a Floresta Murmurante?")
    print("1 - [Descanso Tático] Montar um acampamento rápido e oculto na boca da caverna para enfaixar ferimentos antes de descer.")
    print("2 - [Determinação Cega] A fúria não descansa. Descer as rochas imediatamente enquanto a adrenalina oculta a dor.")

    escolha_descida = input("\nEscolha (1 ou 2): ").strip()

    if escolha_descida == "1":
        slow_print(
            "\nVocê junta fungos secos e cria uma fogueira minúscula, que não emite luz, apenas calor. "
            "Você medita, limpa a Kagekiri e aperta as ataduras. A memória do seu mestre conforta seu coração."
        )
        cura = random.randint(10, 20)
        jogador["vitalidade"] = min(100, jogador.get("vitalidade", 100) + cura)
        print(f"[Descanso] Você recuperou {cura} de Vitalidade. (HP Atual: {jogador['vitalidade']})")
        slow_print("Com o corpo preparado, você inicia a lenta e cuidadosa descida pelo paredão quando o sol encoberto nasce.")

    elif escolha_descida == "2":
        slow_print(
            "\nKuroi Shin'en não dorme, e você também não. Você guarda a espada nas costas e agarra as pedras pontiagudas, "
            "iniciando uma descida arriscada. A pressa o faz ganhar terreno e tempo."
        )
        jogador["honra"] += 1
        print("[Honra +1] O espírito de um samurai é incansável.")
        slow_print(
            "Você chega à base da floresta muito antes do esperado, ganhando vantagem posicional e evitando as "
            "patrulhas diurnas que rondam a fronteira da mata."
        )
        jogador["vantagem_floresta"] = True

    else:
        slow_print("Hesitando no limite do abismo, uma rajada de vento gelado quase o joga para baixo, forçando-o a descer às pressas.")
        jogador["vitalidade"] -= 2

    return jogador

# ==========================================
# INÍCIO DO CAPÍTULO E ESCOLHA DE ROTA
# ==========================================
def jogar(jogador):
    print("\n" + "=" * 75)
    slow_print("                   CAPÍTULO 1: A QUEDA DO MUNDO", 0.05)
    print("=" * 75)

    slow_print(
        "\nA descida da montanha é árdua. A temperatura aumenta, mas a sensação de morte no ar "
        "torna o clima sufocante. Na base do cume principal, a trilha se divide em duas."
    )

    print("\nOpções de Caminho:")
    print("1 - A Estrada Imperial (Caminho aberto, probabilidade de encontrar humanos e patrulhas).")
    print("2 - As Cavernas da Mandíbula (Atalho imerso em escuridão, covil de feras).")

    escolha_caminho = input("\nPor onde você seguirá? (1 ou 2): ").strip()

    print("\n" + "-" * 50)

    if escolha_caminho == "1":
        jogador["rota_cap1"] = "estrada"
        jogador = cena_estrada(jogador)
    elif escolha_caminho == "2":
        jogador["rota_cap1"] = "caverna"
        jogador = cena_caverna(jogador)
    else:
        print("Sem saber para onde ir, você vagueia e perde o equilíbrio nas pedras.")
        jogador["vitalidade"] -= 3
        return jogar(jogador)

    return jogador