# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 15:27:04 2016

@author: alex
"""

from AlexRobotics.planning import RandomTree    as RPRT
from AlexRobotics.dynamic  import Manipulator   as M

import numpy as np

R  =  M.OneLinkManipulator()

x_start = np.array([0,0])

RRT = RPRT.RRT( R , x_start )

RRT.compute_steps(1000,True)