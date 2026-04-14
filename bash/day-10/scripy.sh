#! /bin/bash

CPU_LEVEL=$1
MEM_LEVEL=$2

if (( $# -ne 2 ));then
	printf 'Uzycie %s <cpu level> <mem level>' "$0"
	exit 1
fi

CPU=$(ps aux | awk -v lvl=$CPU_LEVEL 'NR>1 && $3>lvl {print $0}')
MEM=$(ps aux | awk -v lvl=$MEM_LEVEL 'NR>1 && $4>lvl {print $0}')
PIDS_CPU=$(ps aux | awk -v lvl=$CPU_LEVEL 'NR>1 && $3>lvl {print $2}')
PIDS_MEM=$(ps aux | awk -v lvl=$MEM_LEVEL 'NR>1 && $4>lvl {print $2}')

printf "CPU ktore przekracza $CPU_LEVEL:\n%s\n" "$CPU"
printf '####################\n'
printf "MEM ktore przekracza $MEM_LEVEL:\n%s\n" "$MEM"
printf '####################\n'

echo "=== Otwarte porty - wysokie CPU ==="
for pid in $PIDS_CPU; do
    result=$(ss -lp | grep "pid=$pid")
    if [ -n "$result" ]; then 
        echo "PID $pid: $result"
    fi
done

echo "=== Otwarte porty - wysoka RAM ==="
for mpid in $PIDS_MEM; do
    result=$(ss -lp | grep "pid=$mpid")
    if [ -n "$result" ]; then
        echo "PID $mpid: $result"
    fi
done
