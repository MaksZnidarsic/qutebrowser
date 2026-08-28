#!/bin/bash



#
# NOT IN USE
# keeping for later if needed
#
# HOW TO: run simultaneously w/ qutebrowser to clean cache after closing, closes itself when qutebrowser does
#


function date_time() {
    echo $(date +"%Y-%m-%d %T")
}


script_name=$(basename -- "$0")
if pidof -x "$script_name" -o $$ >/dev/null; then
    exit
fi

while [ 1 ]; do
    if ! pidof -x "qutebrowser" >/dev/null; then
        break
    fi
    sleep 1
done


cache=$HOME/.local/share/qutebrowser/cleaning

$HOME/.config/qutebrowser/clean-up/clean-cookies.sh
echo "[$(date_time)] cleaned" >> $cache
