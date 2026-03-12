# capitulo_2.py
import time
import random
import layout

def rolar_teste(atributo_nome, valor_atributo, dificuldade=25):
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
# ROTA 1: FLORESTA (CHÃO) - A LAMA E O SANGUE
# ==========================================
def cena_floresta_chao(jogador):
    layout.cabecalho("A FLORESTA MURMURANTE - OS CAMINHOS DE LAMA")

    layout.imprimir_lento(
        "Deixando a Vila de Kiku para trás, você pisa no solo lamacento da Floresta Murmurante. "
        "As árvores aqui são titânicas, com raízes grossas como muralhas que se contorcem sobre a terra úmida.\n"
        "A neblina no chão é densa. Kazunari costumava dizer que esta floresta era o pulmão de Takenoko, "
        "mas agora, cada farfalhar de folhas soa como um sussurro de agonia."
    )
    
    # ---------------- ENCONTRO 1: A PONTE DE OSSOS ----------------
    layout.imprimir_lento(
        "A névoa se dissipa o suficiente para revelar uma ponte pênsil feita de cordas podres e... ossos. "
        "Do outro lado, três Ronins montam guarda. Eles vestem armaduras enferrujadas e ostentam marcas "
        "de corrupção negra pulsando no pescoço. Venderam suas almas a Kuroi Shin'en."
    )

    print("\nComo você lida com os traidores do código Samurai?")
    print("1 - [Kenjutsu] Avançar pela ponte. Um verdadeiro samurai anuncia sua presença antes do massacre.")
    print("2 - [Destreza] Escalar as raízes gigantes acima da ponte e tentar uma emboscada aérea letal.")
    print("3 - [Honra/Conhecimento] Caminhar até a metade e exigir que cometam Seppuku por servirem a feiticeiros.")

    escolha = input("\nEscolha (1, 2 ou 3): ").strip()

    if escolha == "1":
        layout.imprimir_lento("\nVocê pisa firme na ponte de ossos. Os Ronins sacam suas lâminas com sorrisos macabros.")
        jogador["honra"] += 2
        print("[Honra +2] A coragem de um duelo aberto.")

        if rolar_teste("kenjutsu", jogador["kenjutsu"], 22):
            layout.imprimir_lento("SUCESSO! Você é uma força da natureza. Sua lâmina apara os golpes e decepa cabeças em um giro de pura arte marcial.")
        else:
            layout.imprimir_lento("FALHA! A ponte balança traiçoeiramente. Eles cercam você!")
            resultado = iniciar_combate(jogador, "Trio de Ronins", hp_inimigo=30, min_dano=2, max_dano=5)

    elif escolha == "2":
        layout.imprimir_lento("\nVocê embainha a espada e escala a madeira podre até o dossel escuro.")
        if rolar_teste("destreza", jogador["destreza"], 21):
            layout.imprimir_lento("SUCESSO! Como uma gota de chuva silenciosa, você cai cortando a garganta dos inimigos. Um assassinato sem alarde.")
        else:
            layout.imprimir_lento("FALHA! Um galho quebra. Você cai no meio do acampamento e eles avançam!")
            resultado = iniciar_combate(jogador, "Acampamento Ronin", hp_inimigo=35, min_dano=2, max_dano=4)

    elif escolha == "3":
        layout.imprimir_lento("\n'Vocês desonraram o aço de Takenoko. Limpem sua vergonha ou eu apagarei suas existências!'")
        if rolar_teste("conhecimento", jogador["conhecimento"] + (jogador["honra"]//2), 24):
            layout.imprimir_lento("SUCESSO! O peso da desonra esmaga a mente de dois deles, que cravam as espadas no ventre. O terceiro foge gritando.")
            jogador["honra"] += 3
            print("[Honra +3] A verdadeira força de um samurai está em seu espírito.")
        else:
            layout.imprimir_lento("FALHA! 'A honra morreu com o Xogum!', riem eles, sacando as espadas e avançando!")
            jogador["honra"] -= 1
            resultado = iniciar_combate(jogador, "Ronins Hereges", hp_inimigo=35, min_dano=3, max_dano=6)

    if jogador["vitalidade"] <= 0: return jogador

    # ---------------- ENCONTRO 2: O DILEMA DO PÂNTANO ----------------
    layout.divisoria()
    layout.imprimir_lento(
        "Com a ponte cruzada, a floresta se transforma em um pântano sufocante. "
        "O som de chicotes quebra o silêncio, acompanhado de gemidos humanos.\n"
        "Avançando furtivamente, você avista uma cena terrível: dezenas de camponeses esquálidos, submersos "
        "na água suja até a cintura, estão sendo forçados a extrair seiva negra das raízes das árvores.\n"
        "O feitor não é humano. É um Kawa-no-Oni, um Kappa colossal e corrompido, com o casco coberto de espetos. "
        "Sua tigela sagrada no topo da cabeça borbulha com uma água ácida e escura.\n"
        "Atacar a fera seria arriscado e chamaria a atenção de patrulhas, mas abandonar os escravos é trair "
        "tudo o que Kazunari lhe ensinou."
    )

    print("\nO que o seu coração de samurai decide?")
    print("1 - [Kenjutsu] O aço fala mais alto que o pragmatismo. Saltar no pântano e desafiar o monstro.")
    print("2 - [Destreza] Eles já estão mortos por dentro. Focar na missão, dar a volta e se infiltrar nas sombras.")
    print("3 - [Conhecimento] 'Um Kappa obedece à etiqueta'. Mostrar-se pacificamente e curvar-se, forçando-o a retribuir a reverência.")

    escolha_pantano = input("\nEscolha (1, 2 ou 3): ").strip()

    if escolha_pantano == "1":
        layout.imprimir_lento("\nO grito das vítimas ecoa na sua lâmina. Você salta no pântano, a água suja batendo nos joelhos.")
        jogador["honra"] += 3
        print("[Honra +3] Você é a lenda que o povo esperava.")
        if rolar_teste("kenjutsu", jogador["kenjutsu"], 22):
            layout.imprimir_lento("SUCESSO! O primeiro ataque divide o casco do monstro. Ele grita, a água mágica vaza de sua cabeça e ele tomba enfraquecido antes de morrer.")
        else:
            layout.imprimir_lento("FALHA! A lama restringe seus movimentos. O chicote do monstro o atinge e a batalha começa!")
            iniciar_combate(jogador, "Kappa Feitor", hp_inimigo=45, min_dano=4, max_dano=8)

    elif escolha_pantano == "2":
        layout.imprimir_lento("\nVocê fecha os olhos com força, afoga a empatia no fundo da alma e rasteja pelas margens distantes.")
        jogador["honra"] -= 4
        print("[Honra -4] Você poupou seu corpo, mas mutilou seu espírito.")
        if rolar_teste("destreza", jogador["destreza"], 20):
            layout.imprimir_lento("SUCESSO! Você passa despercebido, deixando os gritos agonizantes para trás.")
        else:
            layout.imprimir_lento("FALHA! A água pantanosa trai seus passos. O monstro fareja seu sangue e avança rugindo contra você nas sombras!")
            iniciar_combate(jogador, "Kappa Caçador", hp_inimigo=40, min_dano=3, max_dano=7)

    elif escolha_pantano == "3":
        layout.imprimir_lento("\nVocê sai das sombras embainhando a espada. O monstro ergue o chicote, mas você faz uma reverência samurai profunda.")
        if rolar_teste("conhecimento", jogador["conhecimento"], 21):
            layout.imprimir_lento(
                "SUCESSO! O instinto folclórico domina a feitiçaria. O Kappa, compelido pela magia milenar da etiqueta, "
                "curva-se de volta. A água negra de sua cabeça derrama no pântano. Ele perde toda a força e cai no chão, "
                "agonizando sem seu poder mágico. Os camponeses o espancam até a morte com as correntes."
            )
            jogador["honra"] += 1
            print("[Honra +1] O sábio vence a guerra sem desembainhar a espada.")
        else:
            layout.imprimir_lento(
                "FALHA! A corrupção em Kuroi destruiu o folclore. 'Etiqueta não salva carne macia!', ri o monstro, chicoteando seu rosto!"
            )
            iniciar_combate(jogador, "Kappa Insano", hp_inimigo=45, min_dano=4, max_dano=8)

    return jogador

# ==========================================
# ROTA 2: FLORESTA (COPAS) - AS ILUSÕES E O VOO
# ==========================================
def cena_floresta_copas(jogador):
    layout.cabecalho("A FLORESTA MURMURANTE - O DOSSEL DAS ILUSÕES")

    layout.imprimir_lento(
        "Vindo das Cavernas, você começa sua travessia saltando entre os galhos colossais do topo "
        "da Floresta Murmurante. Lá embaixo, o chão está invisível sob um mar de névoa cinza."
    )
    
    # ---------------- ENCONTRO 1: A ILUSÃO DO MESTRE ----------------
    layout.imprimir_lento(
        "De repente, a neblina sobe. O ar congela. A figura do seu velho mestre Kazunari, com os dois "
        "braços intactos, aparece flutuando sobre o abismo. 'Venha, Ishido. Pise aqui, é seguro.'"
    )
    
    bonus = 3 if jogador.get("vantagem_floresta") else 0
    if bonus > 0: print("\n[Vantagem Tática da Caverna Ativada!]")

    print("\nO que você faz diante do fantasma do seu mestre?")
    print("1 - [Conhecimento] Focar a mente para dissipar a ilusão Yokai.")
    print("2 - [Destreza] Ignorar a visão e saltar no escuro para buscar um galho real.")
    
    tem_sino = "Sino do Corvo de Bronze" in jogador.get("inventario", [])
    if tem_sino:
        print("3 - [Místico] Retirar o Sino do Corvo de Bronze do inventário e tocá-lo.")

    escolha = input("\nEscolha: ").strip()

    if escolha == "1":
        layout.imprimir_lento("\n'Meu mestre pagou o preço por mim com o braço!'")
        if rolar_teste("conhecimento", jogador["conhecimento"] + bonus, 21):
            layout.imprimir_lento("SUCESSO! Você quebra o feitiço. O falso Kazunari vira fumaça negra, revelando o abismo mortal. Você está a salvo.")
        else:
            layout.imprimir_lento("FALHA! Você avança na direção dele e cai! Você agarra um cipó no último segundo, caindo em um ninho escuro!")
            iniciar_combate(jogador, "Prole de Jorogumo (Aranha)", hp_inimigo=20, min_dano=2, max_dano=5)

    elif escolha == "2":
        layout.imprimir_lento("\nVocê fecha os olhos e salta guiado pelo som e pela intuição.")
        if rolar_teste("destreza", jogador["destreza"] + bonus, 20):
            layout.imprimir_lento("SUCESSO! Seu salto pousa em um tronco maciço. O fantasma grita e se dissolve.")
        else:
            layout.imprimir_lento("FALHA! Você calcula mal e bate violentamente no tronco, deslizando para uma fenda cheia de bestas do tronco!")
            iniciar_combate(jogador, "Gárgula de Madeira", hp_inimigo=25, min_dano=3, max_dano=6)

    elif escolha == "3" and tem_sino:
        layout.imprimir_lento(
            "\nVocê balança o sino de bronze. DING.\n"
            "A onda sonora mística despedaça a ilusão como vidro. O Yokai despenca do galho atordoado. Você passa ileso."
        )
        jogador["honra"] += 1
        print("[Honra +1] Sabedoria milenar purificou o caminho.")
    else:
        layout.imprimir_lento("Você hesita demais e a ilusão ataca sua mente!")
        jogador["vitalidade"] -= 5
        iniciar_combate(jogador, "Espectro da Saudade", hp_inimigo=25, min_dano=3, max_dano=6)

    if jogador["vitalidade"] <= 0: return jogador

    # ---------------- ENCONTRO 2: O DILEMA DO TENGU ----------------
    layout.divisoria()
    layout.imprimir_lento(
        "Avançando pelo dossel recém-limpo da ilusão, você chega a uma clareira suspensa colossal, "
        "feita de árvores entrelaçadas. Penas negras do tamanho de espadas pontilham o chão de madeira.\n"
        "No centro, meditando sobre um santuário de pássaros, está um Daitengu. Ele tem pele vermelha, "
        "um longo nariz demoníaco, e empunha uma Odachi (espada gigante). Pendurada acima do abismo, "
        "há uma gaiola de bambu com um mensageiro humano machucado.\n"
        "O Daitengu abre olhos cor de ouro e fala com uma voz que reverbera no seu peito:\n"
        "'O cheiro da linhagem Shiro. Eu não sirvo ao feiticeiro humano Kuroi, mas odeio sua raça indigna. "
        "Vá embora ou prove que o aço de Takenoko ainda não apodreceu.'"
    )

    print("\nO que você faz diante do mestre dos ares?")
    print("1 - [Kenjutsu] O aço decide a honra. Aceitar o duelo de espadas frontalmente.")
    print("2 - [Destreza] Asas são presunçosas. Tentar furtar a chave da gaiola enquanto ele monologa e soltar o refém.")
    print("3 - [Conhecimento] 'Guerreiros dos céus prezam pelo respeito'. Responder com um haiku milenar sobre os ventos.")

    escolha_tengu = input("\nEscolha (1, 2 ou 3): ").strip()

    if escolha_tengu == "1":
        layout.imprimir_lento("\nVocê saca a Kagekiri e entra em postura de combate. O Daitengu sorri e avança com um salto gigantesco.")
        jogador["honra"] += 3
        print("[Honra +3] Não há recuo para um samurai autêntico.")
        if rolar_teste("kenjutsu", jogador["kenjutsu"], 23):
            layout.imprimir_lento(
                "SUCESSO! Uma troca de golpes titânica! A sua velocidade de uma-mão sobrepuja a força brutal da Odachi. "
                "Com um corte relâmpago, você apara o ataque dele e corta sua asa esquerda. Ele ajoelha, rindo com aprovação."
            )
        else:
            layout.imprimir_lento("FALHA! O poder dele é avassalador. O choque das espadas entorpece seu braço e ele o lança longe!")
            resultado = iniciar_combate(jogador, "Daitengu Furioso", hp_inimigo=60, min_dano=5, max_dano=10)
            if resultado == "vitoria": layout.imprimir_lento("O Tengu cai banhado em sangue, reconhecendo seu valor no último suspiro.")

    elif escolha_tengu == "2":
        layout.imprimir_lento("\nVocê concorda verbalmente, mas usa o vento para mascarar seus passos, deslizando em direção à gaiola.")
        jogador["honra"] -= 2
        print("[Honra -2] Táticas desonestas enfurecem a criatura orgulhosa.")
        if rolar_teste("destreza", jogador["destreza"], 24):
            layout.imprimir_lento(
                "SUCESSO! Suas mãos são mais rápidas que a vista dele. Você corta a corda com a Kagekiri e empurra a gaiola "
                "para um galho seguro. O Daitengu bate as asas em frustração, mas recua, impressionado com seu estilo fantasmagórico."
            )
        else:
            layout.imprimir_lento("FALHA! O Tengu ouve o bambu estalar. 'Verme sem honra!', ele grita, lançando um furacão de vento e cortes contra você!")
            iniciar_combate(jogador, "Daitengu Ofendido", hp_inimigo=65, min_dano=6, max_dano=11)

    elif escolha_tengu == "3":
        layout.imprimir_lento("\nVocê embainha a espada e declama o Haiku Antigo: 'Vento que não corta / Pássaro que não pousa / Aço reconhece aço.'")
        if rolar_teste("conhecimento", jogador["conhecimento"], 22):
            layout.imprimir_lento(
                "SUCESSO! O monstro arregala os olhos. Ele finca a espada no chão e se curva profundamente. "
                "'Há sabedoria na linhagem Shiro', ele murmura. Ele corta a corda da gaiola com uma lufada de vento e abre passagem para você."
            )
            jogador["honra"] += 2
            print("[Honra +2] Respeitar a cultura das criaturas antigas traz sabedoria e aliados.")
        else:
            layout.imprimir_lento("FALHA! Você engasga na última sílaba. O Daitengu suspira de decepção. 'Vocês são macacos tentando imitar a grandeza', diz ele, erguendo a lâmina.")
            iniciar_combate(jogador, "Daitengu Decepcionado", hp_inimigo=55, min_dano=4, max_dano=9)

    return jogador

# ==========================================
# GESTOR DO CAPÍTULO 2
# ==========================================
def jogar(jogador):
    # Puxa de onde o jogador veio no capítulo 1
    rota_anterior = jogador.get("rota_cap1", "estrada") 

    if rota_anterior == "estrada":
        jogador["rota_cap2"] = "chao"
        jogador = cena_floresta_chao(jogador)
    else:
        jogador["rota_cap2"] = "copas"
        jogador = cena_floresta_copas(jogador)
    
    if jogador["vitalidade"] <= 0: return jogador
    
    # --- TRANSIÇÃO PARA O CAPÍTULO 3 ---
    layout.divisoria()
    layout.imprimir_lento(
        "Com a poeira e o sangue para trás, a vegetação densa da Floresta Murmurante começa a morrer.\n"
        "Avançando mais alguns quilômetros, a terra macia dá lugar a pedras afiadas de basalto escuro. "
        "No horizonte, fumaça vulcânica tinge o céu de um vermelho doentio, e o som constante de "
        "marteladas em bigornas ecoa como o batimento cardíaco da terra.\n"
        "Você encontrou os Portões de Ferro Antigo. Esta é a fronteira com a Província de Tetsu, "
        "outrora o lar dos mestres ferreiros, agora as infames Forjas Escravocratas de Kuroi Shin'en.\n"
        "A jornada está prestes a ficar mais quente..."
    )
    
    return jogador