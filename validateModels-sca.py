import pandas as pd
import Metrics as ms
import matplotlib.pyplot as plt


d1 = pd.read_csv("measured/sca/test.csv")
d1['date'] = pd.to_datetime(d1.date)
d1 = d1.sort_values(['date'])



d2 = pd.read_csv("measured/sca/train.csv")
d2['date'] = pd.to_datetime(d2.date)
d2 = d2.sort_values(['date'])


d3 = pd.read_csv("measured/sca/val.csv")
d3['date'] = pd.to_datetime(d3.date)
d3 = d3.sort_values(['date'])





d = pd.concat([d1,d2,d3]).sort_values(['date'])




lsaf = pd.read_csv('LSASAF/sca.csv')
lsaf['date'] = pd.to_datetime(lsaf.date)
lsaf = (lsaf.set_index('date')
      .reindex(d.date)
      .rename_axis(['date'])
      #.fillna(0)
      .reset_index())

d['GHIl'] = lsaf.GHI.values


from datetime import timedelta
merra = pd.read_csv('MERRA/sca.csv')
merra['date'] = pd.to_datetime(merra.date)- timedelta(minutes=30)


merra = (merra.set_index('date')
      .reindex(d.date)
      .rename_axis(['date'])
      #.fillna(0)
      .reset_index())

d['GHImerra'] = merra.swfdn.values


plt.figure()
plt.plot(d.date, d.ghi)
plt.plot(d.date, d.GHI)
plt.plot(d.date, d.GHIl)
plt.plot(d.date, d.GHIera)
plt.plot(d.date, d.GHImerra)


d = d.dropna()
ms.rmae(d.ghi, d.GHI)



