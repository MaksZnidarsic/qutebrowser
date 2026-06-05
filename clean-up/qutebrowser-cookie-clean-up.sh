#!/bin/bash



cache=$HOME/.local/share/qutebrowser/cleaning


function date_time() {
    echo $(date +"%Y-%m-%d %T")
}


script_name=$(basename -- "$0")
if pidof -x "$script_name" -o $$ >/dev/null; then
    exit
fi

echo "$(date_time) started qutebrowser" >> $cache
echo run


while [ 1 ]; do
    if ! pidof -x "qutebrowser" >/dev/null; then
        break
    fi
    sleep 1
done

$HOME/.config/qutebrowser/clean-up/clean-cookies.sh
echo "[$(date_time)] cleaned" >> $cache
