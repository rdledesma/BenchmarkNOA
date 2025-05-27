import pandas as pd 

d = pd.DataFrame()

for year in range(2021, 2024):
    d = pd.concat([d, pd.read_csv(f'LSASAF/LQ/LQ_LSA-SAF_{year}.csv', usecols=['date','GHI'])])



d = d.sort_values(['date'])


d['date'] = pd.to_datetime(d.date)
d= d.resample(
                        '60 min', 
                        on='date', 
                        ).mean().reset_index()

d.to_csv('LSASAF/lq.csv', index=False)
