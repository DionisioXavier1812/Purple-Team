# Ataque 2 – Execução de Comando Remoto

## Objetivo
Simular execução de comando após acesso indevido.

## Passos
1. Acesso via SSH
2. Execução de comando para listar usuários
3. Criação de arquivo malicioso

## Comandos
whoami
cat /etc/passwd
touch /tmp/malware.txt

## IoCs
- Criação de arquivo suspeito
- Execução de comandos administrativos
