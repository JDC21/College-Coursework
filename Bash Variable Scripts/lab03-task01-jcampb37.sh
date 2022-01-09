#!/bin/bash

echo "Enter your name:"
read name_var

echo "Enter the date:"
read date_var

echo "Enter your city;"
read city_var

echo "Enter your current temperature:"
read temp_var

echo "Enter todays birthday:"
read bday_var

echo "Enter your payable bills"
read bill_var

# I decided to use echo -n  to allow my code to allow for multiple sets of  modifiers, as seen below
#The code within the parenthesis take the date in YYYY/MM/DD format and returns the corresponding month
echo -n "Good day, $name_var. Today is $(date +%B -d$date_var), "
#This code below separates the day of the month and the year, I couldn't figure out how to put it on the same line
echo -n $(echo "$date_var" | cut -d '/' -f2)
echo -n ", "
echo -n $(echo "$date_var" | cut -d "/" -f1)
#The code in parenthesis takes the input date and returns the day of the week
echo ", in the city of $city_var. It is a beautiful $(date +%A -d$date_var), the temperature is $temp_var degrees. Today is $bday_var's birthday. Insurance is payable, as are the water, gas, and light bills for a total of \$$bill_var"
