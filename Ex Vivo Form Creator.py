import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = r"C:\Users\Admin\Desktop\P_Voltammetry_Data.xlsm"
df = pd.read_excel(path)

df1p = df[(df['File Name'].str.find('1p')> -1)]

'''Creates list of drug names based on file name'''
Drug_List = []
for name in df1p['File Name']:
    if name.find('cont') > -1:
        Drug_List.append('Control')
    elif name.find('nor') > -1:
        Drug_List.append('norBNI')
    elif name.find('50488') > -1 :
        Drug_List.append(('u50,488'))

df1p['Drug'] = Drug_List
ctrMeans = df1p[df1p['Drug'] == 'Control'].reset_index().sort_index(ascending=False).loc[len(df1p[df1p['Drug'] == 'Control'])-1:len(df1p[df1p['Drug'] == 'Control'])-5].mean()
normdf= df/ctrMeans

print(normdf)


