#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2011 Evan Muller <evan@Tali>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#       

import random

from random import randint

dice = float(input('What dice do you want to roll?'))

# d6 protocol
if dice == 6:
	print "You chose d6"
	print randint(1,6)
	
# d8 protocol
if dice == 8:
	print "You chose d8"
	print lambda :randint(1,8)

# d12 protocol
if dice == 12:
	print "You chose d12"
	print lambda :randint(1,12)
	
# d20 protocol
if dice == 20:
	print "You chose d20"
	print lambda :randint(1,20)

