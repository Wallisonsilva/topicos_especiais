#!/usr/bin/env python3

import random
import numpy as np
from scipy.spatial.distance import cdist
from datetime import datetime
import pandas as pd

instalacoes = pd.read_csv('instalacoes.csv')
print(instalacoes)

start = datetime.now()

# Let's get some repeatable randomness
np.random.seed(42)

# Number of points, number of iterations
Npts, Niter = 1000, 1

# Generate the Npts random X,Y points
dataset = np.random.rand(Npts,2)

# Run lots of iterations for better timing
for n in range(Niter):

   # Generate random red pixel (X,Y)
   red = [-22.8394126, -42.0192303]

   # Work out a Boolean mask for the 4 quadrants
   above = instalacoes[:,3]>red[0,0]
   right = instalacoes[:,4]>red[0,1]
 
   Q1 = np.logical_and(above,right)       # top-right
   Q2 = np.logical_and(above,~right)      # top-left
   Q3 = np.logical_and(~above,~right)     # bottom-left
   Q4 = np.logical_and(~above,right)      # bottom-right

   Q = 1
   for quadrant in [Q1,Q2,Q3,Q4]:
       print(f'Quadrant {Q}: ')
       # Boolean mask to select points in this quadrant
       thisQuad = dataset[quadrant]
       l = len(thisQuad)
       if l==0:
           print('No points in quadrant')
           continue
       # print(f'nPoints in quadrant: {l}')
       # print(f'Points: {dataset[quadrant]}')
       # Calculate distance of each point in dataset to red point
       distances = cdist(thisQuad, red, 'sqeuclidean')
       # Choose nearest
       idx = np.argmin(distances)
       print(idx)
       print(f'Index: {idx}, point: {thisQuad[idx]}, distance: {distances[idx]}')
       Q += 1

print(datetime.now() - start)