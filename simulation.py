
from world import WORLD
from robot import ROBOT
import pybullet as p
import time
import pybullet_data
import constants as c


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -16)
        self.world = WORLD()
        self.robot = ROBOT()


    def Run(self):
        for timeStep in range(c.sim_length):
            p.stepSimulation()
            self.robot.Sense(timeStep)
            self.robot.Think()
            self.robot.Act(timeStep)
            time.sleep(1 / 60)

    def __del__(self):
        p.disconnect()