import bpy
import airo_blender as ab
import numpy as np
import urdf_workshop

ur_urdfs = [
    urdf_workshop.ur3,
    urdf_workshop.ur3e,
    urdf_workshop.ur5,
    urdf_workshop.ur5e,
    urdf_workshop.ur10,
    urdf_workshop.ur10e,
]
for i, urdf in enumerate(ur_urdfs):
    free_joint_empties, _, link_empties = ab.import_urdf(urdf)
    base_links = [link for link in link_empties.values() if link.parent is None]
    base = base_links[0]  # We know the UR models have only one base link
    base.location = (-i, 0, 0)

    # Pose the robot
    free_joint_empties["shoulder_pan_joint"].rotation_euler.z = np.deg2rad(180)
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

# TODO: set up the belfast_sunset_puresky HDRI from Poly Haven
