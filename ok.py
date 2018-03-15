na = """
203 1
 419 10
  36 11
   6 12
  14 2
 236 24
 152 25
  45 26
  26 27
   2 29
49752 33
6117 34
7943 35
1119 36
 316 37
  86 38
  37 39
   7 40
   3 41
"""
for element in na.split('\n'):
	if element == '' : continue
	amount,row = element.split()
	print '%-5s\t%-2s' % (row,amount)