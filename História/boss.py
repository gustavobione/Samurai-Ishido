# boss.py
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

def fase_1_ilusoes(jogador):
    layout.cabecalho("FASE 1: O FEITICEIRO DOS MIL ROSTOS")
    
    hp_kuroi = 60
    
    while hp_kuroi > 0 and jogador["vitalidade"] > 0:
        layout.divisoria()
        print(f"♥ Seu HP: {jogador['vitalidade']}  |  💀 HP Kuroi: {hp_kuroi}")
        
        layout.imprimir_lento(
            "O corpo de Kuroi se desfaz em fumaça negra. De repente, o salão se enche com DEZ cópias "
            "perfeitas do feiticeiro. Todas começam a conjurar esferas de fogo arcano que flutuam "
            "ao redor de você, prontas para incinerar sua carne."
        )
        
        print("\nComo você encontra e ataca o verdadeiro Kuroi?")
        print("1 - [Conhecimento] Fechar os olhos, ignorar a visão e rastrear a perturbação original no Disco do Abismo.")
        print("2 - [Destreza] Mover-se na velocidade do som, cortando todas as dez cópias antes que a magia dispare.")
        
        acao = input("\nEscolha (1 ou 2): ").strip()
        
        if acao == "1":
            if rolar_teste("conhecimento", jogador["conhecimento"], 24):
                layout.imprimir_lento(
                    "SUCESSO! Nove assinaturas arcanas são ocas. Uma pulsa com batimentos cardíacos. "
                    "Você avança de olhos fechados e perfura o ar. O Sol Negro rasga o manto de Kuroi, "
                    "dissipando os clones!"
                )
                dano = random.randint(10, 20) + (jogador["kenjutsu"] // 2)
                hp_kuroi -= dano
                layout.imprimir_lento(f"> Kuroi grita e cospe sangue! (-{dano} HP)")
            else:
                layout.imprimir_lento("FALHA! A magia o engana. Você atinge um fantasma que explode em chamas infernais no seu rosto!")
                jogador["vitalidade"] -= random.randint(8, 15)
        
        elif acao == "2":
            if rolar_teste("destreza", jogador["destreza"], 25):
                layout.imprimir_lento(
                    "SUCESSO! O Nitoryu se torna um redemoinho inrastreável. Você cruza o salão decepando "
                    "cada ilusão até que o aço verdadeiro encontre carne e osso. O feiticeiro tomba para trás!"
                )
                dano = random.randint(10, 20) + (jogador["kenjutsu"] // 2)
                hp_kuroi -= dano
                layout.imprimir_lento(f"> A Kagekiri queima as costelas do mago! (-{dano} HP)")
            else:
                layout.imprimir_lento("FALHA! Você é rápido, mas a feitiçaria é instantânea. Oito esferas de fogo o atingem simultaneamente!")
                jogador["vitalidade"] -= random.randint(10, 18)
        else:
            layout.imprimir_lento("A hesitação é letal. Os clones bombardeiam você.")
            jogador["vitalidade"] -= 12

    return jogador

def fase_2_escudo(jogador):
    if jogador["vitalidade"] <= 0: return jogador
    
    layout.cabecalho("FASE 2: A REJEIÇÃO DA LINHAGEM")
    
    layout.imprimir_lento(
        "Kuroi Shin'en rasteja para trás, o sangue negro manchando o mármore. "
        "'O MUNDO SUPERA O SANGUE!', ele berra, erguendo as duas mãos em direção ao Disco do Abismo.\n"
        "As dez partes do meteorito giram violentamente. Uma cúpula de energia cósmica negra e "
        "impenetrável se forma ao redor do feiticeiro.\n"
        "'Este é o poder do seu pai! E ele me obedece agora!', zomba Kuroi, protegido pela barreira divina."
    )
    
    quebrou_escudo = False
    
    while not quebrou_escudo and jogador["vitalidade"] > 0:
        layout.divisoria()
        print(f"♥ Seu HP: {jogador['vitalidade']}  |  🛡️ Barreira: IMPENETRÁVEL")
        
        print("\nComo destruir o poder de um deus corrompido?")
        print("1 - [Honra] Apelar para a linhagem sagrada. Exigir que o Disco reconheça o herdeiro legítimo.")
        print("2 - [Kenjutsu] O aço do Sol Negro e da Lua Prateada também é feito de meteorito. Usar força bruta máxima!")
        
        acao = input("\nEscolha (1 ou 2): ").strip()
        
        if acao == "1":
            if jogador.get("honra", 10) >= 20:
                layout.imprimir_lento(
                    "Você embainha as duas espadas. Caminha desarmado em direção ao escudo mortal. "
                    "A cada passo, uma memória dos sacrifícios do seu clã ressoa em sua alma. "
                    "'Eu sou Ishido. E a sombra não governa a luz!'\n"
                    "Você encosta a mão nua na barreira. A Honra pura do Xogum reage com o artefato. "
                    "O Disco do Abismo pulsa em azul e... desliga a barreira de Kuroi! O mago entra em choque."
                )
                quebrou_escudo = True
            else:
                layout.imprimir_lento(
                    "O Disco pulsa, mas não o reconhece. Suas mãos estão manchadas demais com atalhos "
                    "desonrosos. A barreira te repele com uma força esmagadora!"
                )
                jogador["vitalidade"] -= 15
        
        elif acao == "2":
            if rolar_teste("kenjutsu", jogador["kenjutsu"], 26):
                layout.imprimir_lento(
                    "SUCESSO ABSOLUTO! Você canaliza toda a energia vital do seu corpo nas lâminas gêmeas. "
                    "O choque do meteorito terrestre contra a cúpula cósmica cria uma explosão ensurdecedora. "
                    "A barreira racha como vidro e estilhaça, arremessando Kuroi contra a parede!"
                )
                quebrou_escudo = True
            else:
                layout.imprimir_lento(
                    "FALHA! A barreira é infinitamente densa. Suas espadas ricocheteiam com uma força avassaladora, "
                    "deslocando seus ombros e lançando você aos ares."
                )
                jogador["vitalidade"] -= 15
        else:
            layout.imprimir_lento("A feitiçaria absorve o oxigênio do salão, asfixiando você.")
            jogador["vitalidade"] -= 10
            
    return jogador

def fase_3_avatar(jogador):
    if jogador["vitalidade"] <= 0: return jogador
    
    layout.cabecalho("FASE FINAL: O AVATAR DO CAOS")
    
    layout.imprimir_lento(
        "Sem escudo e ferido mortalmente, Kuroi Shin'en começa a rir. Uma risada que não soa humana, "
        "mas como montanhas se partindo.\n"
        "'Se eu não posso governar este mundo... ELE NÃO EXISTIRÁ!'\n"
        "O mago estica a mão, e o Disco do Abismo mergulha diretamente no peito dele. A carne de Kuroi "
        "derrete, substituída por pura matéria cósmica. Ele cresce. Sete, dez, quinze metros de altura."
    )
    layout.imprimir_lento(
        "Ele não é mais um humano. É uma massa torcida de trevas, com tentáculos de chamas e dezenas de "
        "olhos vermelhos que choram sangue negro. O teto da torre é vaporizado, revelando o céu "
        "tempestuoso onde o Avatar do Caos o encara."
    )
    
    hp_avatar = 150
    mod_defesa = (jogador.get("destreza", 10) + jogador.get("kenjutsu", 10)) // 4
    defesa_jogador = 10 + mod_defesa + jogador.get("bonus_defesa", 0)
    bonus_ataque_avatar = 15 # Extremamente mortal
    
    while hp_avatar > 0 and jogador["vitalidade"] > 0:
        layout.divisoria()
        max_hp = jogador.get("max_vitalidade", jogador["vitalidade"])
        print(f"♥ Seu HP: {jogador['vitalidade']}/{max_hp}  |  🛡️ Sua Defesa: {defesa_jogador}  |  💀 HP do Avatar: {hp_avatar}")
        
        print("1 - [Arte Nitoryu: Eclipse] Descarregar fúria total e ativar o Roubo de Vida Lunar.")
        print("2 - [Esquiva Perfeita] Focar apenas em não morrer neste turno (Ignora o ataque do inimigo se o teste der certo).")
        
        acao = input("Ação (1 ou 2): ").strip()
        
        if acao == "1":
            bonus_arma = jogador.get("bonus_dano_arma", 6)
            dano_jogador = random.randint(10, 20) + (jogador.get("kenjutsu", 10) // 2) + bonus_arma
            
            layout.imprimir_lento(f"> Você salta nos tentáculos da fera! O Sol e a Lua rasgam a escuridão, causando {dano_jogador} de dano cósmico.")
            hp_avatar -= dano_jogador
            
            cura_lunar = dano_jogador // 2
            jogador["vitalidade"] = min(max_hp, jogador["vitalidade"] + cura_lunar)
            layout.imprimir_lento(f"> A Lua Prateada devora a essência do caos, curando você (+{cura_lunar} HP).")
            
            if hp_avatar <= 0: break
            
        elif acao == "2":
            if rolar_teste("destreza", jogador["destreza"], 25):
                layout.imprimir_lento("> O Avatar atinge o solo onde você estava. A Torre treme, mas você escapa sem um arranhão neste turno!")
                continue # Pula o turno de ataque do boss!
            else:
                layout.imprimir_lento("> Você tenta esquivar, mas a magnitude do golpe o alcança pela onda de choque!")
        else:
            layout.imprimir_lento("> Você trava diante do horror!")
            
        # Turno do Monstro
        layout.imprimir_lento("\n[Turno do Inimigo: O AVATAR ATACA]")
        dado_ataque = random.randint(1, 20)
        total_ataque = dado_ataque + bonus_ataque_avatar
        time.sleep(0.5)
        print(f" 🎲 (Rolou {dado_ataque} + Bônus {bonus_ataque_avatar} = {total_ataque}) vs Sua Defesa ({defesa_jogador})")
        time.sleep(0.5)
        
        if total_ataque >= defesa_jogador:
            dano_sofrido = random.randint(15, 25)
            layout.imprimir_lento(f"> 💥 UM GOLPE DEVASTADOR! A gravidade o esmaga. Você perde {dano_sofrido} de HP.")
            jogador["vitalidade"] -= dano_sofrido
        else:
            layout.imprimir_lento("> ⚔️ Com pura maestria e intuição samurai, você deflete uma montanha de trevas com as suas espadas gêmeas!")

    return jogador

def epilogo(jogador):
    layout.cabecalho("O EPÍLOGO: O PESO DE UMA ERA")
    
    layout.imprimir_lento(
        "A deidade de sombras solta um uivo que rasga as nuvens de Takenoko, dissolvendo-se "
        "em cinzas que caem como neve negra sobre a Capital. Kuroi Shin'en está morto."
    )
    layout.imprimir_lento(
        "O salão desaba silenciosamente. No centro da poeira, flutuando a meio metro do chão e "
        "pulsando com uma energia infinita e corrompida, está o Disco do Abismo. O artefato que "
        "enlouqueceu seu pai e iniciou vinte anos de tormento."
    )
    layout.imprimir_lento(
        "Você embainha a Lua Prateada, mas mantém o Sol Negro (Kagekiri) firme na sua mão. "
        "Você olha para o Disco. Ele sussurra promessas para você. Com esse poder absoluto, "
        "você poderia reconstruir tudo. Ninguém jamais ousaria desafiar o novo Xogum de Takenoko. "
        "Você seria um deus."
    )
    layout.imprimir_lento("Mas você também lembra das cinzas, dos escravos, e do túmulo congelado de Kazunari.")
    
    print("\nO destino do mundo repousa nas suas espadas. Qual é a sua escolha final?")
    print("1 - [A Purificação] A magia é a fonte de toda a ruína. Desferir um golpe fatal e destruir o Disco do Abismo para sempre.")
    print("2 - [O Novo Ciclo] O poder não é bom nem mau, é apenas uma ferramenta. Reivindicar o Disco e assumir o Trono de Obsidiana.")
    
    escolha_final = input("\nA sua decisão ecoará pela eternidade (1 ou 2): ").strip()
    
    layout.divisoria()
    
    if escolha_final == "1":
        layout.imprimir_lento(
            "Você ergue a Kagekiri acima da cabeça. O meteorito ressoa com um brilho ofuscante, "
            "purificado pelo sacrifício de toda a sua jornada. Você desce a lâmina com um grito "
            "que corta a própria essência do tempo.\n"
            "O aço colide com o Disco. O mundo inteiro fica em silêncio.\n"
            "Uma onda de choque branca explode pela torre, varrendo toda a Província Central. "
            "A energia destrói a feitiçaria, derrete os monstros remanescentes e purifica os pântanos.\n"
            "A Torre desmorona ao seu redor, mas você salta para a luz. O céu, pela primeira vez "
            "em vinte anos, é banhado pelo sol natural. Takenoko está livre. A Era da Magia acabou.\n"
            "Anos mais tarde, lendas falarão do samurai descalço de duas espadas que vagava "
            "como um curandeiro pelos arrozais, um homem sem senhores, mas com a alma de um império."
        )
    else:
        layout.imprimir_lento(
            "Você abaixa a lâmina. O Disco sente a sua ambição e gira mais rápido. "
            "Você estende a mão e toca o artefato antigo.\n"
            "Imediatamente, as veias dos seus braços ficam negras. Uma coroa de chamas gélidas "
            "se forma acima da sua cabeça. O poder é inimaginável. As vozes de bilhões de mortos "
            "ecoam em sua mente, subjugando-se à sua vontade imortal.\n"
            "Você caminha lentamente e se senta no Trono de Obsidiana. As portas da torre se "
            "escancaram. Os exércitos de Yokais, antes bestas selvagens, ajoelham-se em uníssono "
            "nos pátios inferiores. O mundo encontrou ordem. Uma ordem de punho de ferro e escuridão.\n"
            f"O Imperador Nobutatsu enlouqueceu. O Mago Kuroi fracassou. Mas o Lorde Demônio {jogador['nome']}, "
            "o Xogum do Abismo, reinará para sempre."
        )

    layout.cabecalho("FIM DE JOGO")
    print(f"Muito obrigado por jogar Samurai Ishido. Status Final de Honra: {jogador['honra']}")
    time.sleep(3)


def jogar(jogador):
    layout.cabecalho("O CLÍMAX: O TRONO DO ABISMO")
    
    layout.imprimir_lento(
        "Você cruza os gigantescos portões de Ouro Negro. A câmara do trono é uma abóbada que desafia "
        "a sanidade, construída inteiramente de antigas armaduras derretidas."
    )
    layout.imprimir_lento(
        "No centro, pairando sobre o piso, está o Mago Kuroi Shin'en. Apesar das décadas, ele aparenta "
        "uma juventude profana, sustentada pelas dez partes giratórias do Disco do Abismo flutuando acima dele."
    )
    layout.imprimir_lento(
        "Ele sorri. 'A ovelha desgarrada do clã Shiro. Pensei que você teria morrido congelado "
        "junto daquele velho aleijado na montanha.'"
    )
    
    jogador = fase_1_ilusoes(jogador)
    if jogador["vitalidade"] <= 0: return layout.imprimir_lento("Sua alma foi devorada pelas ilusões de Kuroi.")
    
    jogador = fase_2_escudo(jogador)
    if jogador["vitalidade"] <= 0: return layout.imprimir_lento("A linhagem do seu pai o rejeitou na morte.")
    
    jogador = fase_3_avatar(jogador)
    if jogador["vitalidade"] <= 0: return layout.imprimir_lento("O Caos consumiu o último resquício de luz do Japão.")
    
    epilogo(jogador)