import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.stats as stat
#ttest studenta albo chi2 żeby porównać 100 pom z rozkładem normalnym
#zrobić histogram dla 100 pomiarów i porównać z gaussem
dane = pd.read_excel('lab5_cw2.xlsx')
print(dane)
kat = np.array(dane[2:14]['Unnamed: 8'])*2*math.pi/360
ukat = 2*math.pi/360
print(kat)
okresy = np.array(dane[2:14]['Unnamed: 10'])
pom100 = np.array(dane[2:102]['Unnamed: 14'])
print(okresy)
t0 = pom100.mean()/3
ut0 = math.sqrt(pom100.std()**2 + 0.2)/3

okr1 = (okresy-t0)/t0
uokr1 = []
for i in okresy:
    uokr1.append(math.sqrt(( (i/(t0**2)*0.2/50)**2 + 1/t0*0.2/50)**2))
katytor = np.linspace(5*(2*math.pi/360),60*(2*math.pi/360))
Tteor = ((1/16)*(katytor**2))
fig, plots = plt.subplots(2)
plots[0].plot(katytor,Tteor,label = 'teoretyczna',color = 'orange')
plots[0].plot(kat,okr1,label = 'pomiary',color = 'blue')
plots[0].scatter(kat,okr1)
plots[0].errorbar(kat,okr1,xerr=ukat,yerr=uokr1)
plots[0].legend()
t0tab = pom100/3
plots[1].hist(t0tab,bins = 10)
xmin ,xmax = plt.xlim()
x_ax = np.linspace(xmin,xmax)
print(f'Wynik testy studenta: {stat.ttest_1samp(list(t0tab),2*math.pi*math.sqrt(0.415/9.81))}\n')
#print(f'wynik testy chi^2: {stat.chisquare(list(t0tab),2*math.pi*math.sqrt(0.415/9.81))}\n')
plots[1].plot(x_ax,stat.norm.pdf(x_ax,t0,t0tab.std()))
plt.show()
