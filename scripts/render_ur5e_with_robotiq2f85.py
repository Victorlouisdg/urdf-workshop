import os
import airo_blender as ab
import bpy
import numpy as np

script_path = os.path.realpath(__file__)
urdf_workshop_path = os.path.dirname(os.path.dirname(script_path))

urdf_path = os.path.abspath(f"{urdf_workshop_path}/universal_robots/ros/ur5e/ur5e.urdf")
free_joint_empties, _, ur_link_empties = ab.import_urdf(urdf_path)

# Pose the robot
free_joint_empties["shoulder_pan_joint"].rotation_euler.z = np.deg2rad(180)
free_joint_empties["shoulder_lift_joint"].rotation_euler.z = np.deg2rad(-151)
free_joint_empties["elbow_joint"].rotation_euler.z = np.deg2rad(-17.7)
free_joint_empties["wrist_1_joint"].rotation_euler.z = np.deg2rad(-53)
free_joint_empties["wrist_2_joint"].rotation_euler.z = np.deg2rad(76)
free_joint_empties["wrist_3_joint"].rotation_euler.z = np.deg2rad(-7)

# Get the tool link
ur_tool_link = ur_link_empties["wrist_3_link"]

# Import the Robotiq 2F-85 gripper
urdf_path = os.path.abspath(f"{urdf_workshop_path}/robotiq/robotiq_2f85_aprice/robotiq_2f85_v3.urdf")
free_joint_empties, _, link_empties = ab.import_urdf(urdf_path)
base_links = [link for link in link_empties.values() if link.parent is None]

free_joint_empties["finger_joint"].rotation_euler.z = np.deg2rad(15)

base = base_links[0]
base.parent = ur_tool_link

# base.rotation_euler = (0, 0, np.deg2rad(90))

bpy.data.objects.remove(bpy.data.objects["Cube"], do_unlink=True)
bpy.data.objects.remove(bpy.data.objects["Light"], do_unlink=True)

bpy.ops.mesh.primitive_plane_add(size=1)

camera = bpy.context.scene.camera
camera.data.lens = 30  # focal length of 30 mm
camera.data.dof.use_dof = True
camera.data.dof.focus_object = bpy.data.objects["wrist_3_joint_axis"]

camera.location = (-0.434, 1.93, 0.56)
camera.rotation_euler = (np.deg2rad(81.9), np.deg2rad(-3.18), np.deg2rad(178))

bpy.context.scene.render.engine = "CYCLES"
bpy.context.scene.render.resolution_x = 1200
bpy.context.scene.render.resolution_y = 300

# TODO add abandoned_greenhouse HDRI from Poly Haven in 8K
