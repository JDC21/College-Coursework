#!/bin/bash

total_var=$#
set_var=1
sum=0

# I learned that you cannot use the == operator when comparing strings
while [ $set_var -le $total_var ] 
     do
          sum=$(($sum + $1))
          set_var=$((set_var + 1))
          shift 1
     done

echo "$sum"
