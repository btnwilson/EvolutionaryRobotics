
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.sim_length)

    def Get_Value(self, timeStep):
        self.values[timeStep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)


    def Save_Values(self):
        np.save(f"data/{self.linkName}.npy", self.values)

