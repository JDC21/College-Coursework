#!/usr/bin/awk

BEGIN{
# Setting the field seperator to a comma will allow me to choose certain fields to print
     FS=","
}
{
print $1, $2
}
