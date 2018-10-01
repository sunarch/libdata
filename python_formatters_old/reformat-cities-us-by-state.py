#!/usr/bin/env python3

#
# < libdata > - < Library of data files and formatters >
#
# Written in 2017 by András Németh <sunarchx@gmail.com>
#
# To the extent possible under law, the author(s) have dedicated all copyright and related and neighboring rights to this software to the public domain worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along with this software. If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.
#

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
