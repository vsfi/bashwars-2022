#!/bin/sh 
clear
cat /data/banner.txt; echo

su hunter - /data/duck.sh &
su hunter - /data/dog.sh
