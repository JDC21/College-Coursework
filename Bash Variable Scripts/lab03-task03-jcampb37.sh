#!/bin/bash

echo "Please select one of the following: add sub mul div exp mod"

echo "Enter operator:"
     read op_var

echo "Enter first number:"
     read num1

echo "Enter second number:"
     read num2

#I decided to use functions to simplify the code, hopefully it isnt too much
fun_add() {
     echo $(( $num1+$num2 ))
}
fun_sub() {
     echo $(( $num1-$num2 ))
}
fun_mul() {
     echo $(( $num1*$num2 ))
}
fun_div() {
     echo $(( $num1/$num2 ))
}
fun_exp() {
     echo $(( $num1**$num2 ))
}
fun_mod() {
     echo $(( $num1%$num2 ))
}

#Each if statement is supposed to match the first input and perform the corresponding function
     if [ $op_var == "add" ]
     then
          echo -n "The sum of $num1 and $num2 is " && fun_add
     elif [ $op_var == "sub" ]
     then
          echo -n "The difference of $num1 and $num2 is " && fun_sub
     elif [ $op_var == "mul" ]
     then
          echo -n "The product of $num1 and $num2 is " && fun_mul
     elif [ $op_var == "div" ]
     then
          echo -n "The quotient of $num1 and $num2 is " && fun_div
     elif [ $op_var == "exp" ]
     then
          echo -n "The exponent of $num1 and $num2 is " && fun_exp
     elif [ $op_var == "mod" ]
     then
          echo -n "The mod of $num1 and $num2 is " && fun_mod
#I needed to include a mis-typing condition
     else
          echo "Bad input"
fi
