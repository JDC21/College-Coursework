#!/usr/bin/awk

BEGIN{
FS=","
}
{
#This is just a very basic addition of rows
total=0
for(i=1;i<=NF;i++)
total += $i
print total
}
