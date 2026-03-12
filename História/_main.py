# main.py
import time
import layout  # Importamos nosso novo motor de interface!
import capitulo_0 as prologo
import capitulo_1
import capitulo_2
import capitulo_3
import capitulo_4
import capitulo_5
import boss
import sistemas


def checar_morte(jogador):
    """Verifica se o jogo deve acabar por falta de vitalidade ou perda total de honra."""
    if jogador["vitalidade"] <= 0:
        layout.cabecalho("FIM DE JOGO")
        layout.imprimir_lento(
            "Sua visão escurece. O aço cai de suas mãos. "
            "O império de Kuroi Shin'en reinará nas sombras pela eternidade."
        )
        return True
    if jogador["honra"] <= 0:
        layout.cabecalho("FIM DE JOGO")
        layout.imprimir_lento(
            "O peso das suas ações cruéis destruiu o código do samurai. "
            "A vergonha consome sua alma. Em silêncio, você comete Seppuku."
        )
        return True
    return False


def iniciar_jogo():
    # O estado inicial do jogador
    jogador = {
        "nome": "",
        "vitalidade": 0,
        "kenjutsu": 0,
        "destreza": 0,
        "conhecimento": 0,
        "honra": 0,
        "inventario": [],
        "bonus_defesa": 0,
        "bonus_dano_arma": 0,
    }

    # ================= PROLÓGO =================
    jogador = prologo.jogar(jogador)
    if checar_morte(jogador):
        return
    jogador["max_vitalidade"] = jogador["vitalidade"]
    layout.painel_status(jogador)

    # ================= CAPÍTULO 1 =================
    jogador = capitulo_1.jogar(jogador)
    if checar_morte(jogador):
        return
    jogador = sistemas.evoluir_capitulo_1(jogador)
    layout.painel_status(jogador)

    # ================= CAPÍTULO 2 =================
    jogador = capitulo_2.jogar(jogador)
    if checar_morte(jogador):
        return
    jogador = sistemas.evoluir_capitulo_2(jogador)
    layout.painel_status(jogador)

    # ================= CAPÍTULO 3 =================
    jogador = capitulo_3.jogar(jogador)
    if checar_morte(jogador):
        return
    jogador = sistemas.evoluir_capitulo_3(jogador)
    layout.painel_status(jogador)

    # ================= CAPÍTULO 4 =================
    jogador = capitulo_4.jogar(jogador)
    if checar_morte(jogador):
        return
    jogador = sistemas.evoluir_capitulo_4(jogador)
    layout.painel_status(jogador)

    # ================= CAPÍTULO 5 =================
    jogador = capitulo_5.jogar(jogador)
    if checar_morte(jogador):
        return
    jogador = sistemas.evoluir_capitulo_5(jogador)
    layout.painel_status(jogador)

    # ================= BOSS FINAL =================
    boss.jogar(jogador)


if __name__ == "__main__":
    iniciar_jogo()
