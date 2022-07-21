/bin/sh -c 'sleep 1; for frame in `ls /data/frames/`; do clear; cat /data/frames/$frame; sleep 0.2; done;' & 
$(sleep 11; killall -9 sh 2>/dev/null) &
$(sleep 10000 > /dev/null) &
$(/bin/sh > /dev/null) &