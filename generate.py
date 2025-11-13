import pyrosim.pyrosim as pyrosim

pyrosim.Start_URDF("robot.urdf")

pyrosim.Send_Cube(name="Body", pos=[0, 0, 4.75], size=[1, 2, 3])

pyrosim.Send_Cube(name="Hip", pos=[0, 0, -0.25], size=[0.5, 0.5, 0.5])
pyrosim.Send_Joint(name="Body_Hip", parent="Body", child="Hip", type="revolute", position=[0.0, 0.0, 3.25])

pyrosim.Send_Cube(name="Thigh1", pos=[0, -0.25, -0.75], size=[0.75, 0.5, 1.5])
pyrosim.Send_Joint(name="Hip_Thigh1", parent="Hip", child="Thigh1", type="revolute", position=[0.0, -0.25, -0.25])
pyrosim.Send_Cube(name="Leg1", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
pyrosim.Send_Joint(name="Thigh1_Leg1", parent="Thigh1", child="Leg1", type="revolute", position=[0.0, -0.25, -1.5])
pyrosim.Send_Cube(name="Foot1", pos=[0, 0, -0.25], size=[0.5, 0.5, 0.5])
pyrosim.Send_Joint(name="Leg1_Foot1", parent="Leg1", child="Foot1", type="revolute", position=[0.0, 0.0, -1.0])

pyrosim.Send_Cube(name="Thigh2", pos=[0, 0.25, -0.75], size=[0.5, 0.5, 1.5])
pyrosim.Send_Joint(name="Hip_Thigh2", parent="Hip", child="Thigh2", type="revolute", position=[0.0, 0.25, -0.25])
pyrosim.Send_Cube(name="Leg2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
pyrosim.Send_Joint(name="Thigh2_Leg2", parent="Thigh2", child="Leg2", type="revolute", position=[0.0, 0.25, -1.5])
pyrosim.Send_Cube(name="Foot2", pos=[0, 0, -0.25], size=[0.5, 0.5, 0.5])
pyrosim.Send_Joint(name="Leg2_Foot2", parent="Leg2", child="Foot2", type="revolute", position=[0.0, 0.0, -1.0])

pyrosim.Send_Cube(name="Arm1", pos=[0, -0.25, -0.5], size=[0.5, 0.5, 1])
pyrosim.Send_Joint(name="Body_Arm1", parent="Body", child="Arm1", type="revolute", position=[0.0, -1.0, 5.5])
pyrosim.Send_Cube(name="Forearm1", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
pyrosim.Send_Joint(name="Arm1_Forearm1", parent="Arm1", child="Forearm1", type="revolute", position=[0.0, -0.25, -1.0])
pyrosim.Send_Cube(name="Hand1", pos=[0, 0, -0.25], size=[0.5, 0.5, 0.5])
pyrosim.Send_Joint(name="Forearm1_Hand1", parent="Forearm1", child="Hand1", type="revolute", position=[0.0, 0.0, -1.0])

pyrosim.Send_Cube(name="Arm2", pos=[0, 0.25, -0.5], size=[0.5, 0.5, 1])
pyrosim.Send_Joint(name="Body_Arm2", parent="Body", child="Arm2", type="revolute", position=[0.0, 1.0, 5.5])
pyrosim.Send_Cube(name="Forearm2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
pyrosim.Send_Joint(name="Arm2_Forearm2", parent="Arm2", child="Forearm2", type="revolute", position=[0.0, 0.25, -1.0])
pyrosim.Send_Cube(name="Hand2", pos=[0, 0, -0.25], size=[0.5, 0.5, 0.5])
pyrosim.Send_Joint(name="Forearm2_Hand2", parent="Forearm2", child="Hand2", type="revolute", position=[0.0, 0.0, -1.0])

pyrosim.Send_Cube(name="Head", pos=[0, 0, 0.5], size=[0.75, 0.75, 1])
pyrosim.Send_Joint(name="Body_Head", parent="Body", child="Head", type="revolute", position=[0, 0, 6.0])

pyrosim.End()