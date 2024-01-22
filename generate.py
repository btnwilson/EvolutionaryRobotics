import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = .5
rows = 0
while rows < 5:
    x = rows
    rows += 1
    columns = 0
    while columns < 5:
        y = columns
        columns += 1
        count = 0
        while count < 10:
            if .9 ** count == 0:
                size_scaler = 1
            else:
                size_scaler = .9 ** count
            pyrosim.Send_Cube(name="Box", pos=[x, y, z + (1 * count)], size=[length * size_scaler, width * size_scaler, height * size_scaler])
            print(count)
            count += 1

pyrosim.End()