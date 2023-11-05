# badanie przy pomocy testu studenta ttest_1samp
from scipy import stats
import numpy as np
import pandas as pd
import math
# odczyt danych z pliku excela 
dane = pd.read_excel('cw2.xlsx')
okrpret = np.array(dane[11:21]["Unnamed: 4"])# tablica zawierająca zmierzone czasy 1 okresu dla wahadła z prętem
okrpierscien = np.array(dane[11:21]["Unnamed: 9"])# -||- dla wahadła z pierścieniem

# deklaracja zmierzonych wielkości dla prętu oraz pierścienia
apret = 0.2713
apierscien = 0.13885
mpret = 0.6490
mpierscien = 1.4270

# tablice z wyliczonymi momentami bezwładności metodą wahadła dla obu brył
Iwahpierscien = (okrpierscien**2*mpierscien*9.81*apierscien)/(4*math.pi**2)
Iwahpret = (okrpret**2*mpret*9.81*apret)/(4*math.pi**2)

# momentamy bezwładności wyznaczone metodą geometryczną dla obu brył
Igeompret = 0.0773
igeompierscien = (1/2)*mpierscien*(0.1459**2+0.13035**2) + mpierscien*apierscien**2

# prezentacja wyników dla pierścienia oraz przeprowadzenie testu statystycznego
print("peirscienie")
print(f"I wyznaczone geometrycznie {igeompierscien:.3f}" )
a = [ round(num, 3) for num in Iwahpierscien] 
print(f"wyznaczone I metodą wahadła {a}" )
print(stats.ttest_1samp(list(Iwahpierscien), igeompierscien)) #(TtestResult(statistic=22.31420225105308, pvalue=3.449912643778628e-09, df=9))

print()
# prezentacja wyników dla pręta oraz przeprowadzenie testu statystycznego
print("prety")
print(f"I wyznaczone geometrycznie {Igeompret:.3f}")
b =[ round(num,3) for num in Iwahpret]
print(f"wyznaczone I metodą wahadła {b}")
print(stats.ttest_1samp(list(Iwahpret), Igeompret))
