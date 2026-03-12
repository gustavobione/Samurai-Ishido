# main.py
import capitulo_0 as prologo
import capitulo_1


def checar_morte(jogador):
    """Verifica se o jogo deve acabar por falta de vitalidade ou perda total de honra."""
    if jogador["vitalidade"] <= 0:
        print(
            "\nSua visão escurece. Você caiu em batalha. Kuroi Shin'en reinará para sempre nas sombras."
        )
        return True
    if jogador["honra"] <= 0:  # Agora honra <= 0 engatilha o Seppuku
        print(
            "\nO peso das suas ações destruiu o código do samurai. A vergonha consome sua alma."
        )
        print(
            "Em silêncio, você se ajoelha, saca sua lâmina menor e comete Seppuku. Fim de jogo."
        )
        return True
    return False


def iniciar_jogo():
    # O estado inicial é vazio, pois o prólogo vai rolar os dados e popular tudo
    jogador = {
        "nome": "",
        "vitalidade": 0,
        "kenjutsu": 0,
        "destreza": 0,
        "conhecimento": 0,
        "honra": 0,
    }

    jogador = prologo.jogar(jogador)

    if checar_morte(jogador):
        return


def iniciar_jogo():
    jogador = {
        "nome": "",
        "vitalidade": 0,
        "kenjutsu": 0,
        "destreza": 0,
        "conhecimento": 0,
        "honra": 0,
    }

    jogador = prologo.jogar(jogador)
    if checar_morte(jogador):
        return

    # Chamada do Capítulo 1
    jogador = capitulo_1.jogar(jogador)
    if checar_morte(jogador):
        return


if __name__ == "__main__":
    iniciar_jogo()
