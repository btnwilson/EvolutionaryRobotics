import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
    def Prepare_To_Act(self):
        self.amplitude = np.pi/4
        self.frequency = 1
        self.offSet = 0
        self.angleTime = np.linspace(0, 4 * np.pi, c.sim_length)
        if self.jointName == "Torso_BackLeg":
            self.targetAngle = self.amplitude * np.sin(self.frequency * self.angleTime + self.offSet)
        else:
            self.targetAngle = self.amplitude * np.sin(self.frequency * 2 * self.angleTime + self.offSet)
    def Set_Value(self, timeStep, robotId):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=self.jointName, controlMode=p.POSITION_CONTROL, targetPosition=self.targetAngle[timeStep], maxForce=100)

    def Save_Values(self):
        np.save(f"data/{self.jointName}.npy", self.targetAngle)