


#TODO still has local storage. gotta be cleared through indexeddb js interface ugh


function element_of() {
    name=$1[@]
    array=("${!name}")
    word=$2
    for ((i = 0; i < ${#array[@]}; i++)); do
        [[ "${array[$i]}" == "$word" ]] && return 0
    done
    return 1
}


cache_path=$HOME/.local/share/qutebrowser


keep_main=( webengine adblock-cache.dat blocked-hosts cleaning state clean-cookies.sh )
for x in $cache_path/*; do
    u="$(basename "$x")"
    if element_of keep_main "$u"; then
        continue
    fi
    echo $x
    rm -rf "$x"
done


keep_webengine=( IndexedDB "Local Storage" "Local Storage-state" Cookies )
for x in $cache_path/webengine/*; do
    u="$(basename "$x")"
    if element_of keep_webengine "$u"; then
        continue
    fi
    echo "$x"
    rm -rf "$x"
done


keep_indexeddb=( https_web.whatsapp.com_0.indexeddb.leveldb )
for x in $cache_path/webengine/IndexedDB/*; do
    u="$(basename $x)"
    if element_of keep_indexeddb "$u"; then
        continue
    fi
    echo "$x"
    rm -rf "$x"
done


cookies_file=$cache_path/webengine/Cookies

gmail_cookies="'account.google.com', '.google.com', 'mail.google.com'"
whatsapp_cookies="'web.whatsapp.com'"
outlook_cookies="'login.microsoftonline.com', '.microsoft.com', 'outlook.office.com'"

sqlite3 $cookies_file "DELETE FROM cookies WHERE host_key NOT IN ($gmail_cookies, $whatsapp_cookies, $outlook_cookies)"

rm -rf $HOME/.cache/qutebrowser/*
