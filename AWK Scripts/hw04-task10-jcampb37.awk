#!/usr/bin/awk

BEGIN{
FS=","
}
NR != 1{
sum += $3
}
END{
print "AVG: " sum/(NR-1)
}
