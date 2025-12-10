p=`ping strangebit.io -c 4 | grep round | awk -F "=" '{print $2}' | awk -F "\/" '{print $2}'`
echo $p
