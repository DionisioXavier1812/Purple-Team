# Ataque 1 – Enumeração e Acesso Indevido

## Objetivo
Simular um ataque simples de enumeração e tentativa de acesso indevido.

## Passos
1. Scan de portas usando Nmap
2. Descoberta de porta 22 aberta
3. Tentativa de login SSH com credenciais fracas
4. Acesso bem-sucedido

## Comandos
nmap -sV 192.168.1.10
ssh admin@192.168.1.10

## IoCs
- IP atacante: 10.0.0.55
- Tentativas de login SSH
