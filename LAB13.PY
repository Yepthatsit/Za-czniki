# import wymaganych bibliotek.
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

#odczyt danych z pliku , deklaracja stałych
excel_dada = pd.read_excel("lab3_cw13.xlsx")
D = 0.039
l = 0.8
gestosc = 1249.10
g= 9.81
balldata = pd.DataFrame(excel_dada[5:15][["Unnamed: 3","Unnamed: 5","Unnamed: 7"]])
balldata.rename(columns={"Unnamed: 3":"srednica[m]","Unnamed: 5": "masa[kg]","Unnamed: 7":"czas_spadania[s]"},inplace=True)
balldata.index = [1,2,3,4,5,6,7,8,9,10]

#zamiana jednostek
balldata[:]["srednica[m]"] *= 0.001
balldata[:]["masa[kg]"] *= 0.001
print(balldata)# wypisanie odczytanych danych w formie dataframe

# obliczanie pynktów zbadanych dla linearyzacji y = (eta)x
x = np.array(balldata[:]["srednica[m]"]*(1 + 2.4*balldata[:]["srednica[m]"]/D)/(balldata[:]["masa[kg]"] - gestosc*math.pi*balldata[:]["srednica[m]"]**3/6),dtype=float)
y = np.array(g*balldata[:]["czas_spadania[s]"]/(3*math.pi*l))
print(x)# wypisanie wartości x
print(y)#wypisanie wartości y

model = sm.WLS(y, x, hasconst = True) # deklaracja modelu, przekazanie danych do modelu
results = model.fit() # fitowanie prostej najlepszego dopasowania
slope = results.params[0] # odczytanie współczynnika lepkości z dopasowanej prostej.
err = results.bse[0] # odczytanie niepewności dopasowanego współczynnika
print(str(slope) + " " + str(err)) # wypisanie współczynnika wraz z błędem

# tworzenie danych do wizualizacji prostej na wykresie
x2 = np.linspace(5,80)
y2 = slope*x2

plt.scatter(x=x,y=y)# naniesienie danych pomiarowych na wykres w formie punktów
plt.plot(x2,y2) # naniesienie prostej na wykres

#opisanie osi oraz pokazanie wykresu
plt.xlabel("x = d*(1 + 2.4*d/D)/(m - gestosc*math.pi*d**3/6)")
plt.ylabel("y = g*t/3/math.pi/l")
plt.show()
