import pandas as pd
import Metrics as ms
import matplotlib.pyplot as plt



d = pd.concat(
    [pd.read_csv(f'measured/SA/salta_h_{year}.csv') for year in range(2009, 2022)],
    ignore_index=True
)

d['date'] = pd.to_datetime(d.date)

d = d.sort_values(['date'])




lsaf = pd.read_csv('LSASAF/sa.csv')
lsaf['date'] = pd.to_datetime(lsaf.date)
lsaf = (lsaf.set_index('date')
      .reindex(d.date)
      .rename_axis(['date'])
      #.fillna(0)
      .reset_index())

d['GHIl'] = lsaf.GHI.values


era = pd.read_csv('ERA/sa.csv')
era['date'] = pd.to_datetime(era.date)


era = (era.set_index('date')
      .reindex(d.date)
      .rename_axis(['date'])
      #.fillna(0)
      .reset_index())

from datetime import timedelta
merra = pd.read_csv('MERRA/sa.csv')
merra['date'] = pd.to_datetime(merra.date)


merra = (merra.set_index('date')
      .reindex(d.date)
      .rename_axis(['date'])
      #.fillna(0)
      .reset_index())


d['GHIera'] = era.ghi.values
d['GHImerra'] = merra.swfdn.values


plt.figure()
plt.plot(d.date, d.ghi)
plt.plot(d.date, d.GHI)
plt.plot(d.date, d.GHIl)
plt.plot(d.date, d.GHIera)
plt.plot(d.date, d.GHImerra)


d = d.dropna()
d = d[d.SZA<80]

ms.rmbe(d.ghi, d.GHImerra)

from sklearn.model_selection import train_test_split

dTrain = d[d.date.dt.year == 2013]

dTrain, dVal = train_test_split(

    dTrain, test_size=0.33, random_state=42)


dTest = d[d.date.dt.year != 2013]



dTrain.to_csv('Procesed/sa_train.csv', index=False)
dVal.to_csv('Procesed/sa_val.csv', index=False)
dTest.to_csv('Procesed/sa_test.csv', index=False)


