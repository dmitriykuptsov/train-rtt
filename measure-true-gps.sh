#!/bin/bash

while True;
do
   location=`corelocationcli`
   time=`date +%s`
   p=`ping strangebit.io -c 4 | grep round | awk -F "=" '{print $2}' | awk -F "\/" '{print $2}'`
   echo "$time $location $p" | tee -a m.log
   sleep 4
done
