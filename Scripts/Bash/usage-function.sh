#!/bin/bash

display_usage() {
  cat << EOF
  usage: ./usage.sh name
  
  This script will check whether the named account exists.
  It will also check whether a home folder exists for the account.
EOF
}

if [[ $# != 1 ]]
then
  display_usage
else
  grep -q $1 /etc/passwd && echo "$1 found in /etc/passwd" 
  if [ -d "/home/$1" ]
  then 
    echo "The folder /home/$1 exists"
  fi
fi
