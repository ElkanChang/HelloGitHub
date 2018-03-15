#!/usr/bin/env python3

# real_tax_money = salary - insurance - 3500
# real_tax = real_tax_money * tax_rate - some_num

import sys

if len(sys.argv) != 2:
	print("Parameter Error")
	sys.exit()

salary = sys.argv[1]

try:
	salary = int(sys.argv[1])
except ValueError:
	print ("Parameter Error")
	sys.exit()

	
real_tax_money = salary - 3500

if real_tax_money <= 1500:
	tax_rate = 0.03
	some_num = 0
elif real_tax_money > 1500 and real_tax_money <= 4500:
	tax_rate = 0.1
	some_num = 105
elif real_tax_money > 4500 and real_tax_money <= 9000:
	tax_tate = 0.2
	some_num = 555
elif real_tax_money > 9000 and real_tax_money <= 35000:
	tax_rate = 0.25 
	some_num = 1005
elif real_tax_money > 35000 and real_tax_money <= 55000:
	tax_rate = 0.3
	some_num = 2755
elif real_tax_money > 55000 and real_tax_money <= 80000:
	tax_rate = 0.35
	some_num = 5505
elif real_tax_money > 80000:
	tax_rate = 0.45
	some_num = 13505
else:
	print("I don't know what you want to do")

real_tax = real_tax_money * tax_rate - some_num
# result = round(real_tax,2)
print('{:.2f}'.format(real_tax))
