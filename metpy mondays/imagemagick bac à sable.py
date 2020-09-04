# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:39:43 2019

@author: Emmanuel
"""

#!/usr/bin/python
import imagemagick

 # Use the Python Imaging Library to create a Tk display
 dpy = Magick.TkDisplay(startmain=0)

 # Read the image
 img = Magick.read('test.gif')

 # Display the image
 dpy(img)
 dpy(img.Swirl(90))

 dpy.startmain=1
 dpy.show()