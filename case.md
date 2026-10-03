# Case Study – Purple Team

## Resumo do Ataque
O Red Team realizou:
- Scan de portas
- Tentativas de login SSH
- Acesso indevido
- Execução de comandos administrativos
- Criação de arquivo suspeito

## Detecção (Blue Team)
O Blue Team identificou:
- Tentativas de login
- Login bem-sucedido
- Execução de comandos
- Criação de arquivo malicioso

## Resposta
- Bloqueio do IP atacante
- Reset de credenciais
- Remoção do arquivo
- Revisão de permissões

## Lições Aprendidas (Purple Team)
- Credenciais fracas são risco crítico
- SSH não deve ficar exposto
- Falta MFA
- Logs foram suficientes para detectar
- Melhorias simples aumentam segurança
