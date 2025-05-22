import pandas as pd 

d1 = pd.read_csv('LSASAF/YU/YU_LSA-SAF_2017.csv', usecols=['date','GHI'])
d2 = pd.read_csv('LSASAF/YU/YU_LSA-SAF_2018.csv', usecols=['date','GHI'])
d3 = pd.read_csv('LSASAF/YU/YU_LSA-SAF_2019.csv', usecols=['date','GHI'])



d = pd.concat([d1,d2,d3]).sort_values(['date'])


d['date'] = pd.to_datetime(d.date)
d= d.resample(
                        '60 min', 
                        on='date', 
                        ).mean().reset_index()

d.to_csv('LSASAF/yu.csv', index=False)