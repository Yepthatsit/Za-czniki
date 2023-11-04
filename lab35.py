import numpy as np
import pandas as pd
import math
#defnicja stałych
I = 0.5# natężenie[A]
klasaAmp = 0.5 #klasa amperomierza
zakresAmp = 75* 0.001
uI = (klasaAmp*zakresAmp)/100
t = 30*60 #czas elektrolizy[s]
ut = 0.2 #niepewność pomiaru czasu
tustI = 20# czas do ustawienia natężenia [s]
ZCu = 2 #st utlenienia jonu miedzi


#odczyt danych z excela
data = pd.read_excel("lab4_cw35.xlsx")
print (data)

# odczyt masy katody przed elektrolizą oraz jej niepewność
mkatodprzed = np.array(data.loc[5, "Unnamed: 5" : "Unnamed: 7" ])
srmkatprzed = mkatodprzed.mean() #metoda .mean() oblicza średnią z tablicy
mkatprzederror = math.sqrt(mkatodprzed.std()**2 + 0.001**2/3)# metoda .std() oblicza odchylenie standardowe średniej z tablicy
print(f'Zmierzone masy katody przed: {mkatodprzed} obliczona wartość średnia {srmkatprzed} +/- {mkatprzederror} (sqrt({mkatodprzed.std()}^2 + 0.001^2))')
print()

#odczyt masy 1 anody oraz obliczanie jej niepewności przed elektrolizą
m1anodprzed = np.array(data.loc[8, "Unnamed: 5" : "Unnamed: 7" ])
srm1anodprzed = m1anodprzed.mean()
m1anodprzederror = math.sqrt(m1anodprzed.std()**2 + 0.001**2/3)
print(f'Zmierzone masy 1 anody przed: {m1anodprzed} obliczona wartość średnia {srm1anodprzed} +/- {m1anodprzederror} (sqrt({m1anodprzed.std()}^2 + 0.001^2))')

#odczyt masy 2 anody oraz obliczanie jej niepewności przed elektrolizą
m2anodprzed = np.array(data.loc[9, "Unnamed: 5" : "Unnamed: 7" ])
srm2anodprzed = m2anodprzed.mean()
m2anodprzederror = math.sqrt(m2anodprzed.std()**2 + 0.001**2/3)
print(f'Zmierzone masy 2 anody przed: {m2anodprzed} obliczona wartość średnia {srm2anodprzed} +/- {m2anodprzederror} (sqrt({m2anodprzed.std()}^2 + 0.001^2))')
print()

# odczyt masy katody po elektrolizie oraz jej niepewność
mkatodypo = np.array(data.loc[6, "Unnamed: 5" : "Unnamed: 7" ])
srmkatodypo = mkatodypo.mean()
mkatodypoerror = math.sqrt(mkatodypo.std()**2 + 0.001**2/3)
print(f'Zmierzone masy katody po: {mkatodypo} obliczona wartość średnia {srmkatodypo} +/-{mkatodypoerror} (sqrt({mkatodypo.std()}^2 + 0.001^2))')
print()

#odczyt masy 1 anody oraz obliczanie jej niepewności po elektrolizie z pyłem
m1anodypozp = np.array(data.loc[10, "Unnamed: 5" : "Unnamed: 7" ])
srm1anodypozp = m1anodypozp.mean()
m1anodypozperror = math.sqrt(m1anodypozp.std()**2 + 0.001**2/3)
print(f'Zmierzone masy 1 anody po z pyłem: {m1anodypozp} obliczona wartość średnia {srm1anodypozp} +/- {m1anodypozperror} (sqrt({m1anodypozp.std()}^2 + 0.001^2))')


#odczyt masy 2 anody oraz obliczanie jej niepewności po elektrolizie z pyłem
m2anodypozp = np.array(data.loc[11, "Unnamed: 5" : "Unnamed: 7" ])
srm2anodypozp = m2anodypozp.mean()
m2anodypozperror = math.sqrt(m2anodypozp.std()**2 + 0.001**2/3)
print(f'Zmierzone masy 2 anody po z pyłem: {m2anodypozp} obliczona wartość średnia {srm2anodypozp} +/- {m2anodypozperror} (sqrt({m2anodypozp.std()}^2 + 0.001^2))')
print()

#odczyt masy 1 anody oraz obliczanie jej niepewności po elektrolizie bez pyłem
m1anodypobp = np.array(data.loc[12, "Unnamed: 5" : "Unnamed: 7" ])
srm1anodypobp = m1anodypobp.mean()
m1anodypobperror = math.sqrt(m1anodypozp.std()**2 + 0.001**2/3)
print(f'Zmierzone masy 1 anody po bez pyłu: {m1anodypobp} obliczona wartość średnia {srm1anodypobp} +/- {m1anodypobperror} (sqrt({m1anodypobp.std()}^2 + 0.001^2))')


#odczyt masy 2 anody oraz obliczanie jej niepewności po elektrolizie bez pyłem
m2anodypobp = np.array(data.loc[13, "Unnamed: 5" : "Unnamed: 7" ])
srm2anodypobp = m2anodypobp.mean()
m2anodypobperror = math.sqrt(m2anodypobp.std()**2 + 0.001**2/3)
print(f'Zmierzone masy 2 anody po bez pyłu: {m2anodypobp} obliczona wartość średnia {srm2anodypobp} +/- {m2anodypobperror} (sqrt({m2anodypobp.std()}^2 + 0.001^2))')
print()

#wyznaczanie masy miedzi wydzielonej na katodzie oraz jej niepewności
mwydz = srmkatodypo - srmkatprzed
mwydzerr = mkatprzederror + mkatodypoerror
mmolCu = 63.546 # masa mollowa miedzi
print(f'wydzielona masa na katodzie wynosi {mwydz} +/- {mwydzerr}')#część miedzi pływała na CuSO4
print()

