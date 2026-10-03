import time

print("Monitorando auth.log...")

try:
    with open("auth.log", "r") as log:
        linhas = log.readlines()
except FileNotFoundError:
    print("Arquivo auth.log não encontrado.")
    exit()

alerta = False

for linha in linhas:
    if "Failed password" in linha:
        alerta = True
        print("[ALERTA] Tentativa de login detectada:")
        print(linha.strip())

if not alerta:
    print("Nenhuma tentativa suspeita encontrada.")
