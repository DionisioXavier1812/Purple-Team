# Ataque 3 – Brute Force Simples

## Objetivo
Simular brute force básico no SSH.

## Passos
1. Tentativas repetidas de login
2. Uso de lista simples de senhas
3. Geração de ruído nos logs

## Comandos
hydra -l admin -P senhas.txt ssh://192.168.1.10

## IoCs
- Múltiplas falhas de login
- Padrão repetitivo de tentativas
