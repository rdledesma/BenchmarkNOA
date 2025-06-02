import pandas as pd 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import Metrics as ms

dTrain = pd.read_csv('Procesed/lq_train.csv')
dVal = pd.read_csv('Procesed/lq_val.csv')
dTest = pd.read_csv('Procesed/lq_test.csv')


# dTrain['date'] = pd.to_datetime(dTrain.date)
# dTest['date'] = pd.to_datetime(dTest.date)

# dTrain = dTrain.sort_values(['date'])

# plt.figure()
# plt.plot(dTrain.date, dTrain.ghi)
# plt.plot(dTrain.date, dTrain.GHI)
# plt.plot(dTrain.date, dTrain.GHIcc)




modelCams1 = LinearRegression().fit(dTrain.GHI.values.reshape(-1,1), dTrain.ghi) 
modelLsa1 = LinearRegression().fit(dTrain.GHIl.values.reshape(-1,1) , dTrain.ghi)
modelEra1 = LinearRegression().fit(dTrain.GHIera.values.reshape(-1,1) , dTrain.ghi)
modelMerra1 = LinearRegression().fit(dTrain.GHImerra.values.reshape(-1,1), dTrain.ghi)




modelCams2 = LinearRegression().fit(dTrain.GHI.values.reshape(-1,1), dTrain.ghi - dTrain.GHI) 
modelLsa2 = LinearRegression().fit(dTrain.GHIl.values.reshape(-1,1), dTrain.ghi - dTrain.GHI)
modelEra2 = LinearRegression().fit(dTrain.GHIera.values.reshape(-1,1), dTrain.ghi - dTrain.GHI)
modelMerra2 = LinearRegression().fit(dTrain.GHImerra.values.reshape(-1,1), dTrain.ghi - dTrain.GHI)



modelCams3 = LinearRegression().fit(dTrain.GHI.values.reshape(-1,1) - dTrain.GHIcc.values.reshape(-1,1) , dTrain.ghi - dTrain.GHIcc) 
modelLsa3 = LinearRegression().fit(dTrain.GHIl.values.reshape(-1,1) - dTrain.GHIcc.values.reshape(-1,1), dTrain.ghi - dTrain.GHIcc)
modelEra3 = LinearRegression().fit(dTrain.GHIera.values.reshape(-1,1) - dTrain.GHIcc.values.reshape(-1,1), dTrain.ghi - dTrain.GHIcc)
modelMerra3 = LinearRegression().fit(dTrain.GHImerra.values.reshape(-1,1) - dTrain.GHIcc.values.reshape(-1,1), dTrain.ghi - dTrain.GHIcc )




dTest['adapCams1'] =  modelCams1.predict(dTest.GHI.values.reshape(-1,1))
dTest['adapLsa1'] = modelLsa1.predict(dTest.GHIl.values.reshape(-1,1))
dTest['adapEra1'] = modelEra1.predict(dTest.GHIera.values.reshape(-1,1))
dTest['adapMerra1'] = modelMerra1.predict(dTest.GHImerra.values.reshape(-1,1)) 




dTest['adapCams2'] =  modelCams2.predict(dTest.GHI.values.reshape(-1,1))  + dTest.GHI.values
dTest['adapLsa2'] = modelLsa2.predict(dTest.GHIl.values.reshape(-1,1))+ dTest.GHI.values
dTest['adapEra2'] = modelEra2.predict(dTest.GHIera.values.reshape(-1,1))+ dTest.GHI.values
dTest['adapMerra2'] = modelMerra2.predict(dTest.GHImerra.values.reshape(-1,1)) + dTest.GHI.values


dTest['adapCams3'] =  modelCams3.predict(dTest.GHI.values.reshape(-1,1) - dTest.GHIcc.values.reshape(-1,1) )  + dTest.GHIcc.values
dTest['adapLsa3'] = modelLsa3.predict(dTest.GHIl.values.reshape(-1,1) - dTest.GHIcc.values.reshape(-1,1))+ dTest.GHIcc.values
dTest['adapEra3'] = modelEra3.predict(dTest.GHIera.values.reshape(-1,1) - dTest.GHIcc.values.reshape(-1,1))+ dTest.GHIcc.values
dTest['adapMerra3'] = modelMerra3.predict(dTest.GHImerra.values.reshape(-1,1) - dTest.GHIcc.values.reshape(-1,1)) + dTest.GHIcc.values


# plt.figure()
# plt.plot(dTest.ghi)
# plt.plot(dTest.GHI)
# plt.plot(dTest.adapCams)


print(ms.rmbe(dTest.ghi, dTest.GHI)) 
print(ms.rmbe(dTest.ghi, dTest.GHIl))
print(ms.rmbe(dTest.ghi, dTest.GHIera))
print(ms.rmbe(dTest.ghi, dTest.GHImerra))



print(ms.rmae(dTest.ghi, dTest.GHI)) 
print(ms.rmae(dTest.ghi, dTest.GHIl))
print(ms.rmae(dTest.ghi, dTest.GHIera))
print(ms.rmae(dTest.ghi, dTest.GHImerra))

print(ms.rrmsd(dTest.ghi, dTest.GHI)) 
print(ms.rrmsd(dTest.ghi, dTest.GHIl))
print(ms.rrmsd(dTest.ghi, dTest.GHIera))
print(ms.rrmsd(dTest.ghi, dTest.GHImerra))




