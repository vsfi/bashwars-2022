IFS=$'\n'
mkdir -p /dev/devices/
zombies=22
for line in `cat answer.txt`; do
    spawn=$(shuf -i 0-$zombies -n 1)
    zombies=$((zombies-spawn))
    if [ zombies != 0 ]; then
        for i in $(seq 1 $spawn); do
            fifo=$RANDOM
            # mkfifo /dev/devices/$fifo
            /bin/sh -c "echo 'Hrrr..Braaaaaains...Brains...' | ./child &" >/dev/devices/$fifo;
        done;
    fi
    fifo=$RANDOM
    # mkfifo /dev/devices/$fifo
    /bin/sh -c "echo \"$line\" | ./child & " >/dev/devices/$fifo;
done
