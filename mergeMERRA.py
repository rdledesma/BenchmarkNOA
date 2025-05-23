import pandas as pd 

d = pd.DataFrame()


d1 = pd.read_csv('MERRA/SA/sa.csv')
d2 = pd.read_csv('MERRA/SA/sa1.csv')
d3 = pd.read_csv('MERRA/SA/sa2.csv')


d = pd.concat([d1,d2,d3])

d['date'] = pd.to_datetime(d.date)
d = d[['date', 'swgnt', 'swfdn']]

d = d.sort_values(['date'])


d= d.resample(
                        '60 min', 
                        on='date', 
                        ).mean().reset_index()

d.to_csv('MERRA/sa.csv', index=False)
