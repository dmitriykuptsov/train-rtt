cat working.log | grep -v GPRMC > 2.log
cat working.log | grep GPRMC > 1.log

echo "time,lat,lng,mean" > result.log

python3 combine.py >> result.log


python3 plot.py result.log 
