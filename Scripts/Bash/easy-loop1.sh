#!/usr/bin/bash

ip1=$( echo $1| cut -d '.' -f1,2,3)
ip2=$( echo $1| cut -d '.' -f4)
#echo $ip1
#echo $ip2
if [ $ip2 -eq 0 ]
then
((ip2++))
fi

counter=0

sum=$(($counter+$ip2))
#echo $sum
while [ $counter -lt $2 ] && [ $sum -le 254 ]
do
  echo "$ip1.$sum"
  ((counter++))
  ((sum++))
done

