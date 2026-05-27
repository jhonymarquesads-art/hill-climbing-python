import random

# =========================================================
# 1. Gerar array aleatório
# =========================================================

tamanho = random.randint(15, 30)

terreno = [random.randint(0, 100) for _ in range(tamanho)]

# =========================================================
# 2. Definir posição inicial aleatória
# =========================================================

posicao_atual = random.randint(0, tamanho - 1)

# =========================================================
# Exibir terreno inicial
# =========================================================

print("=" * 60)
print("TERRENO GERADO")
print(terreno)
print("=" * 60)

print(f"\nPosição inicial do agente: {posicao_atual}")
print(f"Valor inicial: {terreno[posicao_atual]}\n")

# =========================================================
# 3. Algoritmo Hill Climbing
# =========================================================

passo = 1

while True:

    valor_atual = terreno[posicao_atual]

    # Verificar vizinhos
    esquerda = posicao_atual - 1 if posicao_atual > 0 else None
    direita = posicao_atual + 1 if posicao_atual < tamanho - 1 else None

    valor_esquerda = terreno[esquerda] if esquerda is not None else -1
    valor_direita = terreno[direita] if direita is not None else -1

    # =====================================================
    # Mostrar estado atual
    # =====================================================

    print(f"PASSO {passo}")
    print(f"Posição atual: {posicao_atual}")
    print(f"Valor atual: {valor_atual}")

    if esquerda is not None:
        print(f"Vizinho esquerdo [{esquerda}] = {valor_esquerda}")

    if direita is not None:
        print(f"Vizinho direito [{direita}] = {valor_direita}")

    # =====================================================
    # Escolher melhor vizinho
    # =====================================================

    melhor_valor = valor_atual
    nova_posicao = posicao_atual
    movimento = "Parou (ótimo local encontrado)"

    # Verifica esquerda
    if valor_esquerda > melhor_valor:
        melhor_valor = valor_esquerda
        nova_posicao = esquerda
        movimento = "Subiu para a esquerda"

    # Verifica direita
    if valor_direita > melhor_valor:
        melhor_valor = valor_direita
        nova_posicao = direita
        movimento = "Subiu para a direita"

    print("Decisão:", movimento)
    print("-" * 60)

    # =====================================================
    # Se não encontrou vizinho melhor, encerra
    # =====================================================

    if nova_posicao == posicao_atual:
        break

    posicao_atual = nova_posicao
    passo += 1

# =========================================================
# 5. Comparar com ótimo global
# =========================================================

otimo_local = terreno[posicao_atual]
otimo_global = max(terreno)

print("\nRESULTADO FINAL")
print("=" * 60)
print(f"Ótimo local encontrado: {otimo_local}")
print(f"Ótimo global do array: {otimo_global}")

if otimo_local == otimo_global:
    print("O agente encontrou o ótimo global.")
else:
    print("O agente ficou preso em um ótimo local.")