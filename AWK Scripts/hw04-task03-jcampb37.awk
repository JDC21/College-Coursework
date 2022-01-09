#!/usr/bin/awk

BEGIN{
FS=","
}
{
#putting -lt down there does not work
if ($2 >= 75)
print $1
}
