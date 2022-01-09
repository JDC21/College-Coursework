#!/usr/bin/awk

BEGIN{
FS=","
}
{
#Using -le won't work here
if (NF <= 4)
print NR
}
