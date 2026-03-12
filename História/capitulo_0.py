# prologo.py
import time
import random
import layout

def rolar_atributos():
    """Rola 1d6 para os 4 atributos e soma com a base 10."""
    print("\nRolando seus atributos (Base 10 + 1d6)...")
    time.sleep(1)
    
    atributos = {
        "vitalidade": 10 + random.randint(1, 6),   # HP baseado na resiliência
        "kenjutsu": 10 + random.randint(1, 6),     # Força e proficiência com a katana
        "destreza": 10 + random.randint(1, 6),     # Agilidade, esquiva e acrobacia
        "conhecimento": 10 + random.randint(1, 6), # Sabedoria mística e fraqueza de Yokais
        "honra": 10                                # Honra estrita do Samurai
    }
    
    print(f"- Vitalidade (HP): {atributos['vitalidade']}")
    time.sleep(0.5)
    print(f"- Kenjutsu (Dano/Ataque): {atributos['kenjutsu']}")
    time.sleep(0.5)
    print(f"- Destreza (Esquiva/Iniciativa): {atributos['destreza']}")
    time.sleep(0.5)
    print(f"- Conhecimento Yokai (Sabedoria): {atributos['conhecimento']}")
    time.sleep(0.5)
    print(f"- Honra (Alma do Samurai): {atributos['honra']}")
    time.sleep(1)
    
    return atributos

def jogar(jogador):
    layout.cabecalho("O DISCO DO ABISMO")
    
    historia_parte_1 = (
        "Tudo o que você sabe sobre o mundo lá fora são as palavras gravadas na sua mente "
        "pela voz áspera do seu mestre, Kazunari. Ao redor da fogueira, cercados pela neve "
        "eterna da Colina Lótus, ele costumava fechar os olhos cansados e lembrar.\n"
        "'As terras de Takenoko respiravam paz', ele dizia, com um sorriso triste. "
        "'Os camponeses colhiam arroz dourado sob um sol limpo. Os cinco Lordes governavam com "
        "sabedoria sob a luz do seu pai, o Xogum Nobutatsu. Era um império de honra.'\n"
        "Mas o rosto do mestre sempre escurecia ao mencionar o conselheiro. "
        "'Eu nunca confiei em Kuroi Shin'en. Os olhos daquele sacerdote não refletiam a luz. "
        "Ele fedia a túmulos antigos e feitiçaria, mas seu pai... seu pai foi cegado pela paranoia.'\n"
        "Kazunari contava como Kuroi envenenou a mente do Xogum, sussurrando mentiras sobre uma "
        "falsa rebelião dos Lordes. Com medo de perder o trono, Nobutatsu exigiu que as sete partes "
        "do lendário Disco do Abismo fossem tomadas dos Lordes e trazidas para a capital, unindo-as "
        "às três que ele mesmo guardava."
    )
    layout.imprimir_lento(historia_parte_1)
    input("[Pressione Enter para continuar a ouvir a lembrança...]\n")

    historia_parte_2 = (
        "Foi a ruína de tudo. Ao juntar as dez partes do artefato, Kuroi revelou sua verdadeira face.\n"
        "'Eu estava no pátio quando o céu apodreceu', lembrava Kazunari, apertando o coto do "
        "próprio ombro esquerdo. 'As nuvens sangraram. Os portões do submundo foram arrancados de "
        "suas dobradiças. Yokais, os demônios que achávamos ser apenas lendas de ninar, rasgaram o véu "
        "e marcharam sobre nós. A capital foi engolida por trevas e fogo.'\n"
        "Kuroi assassinou o Xogum. Ele precisava do sangue da linhagem sagrada do clã Shiro para "
        "selar o poder do Disco para sempre. Mas Kazunari, banhado no sangue dos próprios irmãos de "
        "armas, invadiu os aposentos reais. Ele pegou você, o filho mais novo, um bebê em prantos.\n"
        "A fuga foi um pesadelo. Para cruzar os portões, Kazunari teve que enfrentar uma abominação "
        "feita de sombras e ossos, invocada pelo próprio Kuroi. 'A fera me cobrou um preço alto', "
        "ele suspirava, tocando o espaço vazio onde seu braço deveria estar. Mas com a outra mão, "
        "ele segurava você e a Kagekiri, a lâmina sagrada do palácio. O preço foi pago."
    )
    layout.imprimir_lento(historia_parte_2)
    input("[Pressione Enter para continuar...]\n")

    historia_parte_3 = (
        "Por 20 anos, vocês não desceram a montanha. Kazunari exigiu de você o impossível. "
        "Como ele lutava com apenas uma mão, ele lhe ensinou um Kenjutsu único, um estilo agressivo, "
        "focado em destreza, evasão e golpes fatais. Ele lhe ensinou sobre os pontos fracos das "
        "criaturas do folclore, preparando sua mente para a feitiçaria que dominava o mundo abaixo.\n"
        "Mas o tempo é uma lâmina que corta até os guerreiros mais fortes. "
        "Hoje, a tempestade de neve parou. O mestre Kazunari deu seu último suspiro.\n"
        "Antes de partir, ele depositou a Kagekiri ('Corta-Sombras') em suas mãos. A katana, "
        "forjada em aço de meteorito, brilhou com um leve tom azulado ao toque de um verdadeiro Shiro. "
        "É a única arma capaz de purificar o feitiço de Kuroi."
    )
    layout.imprimir_lento(historia_parte_3)

    layout.imprimir_lento(
        "Você termina de erguer o túmulo de pedras para Kazunari.\n"
        "O vento sopra da base da montanha, trazendo o cheiro de cinzas e desespero.\n"
        "Você não conhece aquele mundo. Mas aquele mundo está prestes a conhecer você."
    )
    
    nome_input = input("\nComo você se chama, último herdeiro do clã Shiro? (Aperte Enter para usar 'Ishido'): ").strip()
    if nome_input == "":
        jogador["nome"] = "Ishido"
    else:
        jogador["nome"] = nome_input

    layout.imprimir_lento(f"\nLevante-se, {jogador['nome']}.")
    
    # Atribuição dos dados rolados para o dicionário do jogador
    novos_atributos = rolar_atributos()
    jogador.update(novos_atributos)

    layout.imprimir_lento(f"\nCom a Kagekiri embainhada, {jogador['nome']} dá o primeiro passo rumo à descida da Colina Lótus.")
    layout.imprimir_lento("A caçada a Kuroi Shin'en começou.")
    
    return jogador