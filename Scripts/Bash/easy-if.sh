#! /bin/bash
read -p 'Number: ' number

if [ $number -ge 8675 ] || [ $number != 1234 ]
then
	if [ $number -le 1337 ] && ! [ $number -eq 750 ]
	then
		echo "Bill"
	else
		echo "Hank"
	fi
else
	if [ $number -gt 900 ] && [ $number -ne 5000 ]
	then
		echo "Dale"
	else
		echo "Boomhauer"
	fi
fi
