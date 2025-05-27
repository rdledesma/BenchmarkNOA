import pandas as pd 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import Metrics as ms

dTrain = pd.read_csv('Procesed/lq_train.csv')
dVal = pd.read_csv('Procesed/lq_val.csv')
dTest = pd.read_csv('Procesed/lq_test.csv')



modelCams = LinearRegression().fit(dTrain.GHI.values.reshape(-1,1), dTrain.ghi - dTrain.GHI)
modelLsa = LinearRegression().fit(dTrain.GHIl.values.reshape(-1,1), dTrain.ghi)
modelEra = LinearRegression().fit(dTrain.GHIera.values.reshape(-1,1), dTrain.ghi)
modelMerra = LinearRegression().fit(dTrain.GHImerra.values.reshape(-1,1), dTrain.ghi)



dTest['adapCams'] = modelCams.predict(dTest.GHI.values.reshape(-1,1)) + dTest.GHIcc
dTest['adapLsa'] = modelCams.predict(dTest.GHIl.values.reshape(-1,1))
dTest['adapEra'] = modelCams.predict(dTest.GHIera.values.reshape(-1,1))
dTest['adapMerra'] = modelCams.predict(dTest.GHImerra.values.reshape(-1,1))


plt.figure()
plt.plot(dTest.ghi)
plt.plot(dTest.GHI)
plt.plot(dTest.adapCams)


print(ms.rrmsd(dTest.ghi, dTest.GHI))
print(ms.rrmsd(dTest.ghi, dTest.GHIl))
print(ms.rrmsd(dTest.ghi, dTest.GHIera))
print(ms.rrmsd(dTest.ghi, dTest.GHImerra))


# ms.rrmsd(dTest.ghi, dTest.GHI)
# ms.rrmsd(dTest.ghi, dTest.adapCams)

# ms.rrmsd(dTest.ghi, dTest.GHIl)
# ms.rrmsd(dTest.ghi, dTest.adapLsa)

# ms.rrmsd(dTest.ghi, dTest.GHIera)
# ms.rrmsd(dTest.ghi, dTest.adapEra)

# ms.rrmsd(dTest.ghi, dTest.GHImerra)
# ms.rrmsd(dTest.ghi, dTest.adapMerra)



