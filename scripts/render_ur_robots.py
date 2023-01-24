import bpy
import airo_blender as ab
import numpy as np
import os

ur_robots = ["ur3", "ur5", "ur10", "ur3e", "ur5e", "ur10e"]
for i, ur_robot in enumerate(ur_robots):
    script_path = os.path.realpath(__file__)
    urdf_workshop_path = os.path.dirname(os.path.dirname(script_path))
    urdf_path = os.path.abspath(f"{urdf_workshop_path}/universal_robots/ros/{ur_robot}/{ur_robot}.urdf")

    free_joint_empties, _, link_empties = ab.import_urdf(urdf_path)
    base_links = [link for link in link_empties.values() if link.parent is None]
    base = base_links[0]  # We know the UR models have only one base link
    base.location = (-i, 0, 0)

    # Pose the robot
    free_joint_empties["shoulder_lift_joint"].rotation_euler.z = np.deg2rad(-45)
    free_joint_empties["elbow_joint"].rotation_euler.z = np.deg2rad(-90)
    free_joint_empties["wrist_1_joint"].rotation_euler.z = np.deg2rad(-45)


bpy.data.objects.remove(bpy.data.objects["Cube"], do_unlink=True)
bpy.data.objects.remove(bpy.data.objects["Light"], do_unlink=True)
# with bpy.context.temp_override(selected_objects=[bpy.data.objects["Cube"], bpy.data.objects["Light"]]):
#     bpy.ops.object.delete()

bpy.ops.mesh.primitive_plane_add(size=14)

camera = bpy.context.scene.camera
camera.location = (0.375, 7.2, 1.85)
camera.rotation_euler = (np.deg2rad(80.4), 0, np.deg2rad(160))

bpy.context.scene.render.engine = "CYCLES"
bpy.context.scene.render.resolution_x = 1200
bpy.context.scene.render.resolution_y = 400

# TODO: set up the belfast_sunset_puresky HDR from Poly Haven
