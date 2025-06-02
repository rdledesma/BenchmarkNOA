import pandas as pd
import matplotlib.pyplot as plt


meas = pd.read_csv('measured/ero/test.csv')
meas['date'] = pd.to_datetime(meas.date)
lsa = pd.read_csv('LSASAF/ero.csv')
lsa['date'] = pd.to_datetime(lsa.date)


plt.figure()
plt.plot(meas.date, meas.ghi, '-r', label="Measured")
plt.plot(meas.date, meas.GHI, '-b', label="CAMS")
plt.plot(lsa.date, lsa.GHI, '-g', label="LSA-SAF")
plt.legend()