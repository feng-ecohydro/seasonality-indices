#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:33:38 2019

This code produces Figure 1 of Feng et al. GRL
@author: xuefeng
"""

import numpy as np
import matplotlib.pyplot as plt

output_figs = True  # output illustrative figures  
nincre = 10         # number of increment for contourplot     
K_amp_scale = 1.0   # scaling factor for amplitude of PET relative to PET mean 
P_amp_scale = 1.0   # scaling factor for P amp relative to P mean
Ptot = 1            # total annual precipitation in meters
PETtot = 1          # total annual PET in meters     

def defineParams(tAnnual, dtheta, Pp, Kp):
    tAnnShifted = np.mod(tAnnual+int(dtheta/dt),len(tAnnual))
    P = Pp[0] - Pp[1]*np.cos(tAnnShifted*2*np.pi/len(tAnnual))
    K = Kp[0] - Kp[1]*np.cos(tAnnual*2*np.pi/len(tAnnual))
    return P,K

def reshape_daily(x, func=np.mean):
    ''' input is a single year trajectory of length dyear/dt, 
    taking either daily means or sums'''
    r = func(np.reshape(x, (dyear, int(1/dt))), axis=1)
    return r

def reshape_monthly(x, func=np.mean):
    ''' input is a single year trajectory of length dyear/dt, 
    taking either monthly means or sums'''
    rd = reshape_daily(x) # now 365. 
    rm = [np.sum(i) for i in np.split(rd, mic[:-1])]
    return rm

def get_JSDiv(prcp_pdf, temp_pdf):    
    M = 0.5*(temp_pdf + prcp_pdf)
    pre = prcp_pdf[prcp_pdf>0]; M1 = M[prcp_pdf>0]
    tmp = temp_pdf[temp_pdf>0]; M2 = M[temp_pdf>0]
    DivRM = np.sum(pre * np.log2(pre/M1))
    DivPM = np.sum(tmp * np.log2(tmp/M2))
    JSDiv = np.round( 0.5*(DivRM + DivPM), 10)
    return JSDiv 

def get_synchronicity(prcp_pdf, temp_pdf):
    JSDiv_m = np.zeros(12)
    for m_shift in range(12): 
        temp_rolled = np.roll(temp_pdf, m_shift)
        JSDiv_m[m_shift] = get_JSDiv(prcp_pdf, temp_rolled)
    diffJSDiv = np.sqrt( JSDiv_m[0] - np.min(JSDiv_m) ) 
    return diffJSDiv

# simulation parameters
dt = 1.0                                    # increment of temporal variation, in days
dyear = 365                                 # days per year
tRunAnnual = int(dyear/dt)                  # number of time points in a year
tAnnual = np.arange(tRunAnnual)             # annual time series 
mi = [30,30,31,30,31,30,30,31,30,31,30,31]  # divide each month evenly into roughly 30 or 31 days
mic = np.cumsum(mi)                         # cumulative monthly increments

# climatic and soil paramaters 
alpha = 0.01            # mean rainfall depth/day in meters
nZr = 0.45*1.0          # soil water storage: porosity times rooting depth in m
gam = nZr / alpha;      # normalized soil water storage with respect to mean rainfall depth

# reworking the climatic and soil parameters into sinusoidal parameters 
P_mu = Ptot/(alpha*dyear)       # mean frequency of precipitation/day
K_mu = PETtot/(nZr*dyear)       # normalized PET per day
max_amp_ratio = (PETtot*K_amp_scale)/ (Ptot*P_amp_scale);   # maximum amplitude ratio based on amp_scales

P_amp = P_mu * P_amp_scale      # P amplitude
K_amp = K_mu * K_amp_scale      # PET amplitude 
Kp = (K_mu, K_amp)              # PET parameters specified 

# contour figure needs to vary by amplitude ratios and dtheta
dthetaList = np.linspace(1,180,nincre)                      # dtheta increments
amp_ratio_range = np.linspace(0.01, max_amp_ratio, nincre)  # amp_ratio between PET and P
PpList = [(P_mu, P_amp * amp_ratio / max_amp_ratio) for amp_ratio in amp_ratio_range]   # P parameters varies by changes in its relative ratio to PET

s_arr = np.zeros((len(PpList), len(dthetaList)))    # store output values of asynchronicity index
for i, Pp in enumerate(PpList):
    for j, dtheta in enumerate(dthetaList):
        
        # Governing environmental parameters, over annual cycle
        P,K = defineParams(tAnnual, dtheta, Pp, Kp)
        pet = K * nZr           # recalculate daily pet amount (m)
        prcp = P * alpha        # recalculate daily rainfall amount (m)
        PETmonthly, PRmonthly = [ np.array(reshape_monthly(Vseries)) for Vseries in [pet, prcp]]
        s_arr[i,j] = get_synchronicity(PETmonthly/np.sum(PETmonthly), PRmonthly/np.sum(PRmonthly))
        
        if output_figs: 
            plt.figure(figsize=(4,3))
            plt.plot(PRmonthly, lw=5); plt.plot(PETmonthly, lw=5)
            plt.title('dtheta:'+str(np.round(dtheta,3))+', ratio:'+str(np.round(amp_ratio_range[i],3)))

# Figure 1 contour panel 
plt.figure(figsize=(5, 4.5))
x2d, y2d = np.meshgrid(dthetaList, amp_ratio_range)
CS = plt.contour(s_arr, np.arange(0.1,0.61,0.1), colors='k', linewidths=1)
plt.clabel(CS, inline=True, fontsize=10, colors='k')
plt.xlabel('Phase shift')
plt.ylabel('Relative magnitude')
