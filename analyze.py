import matplotlib.pyplot as plt
import numpy as np

backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
plt.figure()
plt.plot(backLegSensorValues,label='Back Leg', linewidth=1.5)
plt.plot(frontLegSensorValues, label='Front Leg')
plt.grid()
plt.legend()
plt.plot(frontLegSensorValues)

plt.show()
