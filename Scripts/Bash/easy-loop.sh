#!/bin/bash

#For loop example
for ip in $(seq 1 10); do echo 10.11.1.$ip; done
for ip in {1..10}; do echo 10.11.1.$ip;done


# while loop example

counter=1

while [ $counter -lt 10 ]
do
  echo "10.11.1.$counter"
  ((counter++))
done

