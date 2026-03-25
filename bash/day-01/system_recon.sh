#! /bin/bash

##host info
HOST=$(hostname)
UPTIME=$(uptime)

## otwarte porty
PORTS=$(ss -tuln)

## procesy
PROCESSES=$(ps aux)

##interfejsy
INTERFACES=$(ip a)

cat <<EOF
Wykonanie skanu systemu:
[HOST]
$HOST 
[UPTIME]
$UPTIME 
[OTWARTE PORTY]
$PORTS 
[URUCHOMIONE PROCESY]
$PROCESSES 
[INTERFEJSY]
$INTERFACES 

EOF



