import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

path = r"C:\Users\Admin\Documents\Masters Stuff\MStim + USVs Exported Excel Files\Rat 2 MStim Preference.xlsx"
df = pd.read_excel(path)

'''Creates Rewarding v Aversie columns sorted at 25 kHz'''
df['Rewarding/Aversive'] = df['Principal Frequency (kHz)'].apply(lambda x : 'Rewarding' if x > 25 else 'Aversive' )




'''Create time bins'''
df['Bins'] = pd.cut(df['Adjusted Time'],bins=150)


'''Creates New Binned DF'''
Tot_Call_Bin = df.groupby(['Bins']).count()['ID']
Rew_Call_Bin = df[df['Rewarding/Aversive']=='Rewarding'].groupby(['Bins']).count()['ID']
Aver_Call_Bin = df[df['Rewarding/Aversive']=='Aversive'].groupby(['Bins']).count()['ID']
Av_Freq_Bin = df.groupby(['Bins']).mean()['Principal Frequency (kHz)'].fillna(0)

BinDF = pd.concat([Tot_Call_Bin,Rew_Call_Bin,Aver_Call_Bin,Av_Freq_Bin],axis=1)
BinDF.columns = ['Total Calls','Rewarding Calls','Aversive Calls','Average Principal Frequency']

pd.DataFrame.to_clipboard(BinDF)







