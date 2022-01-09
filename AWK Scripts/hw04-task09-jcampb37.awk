#!/usr/bin/awk

BEGIN{
FS=","
}
{
sum += $3
}
END{
#I found the tail command useful for trimming down the output
tail -n 1
print "Sum: " sum
}
