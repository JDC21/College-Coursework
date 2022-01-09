#!/bin/bash

# I needed to set the operator variable first as it determines everything else
op_var="$1"
shift

set_var=1
total_var=$#

if [ $op_var = "add" ]
then
    sum=0
    while [ $op_var -le $total_var ]
    do
        sum=$(($sum + $1))
        set_var=$((set_var + 1))
        shift 1
    done
    echo "$sum"

elif [ $op_var = "sub" ]
then
# I needed to fiddle around alot to get the different operators to work, I'm not the best at math, but the changes between them should work
    dif=$1
    shift
    while [ $set_var -lt $total_var ]
    do
        dif=$(($dif - $1))
        set_var=$((set_var + 1))
        shift 1
    done
    echo `expr $dif`

elif [ $op_var = "mul" ]
then
    prod=1
    while [ $set_var -le $total_var ]
    do
        prod=$(($prod * $1))
        set_var=$((set_var + 1))
        shift 1
    done
    echo $prod

elif [ $op_var = "div" ]
then
    div=$1
    shift
    while [ $set_var -lt $total_var ]
    do
        div=$(($div / $1))
        set_var=$((set_var + 1))
        shift 1
    done
    echo `expr $div`

elif [ $op_var = "exp" ]
then
    base=$1
    shift
    prod=1
    while [ $set_var -lt $total_var ]
    do
        prod=$(($prod * $1))
        set_var=$((set_var + 1))
        shift 1
    done
    exp=$(($base ** $prod))
    echo $exp

elif [ $op_var = "mod" ]
then
    mod=$1;
    shift;
    while [ $set_var -lt $total_var ]
    do
        mod=$(($mod % $1))
        set_var=$((set_var + 1))
        shift 1
    done
    echo `expr $mod`
else
        echo "Bad input"
fi
