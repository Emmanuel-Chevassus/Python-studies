# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:37:51 2019

@author: Emmanuel
"""

from datetime import datetime
date=datetime(2018,9,10,0)
station='KEY'

from siphon.simplewebservice.wyoming import WyomingUpperAir

df=WyomingUpperAir.request_data(date,station)

df.units

df.units['dewpoint']

from metpy.units import units

p=df['pressure'].values*units(df.units['pressure'])

