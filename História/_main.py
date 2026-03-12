# main.py
import capitulo_0 as prologo
import capitulo_1

def checar_morte(jogador):
    if jogador["vitalidade"] <= 0:
        print("\nSua visão escurece. Você caiu em batalha. Kuroi Shin'en reinará para sempre nas sombras.")
        return True
    if jogador["honra"] <= 0:
        print("\nO peso das suas ações destruiu o código do samurai. A vergonha consome sua alma.")
        print("Em silêncio, você se ajoelha, saca sua lâmina menor e comete Seppuku. Fim de jogo.")
        return True
    return False

def mostrar_status(jogador):
    """Exibe o painel de status atualizado do jogador."""
    print("\n" + "="*60)
    print(f"                   STATUS DE {jogador['nome'].upper()}")
    print("="*60)
    print(f" ♥ Vitalidade (HP): {jogador['vitalidade']}")
    print(f" ⛩️ Honra: {jogador['honra']}")
    print(f" ⚔️ Atributos -> Kenjutsu: {jogador['kenjutsu']} | Destreza: {jogador['destreza']} | Conhecimento: {jogador['conhecimento']}")
    
    inventario = jogador.get("inventario", [])
    if len(inventario) > 0:
        print(f" 🎒 Inventário: {', '.join(inventario)}")
    else:
        print(" 🎒 Inventário: Vazio")
    print("="*60 + "\n")

def iniciar_jogo():
    jogador = {
        "nome": "",
        "vitalidade": 0,
        "kenjutsu": 0,
        "destreza": 0,
        "conhecimento": 0,
        "honra": 0,
        "inventario": [] # Inicializado aqui para o jogo todo!
    }

    jogador = prologo.jogar(jogador)
    if checar_morte(jogador): return
    
    mostrar_status(jogador) # Mostra o status após rolar os dados no prólogo

    jogador = capitulo_1.jogar(jogador)
    if checar_morte(jogador): return
    
    mostrar_status(jogador) # Mostra como o jogador saiu do capítulo 1

if __name__ == "__main__":
    iniciar_jogo()