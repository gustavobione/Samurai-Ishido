# capitulo_1.py
import time
import random
import layout

def rolar_teste(atributo_nome, valor_atributo, dificuldade=20):
    """Rola 1d20 + Atributo para testar o sucesso de uma ação."""
    d20 = random.randint(1, 20)
    total = d20 + valor_atributo
    print(f"\n[Rolando teste de {atributo_nome.capitalize()}]")
    time.sleep(1)
    print(f"[d20: {d20} + {atributo_nome.capitalize()}: {valor_atributo} = {total}] (Dificuldade: {dificuldade})")
    time.sleep(1)
    return total >= dificuldade

def iniciar_combate(jogador, nome_inimigo, hp_inimigo, min_dano, max_dano):
    """Inicia um loop de combate simples com sistema de Esquiva/Defesa."""
    layout.imprimir_lento(f"\n⚔️ COMBATE INICIADO: {nome_inimigo.upper()} ⚔️")
    
    # Calcula a sua Defesa (Base 10 + modificador de agilidade e bloqueio)
    mod_defesa = (jogador.get("destreza", 10) + jogador.get("kenjutsu", 10)) // 4
    defesa_jogador = 10 + mod_defesa
    
    # O bônus de ataque do inimigo é baseado no quão forte ele bate
    bonus_ataque_inimigo = max_dano // 2
    
    while hp_inimigo > 0 and jogador["vitalidade"] > 0:
        layout.divisoria()
        max_hp = jogador.get("max_vitalidade", jogador["vitalidade"])
        print(f"♥ Seu HP: {jogador['vitalidade']}/{max_hp}  |  🛡️ Sua Defesa: {defesa_jogador}  |  💀 HP do Inimigo: {hp_inimigo}")
        print("1 - [Atacar] Desferir golpe com a Kagekiri.")
        print("2 - [Fugir] Tentar escapar (Teste de Destreza).")
        
        acao = input("Ação (1 ou 2): ").strip()
        
        if acao == "1":
            dano_jogador = random.randint(3, 10) + (jogador.get("kenjutsu", 10) // 3)
            layout.imprimir_lento(f"> Você avança e corta o inimigo! Causou {dano_jogador} de dano.")
            hp_inimigo -= dano_jogador
            
            if hp_inimigo <= 0:
                layout.imprimir_lento(f"\nCom um golpe final perfeito, você derrotou o {nome_inimigo}!")
                return "vitoria"
        
        elif acao == "2":
            if rolar_teste("destreza", jogador.get("destreza", 10), 22):
                layout.imprimir_lento("> Você joga poeira nos olhos do inimigo e recua para as sombras. Fuga bem-sucedida!")
                return "fuga"
            else:
                layout.imprimir_lento("> Você tenta recuar, mas o inimigo bloqueia seu caminho!")
        else:
            layout.imprimir_lento("> Ação inválida! Você hesita e perde a iniciativa!")
            
        # ==========================================
        # TURNO DO INIMIGO (Rolagem de Acerto)
        # ==========================================
        if hp_inimigo > 0:
            layout.imprimir_lento(f"\n[Turno do Inimigo: {nome_inimigo}]")
            dado_ataque = random.randint(1, 20)
            total_ataque = dado_ataque + bonus_ataque_inimigo
            
            time.sleep(0.5)
            print(f" 🎲 O inimigo ataca! (Rolou {dado_ataque} + {bonus_ataque_inimigo} = {total_ataque}) vs Sua Defesa ({defesa_jogador})")
            time.sleep(0.5)
            
            if total_ataque >= defesa_jogador:
                dano_sofrido = random.randint(min_dano, max_dano)
                layout.imprimir_lento(f"> 💥 O {nome_inimigo} rompe sua guarda e acerta o golpe! Você perde {dano_sofrido} de HP.")
                jogador["vitalidade"] -= dano_sofrido
            else:
                # Narrativa dinâmica para o erro do inimigo
                if dado_ataque <= 5:
                    layout.imprimir_lento(f"> 💨 O {nome_inimigo} ataca, mas erra grosseiramente o alvo. Você sai ileso!")
                else:
                    layout.imprimir_lento(f"> ⚔️ O {nome_inimigo} ataca, mas você apara com a Kagekiri e desvia o golpe no último segundo!")
            
    if jogador["vitalidade"] <= 0:
        return "morte"

# ==========================================
# ROTA 1: ESTRADA IMPERIAL
# ==========================================
def cena_estrada(jogador):
    layout.cabecalho("A ESTRADA IMPERIAL E A VILA DE KIKU")

    layout.imprimir_lento(
        "'A Estrada Imperial, meu jovem, era um rio de pétalas de cerejeira na primavera...', "
        "a voz cansada de Kazunari ecoa na sua mente enquanto você desce a encosta.\n"
        "A realidade, porém, é um pesadelo. A pedra branca foi engolida por uma lama espessa "
        "que cheira a ferrugem. As cerejeiras estão mortas, seus galhos retorcidos parecem "
        "mãos esqueléticas implorando aos céus cinzentos.\n"
        "Após algumas horas de marcha tensa, um som corta o silêncio: o choro de uma criança.\n"
        "Você se esgueira por trás das raízes podres de uma árvore e observa. Três guerreiros bloqueiam a estrada. "
        "Eles vestem as armaduras distorcidas do antigo clã Shiro, mas a pele deles é cinza como cinzas de fogueira, "
        "e os olhos são poços de escuridão pura. Guardas de Cinza. Mortais corrompidos pela magia de Kuroi.\n"
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
        layout.imprimir_lento("\nVocê respira fundo. A fúria aquece seu sangue. A Kagekiri desliza da bainha com um zumbido fantasmagórico.")
        jogador["honra"] += 2
        print("[Honra +2] Um samurai é o escudo dos indefesos.")

        if rolar_teste("kenjutsu", jogador["kenjutsu"], 20):
            layout.imprimir_lento(
                "SUCESSO! Você é um relâmpago azul na lama negra. O primeiro guarda perde a cabeça antes de piscar. "
                "O segundo tenta erguer a lança, mas a lâmina de meteorito corta a haste de ferro e o peito dele de uma só vez. "
                "O terceiro cai de joelhos, virando pó negro."
            )
            mercador_salvo = True
        else:
            layout.imprimir_lento(
                "FALHA! Sua lâmina corta o primeiro, mas a lama escorregadia trai seus pés. "
                "Um dos guardas acerta um golpe contundente nas suas costelas antes de você decapitá-lo! O sobrevivente avança!"
            )
            dano = random.randint(1, 3)
            jogador["vitalidade"] -= dano
            print(f"Você perdeu {dano} de Vitalidade no deslize.")
            resultado = iniciar_combate(jogador, "Guarda de Cinza Restante", hp_inimigo=15, min_dano=1, max_dano=3)
            if resultado == "vitoria":
                mercador_salvo = True

    elif escolha == "2":
        layout.imprimir_lento("\nVocê aperta o cabo da espada, mas engole a raiva. Matar Kuroi salvará milhares. Você não pode arriscar agora.")
        jogador["honra"] -= 3
        print("[Honra -3] Os gritos da criança mancharão seus pesadelos.")

        if rolar_teste("destreza", jogador["destreza"], 19):
            layout.imprimir_lento(
                "SUCESSO! Você se move com o vento. Os guardas estão distraídos demais com a crueldade "
                "e não percebem a sua sombra deslizando pela floresta morta além da estrada."
            )
        else:
            layout.imprimir_lento(
                "FALHA! Um corvo grasna de repente e voa do seu esconderijo. O guarda joga a criança no chão "
                "e atira uma faca de arremesso que crava no seu ombro enquanto você foge! Eles o avistaram!"
            )
            dano = random.randint(1, 2)
            jogador["vitalidade"] -= dano
            print(f"Você perdeu {dano} de Vitalidade.")
            resultado = iniciar_combate(jogador, "Patrulha de Cinza", hp_inimigo=20, min_dano=2, max_dano=4)
            mercador_salvo = False 

    elif escolha == "3":
        layout.imprimir_lento("\nVocê se lembra das noites frias. 'Criaturas de cinza enxergam a vida, não a luz', dizia o mestre.")
        if rolar_teste("conhecimento", jogador["conhecimento"], 18):
            layout.imprimir_lento(
                "SUCESSO! Você quebra uma pedra de enxofre que trazia do cume e a arremessa nas brasas da carroça. "
                "Uma fumaça mística ofusca os sentidos vitais dos guardas. Eles gritam, cegos. O mercador aproveita "
                "o caos e foge com a criança. Você passa despercebido."
            )
            jogador["honra"] -= 1
            print("[Honra -1] Tática engenhosa, mas sem a bravura de um embate direto.")
            mercador_salvo = True 
        else:
            layout.imprimir_lento(
                "FALHA! Você tenta criar o pó ofuscante, mas a umidade da lama estraga a mistura. "
                "Os guardas o farejam. Você é forçado a lutar contra oponentes enfurecidos de uma vez!"
            )
            resultado = iniciar_combate(jogador, "Guardas Enfurecidos", hp_inimigo=25, min_dano=2, max_dano=5)
            if resultado == "vitoria":
                mercador_salvo = True

    else:
        layout.imprimir_lento("A indecisão é a mãe da morte. Os guardas atiram em você antes do combate começar!")
        jogador["vitalidade"] -= 2
        iniciar_combate(jogador, "Patrulha de Cinza", hp_inimigo=20, min_dano=2, max_dano=4)
        mercador_salvo = False

    if jogador["vitalidade"] <= 0: return jogador

    # --- CONTINUAÇÃO DA TRAMA DA ESTRADA ---
    layout.divisoria()
    
    if mercador_salvo:
        layout.imprimir_lento(
            "Com a estrada segura, o velho mercador se joga aos seus pés, tremendo.\n"
            "'Meu lorde... eu não via as vestes de um samurai há décadas. Pensei que o clã Shiro estava extinto!'\n"
            "Ele vasculha os destroços da carroça e estende as mãos trêmulas para você. "
            "Nelas repousa um pedaço de jade bruto, pulsando com uma energia morna.\n"
            "'Tome, por favor. É uma Lágrima de Kami. Iria vender no mercado clandestino, mas pertence a um herói.'"
        )
        jogador.setdefault("inventario", []).append("Lágrima de Kami")
        print("[Item Adicionado: Lágrima de Kami (Pode curar feitiços ou ser usada em rituais)]")

    layout.imprimir_lento(
        "Você continua a descida. Algumas horas depois, a neblina se dissipa ligeiramente, revelando a Vila de Kiku.\n"
        "'A joia do norte', Kazunari a chamava. Hoje, não passa de um agrupamento de casebres apodrecidos. "
        "Os moradores andam de cabeça baixa, cobrindo os rostos. O medo empapuça o ar.\n"
        "No centro da vila, a antiga casa de chá foi transformada em um posto de coleta de sangue para os Yokais."
        "Um magistrado humano, gordo e vestido com sedas roubadas, supervisiona a extorsão."
    )

    print("\nComo você vai cruzar a vila em direção à Floresta Murmurante?")
    print("1 - [Ação Direta] Caminhar até o centro, expor a Kagekiri e desafiar o Magistrado corrupto na frente de todos.")
    print("2 - [Furtividade] Ignorar o centro da vila. Usar os telhados e vielas para chegar aos portões da floresta em silêncio.")
    
    escolha_vila = input("\nEscolha (1 ou 2): ").strip()

    if escolha_vila == "1":
        layout.imprimir_lento(
            "Você caminha pesadamente. A cada passo, a aura da sua espada atrai os olhares apavorados dos camponeses.\n"
            "O magistrado arregala os olhos ao ver a lâmina. Ele grita por guardas, mas o medo nos olhos dele é o verdadeiro prêmio. "
            "Você abre caminho a força, deixando uma mensagem clara: O Clã Shiro voltou."
        )
        jogador["honra"] += 3
        print("[Honra +3] A esperança foi reacendida no coração do povo.")
        layout.imprimir_lento("Você deixa a vila banhada em caos, adentrando os limites escuros da Floresta Murmurante.")

    elif escolha_vila == "2":
        layout.imprimir_lento(
            "Você é um fantasma. Saltando pelos telhados podres, você observa a miséria lá embaixo.\n"
            "Embora seu coração sangre por não ajudar, você sabe que Kuroi Shin'en é o verdadeiro alvo. "
            "Você alcança os muros dos fundos da vila sem ser detectado, saltando para o barro do outro lado.\n"
            "A neblina densa da Floresta Murmurante o engole instantaneamente."
        )
    
    else:
        layout.imprimir_lento("Sua hesitação atrai a atenção de cães de guarda corrompidos, forçando-o a correr pelos becos e fugir para a floresta.")

    return jogador

# ==========================================
# ROTA 2: CAVERNAS DA MANDÍBULA
# ==========================================
def cena_caverna(jogador):
    layout.cabecalho("AS CAVERNAS DA MANDÍBULA E O ABISMO")

    layout.imprimir_lento(
        "'A escuridão absoluta não é o fim da luz, Ishido. É o berço de coisas muito mais antigas que ela...'\n"
        "O aviso de Kazunari reverbera em sua mente enquanto a luz do dia fica para trás, engolida pelas rochas.\n"
        "Você escolheu o atalho pelas Cavernas da Mandíbula. O ar aqui é denso, sufocante, "
        "com um cheiro metálico de sangue velho misturado a enxofre. Sob suas botas, não há apenas "
        "pedras, mas o som oco de ossos humanos triturados.\n"
        "De repente, o gotejar da água para. O silêncio se torna absoluto.\n"
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
        layout.imprimir_lento("\nCom um grito de guerra que ecoa na caverna, você empunha a Kagekiri com as duas mãos e avança!")
        jogador["honra"] += 1
        print("[Honra +1] Enfrentar um demônio de frente exige coragem inabalável.")

        if rolar_teste("kenjutsu", jogador["kenjutsu"], 22):
            layout.imprimir_lento(
                "SUCESSO! O aço de meteorito zune no ar escuro. Seu corte é um arco de luz azul "
                "perfeito. Duas das patas grossas do monstro são decepadas de uma só vez. O Tsuchigumo "
                "grita com um som humano e recua para as fendas do teto, pingando um lodo corrosivo. O caminho está livre."
            )
            yokai_derrotado = True
        else:
            layout.imprimir_lento(
                "FALHA! A carapaça do monstro é dura como ferro fundido. A Kagekiri resvala com faíscas. "
                "O impacto o desequilibra, e a fera avança furiosamente sobre você!"
            )
            resultado = iniciar_combate(jogador, "Tsuchigumo Colossal", hp_inimigo=30, min_dano=3, max_dano=6)
            if resultado == "vitoria": yokai_derrotado = True

    elif escolha == "2":
        layout.imprimir_lento("\nVocê embainha a espada parcialmente. O samurai verdadeiro sabe a hora de não derramar sangue inútil.")
        jogador["honra"] -= 1
        print("[Honra -1] Fugir de uma besta infernal o mantém vivo, mas mancha o orgulho.")

        if rolar_teste("destreza", jogador["destreza"], 20):
            layout.imprimir_lento(
                "SUCESSO! Você é uma sombra ágil. Quicando na parede úmida, você gira no ar, passando "
                "milímetros acima das presas envenenadas da criatura. Você aterrissa rolando do outro lado "
                "da teia impenetrável. A fera silva, frustrada por ter perdido a presa."
            )
        else:
            layout.imprimir_lento(
                "FALHA! O musgo na parede esfarela sob sua bota. Você perde o impulso e cai "
                "direto na borda da teia. Os fios cortam suas roupas como navalhas. O monstro te persegue!"
            )
            dano = random.randint(1, 3)
            jogador["vitalidade"] -= dano
            print(f"Você perdeu {dano} de Vitalidade na teia.")
            resultado = iniciar_combate(jogador, "Tsuchigumo Faminto", hp_inimigo=25, min_dano=2, max_dano=5)
            if resultado == "vitoria": yokai_derrotado = True

    elif escolha == "3":
        layout.imprimir_lento("\nVocê crava a espada na pedra, une os dedos polegar e indicador, e entoa o mantra de Kazunari.")
        if rolar_teste("conhecimento", jogador["conhecimento"], 19):
            layout.imprimir_lento(
                "SUCESSO! As palavras antigas ganham vida. Uma faísca azul salta de seus dedos e "
                "inflama o miasma da caverna. Uma luz cegante e purificadora explode. "
                "O Yokai, acostumado a décadas de escuridão, entra em pânico e foge se arrastando para as profundezas."
            )
            yokai_derrotado = True
        else:
            layout.imprimir_lento(
                "FALHA! Você troca uma única sílaba do mantra complexo. A magia implode em suas mãos "
                "com um estalo abafado, queimando seus dedos. O Yokai, enfurecido pelo barulho, investe."
            )
            dano = random.randint(1, 2)
            jogador["vitalidade"] -= dano
            print(f"Suas mãos queimam. Você perdeu {dano} de Vitalidade.")
            resultado = iniciar_combate(jogador, "Tsuchigumo Enfurecido", hp_inimigo=25, min_dano=3, max_dano=6)
            if resultado == "vitoria": yokai_derrotado = True

    else:
        layout.imprimir_lento("Opção inválida. A escuridão não espera indecisos. A besta salta sobre você.")
        jogador["vitalidade"] -= 2
        iniciar_combate(jogador, "Tsuchigumo", hp_inimigo=25, min_dano=2, max_dano=5)

    if jogador["vitalidade"] <= 0: return jogador

    # --- CONTINUAÇÃO DA TRAMA DA CAVERNA ---
    layout.divisoria()

    if yokai_derrotado:
        layout.imprimir_lento(
            "Com a passagem agora iluminada pela luz fraca que vem do fim do túnel, "
            "você nota algo preso em um antigo casulo espesso deixado pelo Tsuchigumo no chão.\n"
            "Você rasga a seda com a espada. Lá dentro estão os restos mortais de um monge guerreiro de Takenoko. "
            "Nas mãos ósseas dele, um pequeno amuleto de bronze em forma de corvo ainda brilha intensamente."
        )
        jogador.setdefault("inventario", []).append("Sino do Corvo de Bronze")
        print("[Item Adicionado: Sino do Corvo de Bronze (Emite um som que revela ilusões de nível baixo)]")

    layout.imprimir_lento(
        "Você avança em direção à luz. O ar frio atinge seu rosto, mas a visão do lado de fora o paralisa.\n"
        "A caverna não leva à Vila de Kiku. O atalho cuspiu você no alto de um desfiladeiro vertiginoso. "
        "Lá embaixo, estendendo-se até o horizonte, está a vasta e assustadora Floresta Murmurante.\n"
        "A neblina no nível do solo pulsa como um coração doente. A descida pelo paredão de pedra é íngreme e mortal. "
        "O vento corta o desfiladeiro, trazendo sussurros de espíritos perdidos na floresta abaixo."
    )

    print("\nComo você decide iniciar sua descida para a Floresta Murmurante?")
    print("1 - [Descanso Tático] Montar um acampamento rápido e oculto na boca da caverna para enfaixar ferimentos antes de descer.")
    print("2 - [Determinação Cega] A fúria não descansa. Descer as rochas imediatamente enquanto a adrenalina oculta a dor.")

    escolha_descida = input("\nEscolha (1 ou 2): ").strip()

    if escolha_descida == "1":
        layout.imprimir_lento(
            "Você junta fungos secos e cria uma fogueira minúscula, que não emite luz, apenas calor. "
            "Você medita, limpa a Kagekiri e aperta as ataduras. A memória do seu mestre conforta seu coração."
        )
        cura = random.randint(3, 6)
        max_vit = jogador.get("max_vitalidade", jogador.get("vitalidade", 15))
        jogador["vitalidade"] = min(max_vit, jogador.get("vitalidade", 10) + cura)
        print(f"[Descanso] Você recuperou Vitalidade. (HP Atual: {jogador['vitalidade']})")
        layout.imprimir_lento("Com o corpo preparado, você inicia a lenta e cuidadosa descida pelo paredão quando o sol encoberto nasce.")

    elif escolha_descida == "2":
        layout.imprimir_lento(
            "Kuroi Shin'en não dorme, e você também não. Você guarda a espada nas costas e agarra as pedras pontiagudas, "
            "iniciando uma descida arriscada. A pressa o faz ganhar terreno e tempo."
        )
        jogador["honra"] += 1
        print("[Honra +1] O espírito de um samurai é incansável.")
        layout.imprimir_lento(
            "Você chega à base da floresta muito antes do esperado, ganhando vantagem posicional e evitando as "
            "patrulhas diurnas que rondam a fronteira da mata."
        )
        jogador["vantagem_floresta"] = True

    else:
        layout.imprimir_lento("Hesitando no limite do abismo, uma rajada de vento gelado quase o joga para baixo, forçando-o a descer às pressas.")
        jogador["vitalidade"] -= 1

    return jogador

# ==========================================
# INÍCIO DO CAPÍTULO E ESCOLHA DE ROTA
# ==========================================
def jogar(jogador):
    layout.cabecalho("CAPÍTULO 1: A QUEDA DO MUNDO")

    layout.imprimir_lento(
        "A descida da montanha é árdua. A temperatura aumenta, mas a sensação de morte no ar "
        "torna o clima sufocante. Na base do cume principal, a trilha se divide em duas."
    )

    print("\nOpções de Caminho:")
    print("1 - A Estrada Imperial (Caminho aberto, probabilidade de encontrar humanos e patrulhas).")
    print("2 - As Cavernas da Mandíbula (Atalho imerso em escuridão, covil de feras).")

    escolha_caminho = input("\nPor onde você seguirá? (1 ou 2): ").strip()

    layout.divisoria()

    if escolha_caminho == "1":
        jogador["rota_cap1"] = "estrada"
        jogador = cena_estrada(jogador)
    elif escolha_caminho == "2":
        jogador["rota_cap1"] = "caverna"
        jogador = cena_caverna(jogador)
    else:
        print("Sem saber para onde ir, você vagueia e perde o equilíbrio nas pedras.")
        jogador["vitalidade"] -= 1
        return jogar(jogador)

    return jogador