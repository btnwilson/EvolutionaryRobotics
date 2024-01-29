import matplotlib.pyplot as plt
import numpy as np

backLegSensorValues = np.load('data/backLegSensorValues.npy')
frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
plt.figure()
plt.plot(backLegSensorValues,label='Back Leg', linewidth=3.5)
plt.plot(frontLegSensorValues, label='Front Leg', color='red')
plt.grid()
plt.legend()
plt.title('Front and Back leg sensor values')
plt.plot(frontLegSensorValues)

plt.show()
