# Covered Call

import numpy as np
import matplotlib.pyplot as plt


#option_greek

#How much change in the underlaying affections the options price.
# Range of 0-100% (0.0 - 1.0)
# Also used a propability of being in the money at time of expirary. An option with 0.7 delta 
# has a 70% chance of being in the money at time of expirary.   
delta = .80

vega 

rho

#Rate of change of the underlying delta. A higher delta typically means a higher chance of volatility when it comes to the underlying. 
#Think of it as a second derivative of the dStockPrice/dt. Or first derivative of the delta
gamma 








# Create a plot using matplotlib 
fig, ax = plt.subplots()
ax.spines['top'].set_visible(False) # Top border removed 
ax.spines['right'].set_visible(False) # Right border removed
ax.spines['bottom'].set_position('zero') # Sets the X-axis in the center
ax.tick_params(top=False, right=False) # Removes the tick-marks on the RHS

plt.plot(sT,y1,lw=1.5,label='Long Stock')
plt.plot(sT,y2,lw=1.5,label='Short Call')
plt.plot(sT,y3,lw=1.5,label='Covered Call')

plt.title('Covered Call') 
plt.xlabel('Stock Prices')
plt.ylabel('Profit/loss')

plt.grid(True)
plt.axis('tight')
plt.legend(loc=0)
plt.show()