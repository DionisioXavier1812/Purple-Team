#!/bin/bash
echo "Monitorando tentativas de login..."
grep "Failed password" /var/log/auth.log > /tmp/deteccao.txt

if [ -s /tmp/deteccao.txt ]; then
    echo "[ALERTA] Tentativas de login detectadas!"
fi