#wyznaczanie mas anod oraz ich błędów
#przed
manodprzed = srm1anodprzed + srm2anodprzed
manodprzederr = m1anodprzederror + m2anodprzederror
print()

#po bez proszku
manodpobp = srm1anodypobp + srm2anodypobp
manodpobperr = m1anodypobperror + m2anodypobperror
deltambp =manodprzed - manodpobp
deltambperr = manodpobperr + manodprzederr
print(f'różnica mas anod po usunięciu proszku wynosi: {deltambp} +/- {deltambperr}')
print()

#z proszkiem
manodpozp = srm1anodypozp + srm2anodypozp
manodpozperr = m1anodypozperror + m2anodypozperror
deltamzp =manodprzed - manodpozp
deltamzperr = manodpozperr + manodprzederr
print(f'różnica mas anod przed usunięciem proszku wynosi: {deltamzp} +/- {deltamzperr}')
print()

# obliczanie stałej faradaya dla masy wydzielonej na katodzie
F = (I*(t)*mmolCu)/(ZCu*mwydz)
UI = ((t*mmolCu)*uI/(ZCu*mwydz))**2
Ut = ((I*mmolCu)*ut/(ZCu*mwydz))**2
Um = ((I*t*mmolCu)*mwydzerr/(ZCu*mwydz**2))**2
Uf = math.sqrt(UI + Um + Ut)
print(f'Uf = sqrt({UI + Um + Ut})')  
print(f'wyznaczona stała F wynosi: {F} +/- {Uf}')
print()

# obliczanie stałej faradaya dla masy, jaka ubyła na anodach z proszkiem(powinna kompensować pływającą w cuso4 miedź)
Fazp = (I*(t)*mmolCu)/(ZCu*deltamzp)
UIazp = ((t*mmolCu)*uI/(ZCu*deltamzp))**2
Utazp = ((I*mmolCu)*ut/(ZCu*deltamzp))**2
Umazp = ((I*t*mmolCu)*deltamzperr/(ZCu*deltamzp**2))**2
Ufazp = math.sqrt(UIazp + Umazp + Utazp) 
print(f'Uf = sqrt({UIazp + Umazp + Utazp})')   
print(f'wyznaczona stała F wynosi: {Fazp} +/- {Ufazp}')
print()

# obliczanie stałej faradaya dla masy, jaka ubyła na anodach bez proszku(powinna kompensować pływającą w cuso4 miedź)
Fabp = (I*(t)*mmolCu)/(ZCu*deltambp)
UIabp = ((t*mmolCu)*uI/(ZCu*deltambp))**2
Utabp = ((I*mmolCu)*ut/(ZCu*deltambp))**2
Umabp = ((I*t*mmolCu)*deltambperr/(ZCu*deltambp**2))**2
Ufabp = math.sqrt(UIabp + Umabp + Utabp) 
print(f'Uf = sqrt({UIabp + Umabp + Utabp})')   
print(f'wyznaczona stała F wynosi: {Fabp} +/- {Ufabp}')
print()

#wynik działania programu
'''
Zmierzone masy katody przed: [124.6 124.6 124.59] obliczona wartość średnia 124.59666666666665 +/- 0.004749268949587413 (sqrt(0.004714045207906029^2 + 0.001^2/3))

Zmierzone masy 1 anody przed: [141.878 141.88 141.878] obliczona wartość średnia 141.87866666666665 +/- 0.0011055415967889724 (sqrt(0.0009428090415865652^2 + 0.001^2/3))
Zmierzone masy 2 anody przed: [136.506 136.509 136.504] obliczona wartość średnia 136.50633333333334 +/- 0.0021343747458085587 (sqrt(0.002054804667653842^2 + 0.001^2/3))

Zmierzone masy katody po: [124.778 124.784 124.783] obliczona wartość średnia 124.78166666666668 +/-0.0026874192494321636 (sqrt(0.0026246692913365678^2 + 0.001^2/3))

Zmierzone masy 1 anody po z pyłem: [141.742 141.743 141.742] obliczona wartość średnia 141.74233333333333 +/- 0.0007453559925013534 (sqrt(0.00047140452079328255^2 + 0.001^2/3))
Zmierzone masy 2 anody po z pyłem: [136.377 136.381 136.376] obliczona wartość średnia 136.37800000000001 +/- 0.0022360679774970442 (sqrt(0.002160246899466445^2 + 0.001^2/3))

Zmierzone masy 1 anody po bez pyłu: [141.735 141.735 141.731] obliczona wartość średnia 141.73366666666666 +/- 0.0007453559925013534 (sqrt(0.0018856180831731304^2 + 0.001^2/3))
Zmierzone masy 2 anody po bez pyłu: [136.375 136.371 136.376] obliczona wartość średnia 136.374 +/- 0.0022360679774970442 (sqrt(0.002160246899466445^2 + 0.001^2/3))

wydzielona masa na katodzie wynosi 0.1850000000000307 +/- 0.007436688199019577


różnica mas anod po usunięciu proszku wynosi: 0.2773333333333312 +/- 0.006221340312595929

różnica mas anod przed usunięciem proszku wynosi: 0.26466666666664196 +/- 0.006221340312595929

Uf = sqrt(38621413.66841385)
wyznaczona stała F wynosi: 154571.35135132572 +/- 6214.612913803549

Uf = sqrt(6456898.744744739)
wyznaczona stała F wynosi: 108044.20654912847 +/- 2541.0428459088876

Uf = sqrt(5356201.594680485)
wyznaczona stała F wynosi: 103109.49519230849 +/- 2314.3469045673523
'''
