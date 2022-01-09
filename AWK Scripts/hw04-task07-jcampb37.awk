#!/usr/bin/awk

BEGIN{
FS=","
#I didn't realize variables needed to be declared only within the BEGIN block
vote = 0
}
{
if ( $2 > vote )
#Without including the additional {} I was unable to get the script to work
{
vote = $2;
dog = $1
}
}
END{
print dog" has"vote" votes"
}
