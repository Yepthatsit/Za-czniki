import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
t = np.linspace(0,10)
tzm = np.array([7.16,7.75,8.34,8.93,9.52,10.11,10.7,11.29,11.88,12.47])
m = 0.000374
d = 0.00394
mw = 1/6*math.pi*d**3*1261
k = (6)*math.pi*d*0.519*(1+2.4*(d/0.039))
a = m/k
vgr = (9.81*(m-mw))/k
v  =  vgr - vgr*math.e**(-t/a)
vsrnaprzedz = 0.8/tzm
print(vsrnaprzedz)
print(stats.ttest_1samp(vsrnaprzedz,vgr))
