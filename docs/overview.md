# Purple Team – Overview

## Objetivos
- Simular ataques básicos (Red Team)
- Detectar eventos e responder (Blue Team)
- Correlacionar informações e melhorar defesas (Purple Team)

## Arquitetura Simples
Atacante (Red Team)
    ?
Servidor alvo (SSH)
    ?
Logs do sistema (auth.log, syslog, kernel.log)
    ?
Análise Blue Team
    ?
Correlação Purple Team

## Fluxo do Ataque
1. Red Team faz scan de portas
2. Descobre SSH aberto
3. Tenta credenciais fracas
4. Acessa o sistema
5. Executa comandos suspeitos
6. Blue Team detecta via logs
7. Purple Team correlaciona e recomenda melhorias
