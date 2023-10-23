# %%
import pandas as pd
import numpy as np

paises = ['FIN','JP','EUA','CG','LX','IS','SUE']
anos = ['2000', '2005', '2009']
ano2000 = [6731,5151,4545,4245,3773,np.NaN,np.NaN]
ano2005 = [7544,5360,4612,np.NaN,np.NaN,7261,6100]
ano2009 = [7643,5147,np.NaN,6149,4810,9117,5046]
dfPeD = pd.DataFrame([ano2000,ano2005,ano2009],
        anos, paises)
print(dfPeD)

dfPeD_1 = dfPeD.copy()
dfPeD_1.fillna(value=dfPeD_1.mean(), inplace=True)
print('\n')
print(dfPeD_1)

# %%

print(dfPeD)
print(dfPeD_1)

dfPeD_2 = dfPeD.copy()
#pd.isna(dfPeD_2['EUA'].iloc[2])

def subst_na(series):
    indice = 0
    if pd.isna(series.iloc[indice]):
        series.iloc[indice] = series.iloc[indice+1]
        indice+=1
    elif pd.isna(series.iloc[indice+1]):
         series.iloc[indice+1] = series.iloc[indice]
    elif pd.isna(series.iloc[indice+2]):
        series.iloc[indice+2] = series.iloc[indice+1]

print(dfPeD_2)
subst_na(dfPeD_2['EUA'])
subst_na(dfPeD_2['CG'])
subst_na(dfPeD_2['LX'])
subst_na(dfPeD_2['IS'])
subst_na(dfPeD_2['SUE'])
dfPeD_2

# %%
