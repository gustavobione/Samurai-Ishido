# layout.py
import time
import sys
import textwrap

# Define a largura padrão da tela do terminal (80 colunas é o padrão clássico)
LARGURA_TELA = 80


def imprimir_lento(texto, atraso=0.03, largura=LARGURA_TELA):
    """
    Imprime o texto aos poucos, respeitando a largura da tela sem quebrar palavras ao meio.
    """
    # Separa o texto por quebras de linha manuais (\n) que já existam na história
    paragrafos = texto.split("\n")

    for p in paragrafos:
        # Se for uma linha vazia, apenas pula
        if p.strip() == "":
            print()
            continue

        # O textwrap.wrap corta a string em uma lista de linhas que cabem na 'largura'
        linhas = textwrap.wrap(p, width=largura)

        for linha in linhas:
            for char in linha:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(atraso)
            print()  # Pula para a próxima linha após terminar de escrever

    print()  # Dá um respiro extra ao final do bloco de texto


def cabecalho(titulo):
    """Cria um cabeçalho elegante e centralizado para capítulos e eventos."""
    print("\n" + "╔" + "═" * (LARGURA_TELA - 2) + "╗")

    # Centraliza o título no meio do espaço disponível
    titulo_centralizado = titulo.center(LARGURA_TELA - 2)
    print(f"║{titulo_centralizado}║")

    print("╚" + "═" * (LARGURA_TELA - 2) + "╝\n")


def divisoria():
    """Imprime uma linha divisória simples."""
    print("-" * LARGURA_TELA)


def painel_status(jogador):
    """Exibe o HUD do jogador de forma estruturada dentro de um painel."""
    max_hp = jogador.get("max_vitalidade", jogador.get("vitalidade", 0))

    # Cálculo de Defesa Passiva
    bonus_defesa = jogador.get("bonus_defesa", 0)
    mod_defesa = (jogador.get("destreza", 10) + jogador.get("kenjutsu", 10)) // 4
    defesa_total = 10 + mod_defesa + bonus_defesa

    # Controle da Arma Equipada
    if jogador.get("duas_espadas_longas"):
        arma = "Daisho Celestial (Sol Negro & Lua Prateada)"
    elif jogador.get("espada_quebrada"):
        arma = "Cabo Quebrado (Dano Mínimo)"
    else:
        arma = "Katana Kagekiri"

    inventario = jogador.get("inventario", [])
    str_inventario = ", ".join(inventario) if inventario else "Vazio"

    # Desenhando o painel com largura fixa
    cabecalho(f"STATUS DE {jogador['nome'].upper()}")

    print(
        f" ♥ Vitalidade: {jogador['vitalidade']}/{max_hp}".ljust(LARGURA_TELA // 2)
        + f" ⛩️ Honra: {jogador['honra']}"
    )

    print(f" 🛡️ Defesa: {defesa_total}".ljust(LARGURA_TELA // 2) + f" 🗡️ Arma: {arma}")

    print("\n ⚔️ Atributos:")
    print(
        f"    Kenjutsu: {jogador['kenjutsu']} | Destreza: {jogador['destreza']} | Conhecimento: {jogador['conhecimento']}"
    )

    print(f"\n 🎒 Inventário: {str_inventario}")
    print("═" * LARGURA_TELA + "\n")
    time.sleep(1.5)
