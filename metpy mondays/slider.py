# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 18:15:18 2019

@author: Emmanuel
"""

import metpy.calc as mpcalc
from metpy.units import units
from ipywidgets import interact,FloatSlider,IntSlider

def calculate_dewpoint(temperature,rh):
    temperature=temperature*units.degF
    rh=rh*units.percent
    return round(mpcalc.dewpoint_rh(temperature, rh).to('degF'),1)

temperature_slider = FloatSlider(min=32,max=90,step=0.5,value=65)
rh_slider=IntSlider(min=1,max=100,value=50)

interact(calculate_dewpoint,temperature=temperature_slider,rh=rh_slider);