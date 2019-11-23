#!/usr/bin/env python3

infile = open('cities-us-by-state.txt', 'r')
#outfile =  open('cities-us-by-state.py', 'w')
'''
outfile.write("\n")
outfile.write("#  From the U.S. Census Bureau (1990 census)\n")
outfile.write("\n")
'''
#for line in infile:
#    parts = line.split(" ")
#    outfile.write()

l = infile.readline()
print(str(l))
parts = l.split(" ")
print(str(parts))

infile.close()
#outfile.close()
