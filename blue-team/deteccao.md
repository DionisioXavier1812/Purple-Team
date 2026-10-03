# Detecção – Blue Team

## Eventos detectados
- Tentativas de login SSH
- Acesso indevido
- Execução de comandos administrativos
- Criação de arquivo suspeito

## Ferramentas usadas
- journalctl
- auth.log
- syslog
- kernel.log

## Logs relevantes
Oct 03 10:22:14 sshd: Failed password for admin from 10.0.0.55
Oct 03 10:22:18 sshd: Accepted password for admin
Oct 03 10:23:01 system: User admin executed 'cat /etc/passwd'
Oct 03 10:23:44 system: File created: /tmp/malware.txt
