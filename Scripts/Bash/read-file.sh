#!/bin/bash
input="filepath.txt"
while IFS= read -r line
do
  echo "$line"
done < "$input"
