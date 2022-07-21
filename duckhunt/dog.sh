(sleep 12; if ps aux | grep -q '[d]uck'; then echo "The duck is still alive..."; else printf 'You made it!\nYour flag is: Duck_Hunter_10000\n'; fi; killall -9 sh 2>/dev/null) &
/bin/sh -i 