# main.py
import time
import capitulo_0 as prologo
import capitulo_1
import capitulo_2
import capitulo_3
import capitulo_4
import capitulo_5
import sistemas
# import boss  # Este arquivo criaremos na próxima etapa!

def checar_morte(jogador):
    """Verifica se o jogo deve acabar por falta de vitalidade ou perda total de honra."""
    if jogador["vitalidade"] <= 0:
        print("\n" + "="*60)
        print("Sua visão escurece. O aço cai de suas mãos.")
        print("Você pereceu. O império de Kuroi Shin'en reinará nas sombras pela eternidade.")
        print("="*60)
        return True
    if jogador["honra"] <= 0:
        print("\n" + "="*60)
        print("O peso das suas ações cruéis destruiu o último resquício do código do samurai.")
        print("A vergonha consome sua alma. Em silêncio, você se ajoelha e comete Seppuku.")
        print("FIM DE JOGO")
        print("="*60)
        return True
    return False

def mostrar_status(jogador):
    """Exibe o painel de status atualizado e completo do jogador."""
    print("\n" + "╔" + "═"*60 + "╗")
    print(f"║                   STATUS DE {jogador['nome'].upper():<21} ║")
    print("╠" + "═"*60 + "╣")
    
    # HP
    max_hp = jogador.get("max_vitalidade", jogador.get("vitalidade", 0))
    print(f"║  ♥ Vitalidade (HP): {jogador['vitalidade']}/{max_hp}")
    print(f"║  ⛩️ Honra: {jogador['honra']}")
    
    # Status Principais
    print(f"║  ⚔️ Atributos -> Kenjutsu: {jogador['kenjutsu']} | Destreza: {jogador['destreza']} | Conhecimento: {jogador['conhecimento']}")
    
    # Cálculo de Defesa Passiva
    bonus_defesa = jogador.get("bonus_defesa", 0)
    mod_defesa = (jogador.get("destreza", 10) + jogador.get("kenjutsu", 10)) // 4
    defesa_total = 10 + mod_defesa + bonus_defesa
    print(f"║  🛡️ Defesa Passiva (Esquiva/Bloqueio): {defesa_total}")
    
    # Controle da Arma Equipada
    if jogador.get("duas_espadas_longas"):
        arma = "Daisho Celestial (Sol Negro & Lua Prateada)"
    elif jogador.get("espada_quebrada"):
        arma = "Cabo Quebrado (Dano Crítico Nulo)"
    else:
        arma = "Katana Kagekiri"
    print(f"║  🗡️ Arma Equipada: {arma}")

    # Inventário
    inventario = jogador.get("inventario", [])
    if len(inventario) > 0:
        print(f"║  🎒 Inventário: {', '.join(inventario)}")
    else:
        print("║  🎒 Inventário: Vazio")
        
    print("╚" + "═"*60 + "╝\n")
    time.sleep(2)

def iniciar_jogo():
    # O estado inicial e imutável do jogador
    jogador = {
        "nome": "",
        "vitalidade": 0,
        "kenjutsu": 0,
        "destreza": 0,
        "conhecimento": 0,
        "honra": 0,
        "inventario": [],
        "bonus_defesa": 0,
        "bonus_dano_arma": 0
    }

    # ================= PROLÓGO =================
    jogador = prologo.jogar(jogador)
    if checar_morte(jogador): return
    # A primeira definição de Vida Máxima baseada na rolagem inicial do Prólogo
    jogador["max_vitalidade"] = jogador["vitalidade"] 
    mostrar_status(jogador)

    # ================= CAPÍTULO 1 =================
    jogador = capitulo_1.jogar(jogador)
    if checar_morte(jogador): return
    jogador = sistemas.evoluir_capitulo_1(jogador)
    mostrar_status(jogador)

    # ================= CAPÍTULO 2 =================
    jogador = capitulo_2.jogar(jogador)
    if checar_morte(jogador): return
    jogador = sistemas.evoluir_capitulo_2(jogador)
    mostrar_status(jogador)

    # ================= CAPÍTULO 3 =================
    jogador = capitulo_3.jogar(jogador)
    if checar_morte(jogador): return
    jogador = sistemas.evoluir_capitulo_3(jogador)
    mostrar_status(jogador)

    # ================= CAPÍTULO 4 =================
    jogador = capitulo_4.jogar(jogador)
    if checar_morte(jogador): return
    jogador = sistemas.evoluir_capitulo_4(jogador)
    mostrar_status(jogador)

    # ================= CAPÍTULO 5 =================
    jogador = capitulo_5.jogar(jogador)
    if checar_morte(jogador): return
    jogador = sistemas.evoluir_capitulo_5(jogador)
    mostrar_status(jogador)

    # ================= BOSS FINAL =================
    # print("\nIniciando o Confronto Final...")
    # boss.jogar(jogador)

if __name__ == "__main__":
    iniciar_jogo()