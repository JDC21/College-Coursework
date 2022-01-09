#!/usr/bin/python3

bad = "The Fall,Humans,Demon Time,The Now Now,Face Value,Vinyl Beach"
bad = bad.split(',')
bad[0] = "Face Value"
bad[1] = "Demon Days"
bad[2] = "Plastic Beach"
bad[3] = "The Fall"
bad[4] = "Humanz"
bad[5] = "The Now Now"

# Face value, 13 February 1981. Demon Days, 11 May 2005. Plastic Beach, 3 March 2010. The Fall, 25 December 2010. Humanz, 27 April 2017. The Now Now, 29 June 2018
# Face value was not represented in the expected output, but I found the album and release date on the web

print(bad)
