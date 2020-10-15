# -*- coding: utf-8 -*-
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


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
