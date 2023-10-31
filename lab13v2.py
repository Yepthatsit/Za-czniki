#import niezbędnych bibliotek
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats

#tablica zawierająca czasy spadku kulki zmierzone na odcinkach o długości 80 cm.
tzm = np.array([7.16,7.75,8.34,8.93,9.52,10.11,10.7,11.29,11.88,12.47])

#deklaracja parametrów badanej kulki oraz wyznaczenie prędkości granicznej
m = 0.000374
d = 0.00394
mw = 1/6*math.pi*d**3*1261
k = (6)*math.pi*d*0.519*(1+2.4*(d/0.039))
vgr = (9.81*(m-mw))/k

vsrnaprzedz = 0.8/tzm #utworzenie tablicy zawierającej prędkości wyznaczone przy pomocy tablicy tzm

print(vsrnaprzedz)# prezentacja wyznaczonych prędkości

print(stats.ttest_1samp(vsrnaprzedz,vgr))  # przeprowadzenie testy statystycznego oraz wypisanie jego rezultatów (TtestResult(statistic=3.136681058362772, pvalue=0.011991948710394872, df=9))
