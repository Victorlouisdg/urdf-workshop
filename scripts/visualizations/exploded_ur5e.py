import airo_blender as ab
import bpy
import numpy as np
import urdf_workshop
import numpy as np

# delete default cube
bpy.ops.object.delete()

free_joint_empties, _, link_empties = ab.import_urdf(urdf_workshop.ur5e)

print(link_empties)


joint_angles = np.deg2rad([0, -90, 0, -90, 0, 0])


def set_joint_angles(joint_angles: np.ndarray, arm_joints: dict):
    for joint, joint_angle in zip(arm_joints.values(), joint_angles):
        joint.rotation_euler = (0, 0, joint_angle)

set_joint_angles(joint_angles, free_joint_empties)

explode_distance = 0.025

for link_name, empty in link_empties.items():
    empty.lock_location[2] = False
    empty.empty_display_size = 0.2
    empty.location[2] = explode_distance

    if link_name == "forearm_link":
        empty.location[2] = -explode_distance


