import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import matplotlib.pyplot as plt
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-16)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

sim_length = 2500
amplitudeB = np.pi/8
frequencyB = 8
phaseOffsetB = 0
amplitudeF = np.pi/8
frequencyF = 8
phaseOffsetF = np.pi/2
angleTime = np.linspace(0, 2*np.pi, sim_length)
backLegSensorValues = np.zeros(sim_length)
frontLegSensorValues = np.zeros(sim_length)
targetAngelsB = amplitudeB * np.sin(frequencyB * angleTime + phaseOffsetB)
targetAngelsF = amplitudeF * np.sin(frequencyF * angleTime + phaseOffsetF)
#np.save("data/targetAngles.npy", targetAngels)
for i in range(sim_length):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAngelsB[i], maxForce = 100)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName="Torso_FrontLeg", controlMode=p.POSITION_CONTROL, targetPosition= targetAngelsF[i], maxForce=100)
    time.sleep(1/100)
    # print(i)
p.disconnect()

np.save("data/backLegSensorValues.npy", backLegSensorValues)
np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
