#!/bin/bash

echo "Enter the first number:"
read num1

echo "Enter the second number:"
read num2

#I used a function because it was similar to a task from the previous labs
fun() {
echo $(( num1+num2 ))
}

echo -n "The sum of $num1 and $num2 is " && fun
