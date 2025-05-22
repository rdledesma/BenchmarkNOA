import pandas as pd
import Metrics as ms
import matplotlib.pyplot as plt


d1 = pd.read_csv("measured/yu/test.csv")
d1['date'] = pd.to_datetime(d1.date)
d1 = d1.sort_values(['date'])

d1= d1.resample(
                        '60 min', 
                        on='date', 
                        ).mean().reset_index()



d2 = pd.read_csv("measured/yu/train.csv")
d2['date'] = pd.to_datetime(d2.date)
d2 = d2.sort_values(['date'])

d2= d2.resample(
                        '60 min', 
                        on='date', 
                        ).mean().reset_index()



d3 = pd.read_csv("measured/yu/val.csv")
d3['date'] = pd.to_datetime(d3.date)
d3 = d3.sort_values(['date'])



d3= d3.resample(
                        '60 min', 
                        on='date', 
                        ).mean().reset_index()






d = pd.concat([d1,d2,d3]).sort_values(['date'])




lsaf = pd.read_csv('LSASAF/yu.csv')
lsaf['date'] = pd.to_datetime(lsaf.date)
lsaf = (lsaf.set_index('date')
      .reindex(d.date)
      .rename_axis(['date'])
      #.fillna(0)
      .reset_index())

d['GHIl'] = lsaf.GHI.values


era = pd.read_csv('ERA/yu.csv')
era['date'] = pd.to_datetime(era.date)


era = (era.set_index('date')
      .reindex(d.date)
      .rename_axis(['date'])
      #.fillna(0)
      .reset_index())

from datetime import timedelta
merra = pd.read_csv('MERRA/yu.csv')
merra['date'] = pd.to_datetime(merra.date)- timedelta(minutes=30)


merra = (merra.set_index('date')
      .reindex(d.date)
      .rename_axis(['date'])
      #.fillna(0)
      .reset_index())


d['GHIera'] = era.GHIe.values
d['GHImerra'] = merra.swfdn.values


plt.figure()
plt.plot(d.date, d.ghi)
plt.plot(d.date, d.GHI)
plt.plot(d.date, d.GHIl)
plt.plot(d.date, d.GHIera)
plt.plot(d.date, d.GHImerra)


d = d.dropna()
ms.rmae(d.ghi, d.GHImerra)



