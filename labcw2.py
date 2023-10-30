# badanie przy pomocy testu studenta ttest_1samp
from scipy import stats
import numpy as np
import pandas as pd
import math
dane = pd.read_excel('cw2.xlsx')
okrpret = np.array(dane[11:21]["Unnamed: 4"])
okrpierscien = np.array(dane[11:21]["Unnamed: 9"])
apret = 0.2713
apierscien = 0.1451
mpret = 0.6490
mpierscien = 1.4270
Iwahpierscien = (okrpierscien**2*mpierscien*9.81*apierscien)/(4*math.pi**2)
Iwahpret = (okrpret**2*mpret*9.81*apret)/(4*math.pi**2)
Igeompret = 0.0773
igeompierscien = (1/2)*mpierscien*(0.1459**2+0.1303**2) + mpret*apierscien**2
print("peirscienie")
print("I wyznaczone geometrycznie " + str(igeompierscien))
print("wyznaczone I metodą wahadła " + str(Iwahpierscien))
print(stats.ttest_1samp(list(Iwahpierscien), igeompierscien))
print("prety")
print("I wyznaczone geometrycznie " + str(igeompierscien))
print("wyznaczone I metodą wahadła " + str(Iwahpierscien))
print(stats.ttest_1samp(list(Iwahpret), Igeompret))