print(ms.rmbe(dTest.ghi, dTest.adapCams1)) 
print(ms.rmbe(dTest.ghi, dTest.adapLsa1))
print(ms.rmbe(dTest.ghi, dTest.adapEra1))
print(ms.rmbe(dTest.ghi, dTest.adapMerra1))

print(ms.rmae(dTest.ghi, dTest.adapCams1)) 
print(ms.rmae(dTest.ghi, dTest.adapLsa1))
print(ms.rmae(dTest.ghi, dTest.adapEra1))
print(ms.rmae(dTest.ghi, dTest.adapMerra1))

print(ms.rrmsd(dTest.ghi, dTest.adapCams1)) 
print(ms.rrmsd(dTest.ghi, dTest.adapLsa1))
print(ms.rrmsd(dTest.ghi, dTest.adapEra1))
print(ms.rrmsd(dTest.ghi, dTest.adapMerra1))



print(ms.rmbe(dTest.ghi, dTest.adapCams2)) 
print(ms.rmbe(dTest.ghi, dTest.adapLsa2))
print(ms.rmbe(dTest.ghi, dTest.adapEra2))
print(ms.rmbe(dTest.ghi, dTest.adapMerra2))

print(ms.rmae(dTest.ghi, dTest.adapCams2)) 
print(ms.rmae(dTest.ghi, dTest.adapLsa2))
print(ms.rmae(dTest.ghi, dTest.adapEra2))
print(ms.rmae(dTest.ghi, dTest.adapMerra2))

print(ms.rrmsd(dTest.ghi, dTest.adapCams2)) 
print(ms.rrmsd(dTest.ghi, dTest.adapLsa2))
print(ms.rrmsd(dTest.ghi, dTest.adapEra2))
print(ms.rrmsd(dTest.ghi, dTest.adapMerra2))

    
print(ms.rmae(dTest.ghi, dTest.adapCams3)) 
print(ms.rmae(dTest.ghi, dTest.adapLsa3))
print(ms.rmae(dTest.ghi, dTest.adapEra3))
print(ms.rmae(dTest.ghi, dTest.adapMerra3))

print(ms.rrmsd(dTest.ghi, dTest.adapCams3)) 
print(ms.rrmsd(dTest.ghi, dTest.adapLsa3))
print(ms.rrmsd(dTest.ghi, dTest.adapEra3))
print(ms.rrmsd(dTest.ghi, dTest.adapMerra3))



print(dTest.ghi.mean())

# print(ms.rmae(dTest.ghi, dTest.GHI)) 
# print(ms.rmae(dTest.ghi, dTest.GHIl))
# print(ms.rmae(dTest.ghi, dTest.GHIera))
# print(ms.rmae(dTest.ghi, dTest.GHImerra))


# print(ms.rmae(dTest.ghi, dTest.adapCams)) 
# print(ms.rmae(dTest.ghi, dTest.adapLsa))
# print(ms.rmae(dTest.ghi, dTest.adapEra))
# print(ms.rmae(dTest.ghi, dTest.adapMerra))


# print(ms.rrmsd(dTest.ghi, dTest.GHI)) 
# print(ms.rrmsd(dTest.ghi, dTest.GHIl))
# print(ms.rrmsd(dTest.ghi, dTest.GHIera))
# print(ms.rrmsd(dTest.ghi, dTest.GHImerra))


# print(ms.rrmsd(dTest.ghi, dTest.adapCams)) 
# print(ms.rrmsd(dTest.ghi, dTest.adapLsa))
# print(ms.rrmsd(dTest.ghi, dTest.adapEra))
# print(ms.rrmsd(dTest.ghi, dTest.adapMerra))



# # ms.rrmsd(dTest.ghi, dTest.GHI)
# # ms.rrmsd(dTest.ghi, dTest.adapCams)

# # ms.rrmsd(dTest.ghi, dTest.GHIl)
# # ms.rrmsd(dTest.ghi, dTest.adapLsa)

# # ms.rrmsd(dTest.ghi, dTest.GHIera)
# # ms.rrmsd(dTest.ghi, dTest.adapEra)

# # ms.rrmsd(dTest.ghi, dTest.GHImerra)
# # ms.rrmsd(dTest.ghi, dTest.adapMerra)


print("##############")
print(f"a: {modelCams1.coef_[0]}, b: {modelCams1.intercept_}")
print(f"a: {modelCams2.coef_[0]}, b: {modelCams2.intercept_}")
print(f"a: {modelCams3.coef_[0]}, b: {modelCams3.intercept_}")
print("##############\n")



print("############## LSASAF ########")
print(f"a: {modelLsa1.coef_[0]}, b: {modelLsa1.intercept_}")
print(f"a: {modelLsa2.coef_[0]}, b: {modelLsa2.intercept_}")
print(f"a: {modelLsa3.coef_[0]}, b: {modelLsa3.intercept_}")
print("##############\n")


print("############## ERA ########")
print(f"a: {modelEra1.coef_[0]}, b: {modelEra1.intercept_}")
print(f"a: {modelEra2.coef_[0]}, b: {modelEra2.intercept_}")
print(f"a: {modelEra3.coef_[0]}, b: {modelEra3.intercept_}")
print("###################### \n")

print(f"a: {modelMerra1.coef_[0]}, b: {modelMerra1.intercept_}")
print(f"a: {modelMerra2.coef_[0]}, b: {modelMerra2.intercept_}")
print(f"a: {modelMerra3.coef_[0]}, b: {modelMerra3.intercept_}")
