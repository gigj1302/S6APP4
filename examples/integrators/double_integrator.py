# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 10:17:36 2018

@author: Alexandre
"""

###############################################################################
import numpy as np

###############################################################################
from pyro.dynamic  import integrator
from pyro.analysis import costfunction
    
###################################
# Simple integrator
###################################

di = integrator.DoubleIntegrator()

di.ubar = np.array([1]) # constant input = 1


###################################
# Analysis
###################################
    
# Phase plane behavior test
di.plot_phase_plane()

# Simulation
sim = di.compute_trajectory(x0=np.array([0,0]))
di.get_plotter().plot(sim)
di.get_plotter().plot(sim, 'y')


# Cost computing

# Weights for quadratic cost function
q, r, v = np.ones(di.n), np.ones(di.m), np.ones(di.p)

qcf = costfunction.QuadraticCostFunction(q, r, v)
di.get_plotter().plot(sim, 'xuj', cost=qcf.eval(di.sim))

# Time cost
tcf = costfunction.TimeCostFunction( di.xbar )
di.get_plotter().plot(sim, 'j', cost=tcf.eval(sim))

# Phase plane trajectory
di.get_plotter().phase_plane_trajectory( sim )