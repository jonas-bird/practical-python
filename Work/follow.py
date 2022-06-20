#!/usr/bin/env python3 
"""
Code from practical python  https://dabeaz-course.github.io/practical-python/Notes/06_Generators/02_Customizing_iteration.html
"""
import os
import time 

f = open('Data/stocklog.csv')
f.seek(0, os.SEEK_END)  # Move file pointer 0 bytes from end of file
while True:
	line = f.readline()
	if line == '':
		time.sleep(0.1)  # pause before retry
		continue
	fields = line.split(',')
	name = fields[0].strip('"')
	price = float(fields[1])
	change = float(fields[4])
	if change < 0:
		print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
