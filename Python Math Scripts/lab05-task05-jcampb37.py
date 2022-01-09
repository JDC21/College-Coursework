#!/usr/nin/python3
import math

investment = int(input("Enter a starting value: "))

interest = {
"01 year":(round(investment*(1.01**1))),
"02 years":(round(investment*(1.01**2))),
"03 years":(round(investment*(1.01**3))),
"04 years":(round(investment*(1.01**4))),
"05 years":(round(investment*(1.01**5))),
"06 years":(round(investment*(1.01**6))),
"07 years":(round(investment*(1.01**7))),
"08 years":(round(investment*(1.01**8))),
"09 years":(round(investment*(1.01**9))),
"10 years":(round(investment*(1.01**10)))
}
print('{', end = '')
for key in sorted(interest):
	print(key,':',interest[key])
print('}')
