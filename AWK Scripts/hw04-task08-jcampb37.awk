#!/user/bin/awk

#No Begin or End blocks are necessary for this script
{
if($0 !~ /[0-9]/)
print $0
}
