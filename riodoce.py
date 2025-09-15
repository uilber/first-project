# Rio Doce - Emissão de passagem (COMPLETO)
# Trecho: Além Paraíba (MG) -> Rio de Janeiro (RJ)
# Duração: 3h30 | Valor: R$ 75,00 | 1 passageiro

import random

print("=== COMPANHIA RIO DOCE ===")
print("Trecho: Além Paraíba (MG) -> Rio de Janeiro (RJ)")
print("Paradas: Sapucaia, Três Rios, Areal, Petrópolis\n")

# Hora de saída (hora cheia)
hora_saida = int(input("Informe a HORA de saída (ex: 7 para 07:00): "))
hora_chegada = (hora_saida + 3) % 24
minuto_chegada = 30

# Dados do passageiro
print("\nCadastro do passageiro")
nome = input("Nome: ").strip()
sexo = input("Sexo (M/F): ").strip().upper()
cpf  = input("CPF: ").strip()

# -------- Desafio 1: Layout visual --------
print("\n=== LAYOUT DO ÔNIBUS (40 lugares) ===")
todos = list(range(1, 41))
total_disponivel = random.randint(1, 25)
assentos_disponiveis = sorted(random.sample(todos, total_disponivel))
for fila in range(10):
    a = fila*4 + 1
    b = fila*4 + 2
    c = fila*4 + 3
    d = fila*4 + 4
    
    # marcar com * se disponível, x se indisponível
    def marcar(n):
        if n in assentos_disponiveis:
            return f"[{n:02d}]"
        else:
            return "[--]"
    
    print(f"{marcar(a)}{marcar(b)}   |   {marcar(c)}{marcar(d)}")

print("\nAssentos livres:", assentos_disponiveis)
# -------- Desafio 2: Somente 9 assentos aleatórios disponíveis --------
while True:
    assento = int(input("Escolha seu assento dentre os disponíveis: "))
    if assento in assentos_disponiveis:
        break
    print("❌ Assento indisponível, escolha outro dos listados.")

# -------- Desafio 3: Janela ou corredor --------
# Janela: posição 1 e 4 na fileira (mod 4 == 1 ou 0)
# Corredor: posição 2 e 3 na fileira (mod 4 == 2 ou 3)
if assento % 4 == 1 or assento % 4 == 0:
    posicao = "Janela"
else:
    posicao = "Corredor"

# -------- Desafio 4: Frente (1..20) ou Trás (21..40) --------
parte_onibus = "Assento na parte da frente" if assento <= 20 else "Assento na parte de trás"

# -------- Desafio 5: Viagem diurna/noturna --------
tipo_viagem = "Viagem noturna" if hora_saida >= 18 else "Viagem diurna"

# -------- Desafio 6: Saudação personalizada --------
if sexo == "F":
    saudacao = f"Boa viagem, senhora {nome}!"
elif sexo == "M":
    saudacao = f"Boa viagem, senhor {nome}!"
else:
    saudacao = f"Boa viagem, {nome}!"

# -------- Ticket completo --------
preco = 75
print("\n===============================================")
print("              COMPANHIA RIO DOCE")
print("===============================================")
print("Trecho: Além Paraíba (MG)  →  Rio de Janeiro (RJ)")
print(f"Passageiro: {nome}")
print(f"Sexo: {sexo}")
print(f"CPF: {cpf}")
print(f"Assento: {assento}  ({posicao})")
print(f"{parte_onibus}")
print("\nParadas programadas:")
print("- Sapucaia (RJ)")
print("- Três Rios (RJ)")
print("- Areal (RJ)")
print("- Petrópolis (RJ)")
print(f"\nSaída: {hora_saida:02d}:00")
print(f"Chegada prevista: {hora_chegada:02d}:{minuto_chegada:02d}")
print(f"{tipo_viagem}")
print(f"\nValor da passagem: R$ {preco:.2f}")
print(saudacao)
print("===============================================\n")
