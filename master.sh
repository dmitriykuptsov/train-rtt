cat working.log | grep -v GPRMC > 2.log
cat working.log | grep GPRMC > 1.log

python3 parse-coords.py > 1_parsed.log
cat 2.log | awk -F" " '{print $1","$2}' > 2_parsed.log

echo "time,lat,lng,mean" > result.log


python3 combine.py >> result.log


python3 plot.py result.log 
