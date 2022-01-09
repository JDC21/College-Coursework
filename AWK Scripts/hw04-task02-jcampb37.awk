#!/usr/bin/awk

BEGIN{
     FS=","
}
{
#I attempted regex through the command line, however this would not not work in the script, so this was my work around solution
if ($3 == "online")
print $1 " is an online student"
if ($3 == "onsite")
print $1 " is an onsite student"
}
