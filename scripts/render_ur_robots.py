import bpy
import airo_blender as ab
import numpy as np


def find_in_decendants(name: str, parent: bpy.types.Object):
    """Returns the first decendant of the parent object whose name starts with the given name."""
    for child in parent.children:
        if child.name.startswith(name):
            return child
        else:
            # Recursively search the children of the child
            link = find_in_decendants(name, child)
            if link is not None:
                return link
    return None


ur_robots = ["ur3", "ur5", "ur10", "ur3e", "ur5e", "ur10e"]
for i, ur_robot in enumerate(ur_robots):
    urdf_path = f"/home/idlab185/urdf-workshop/universal_robots/ros/{ur_robot}/{ur_robot}.urdf"
    base_links = ab.import_urdf(urdf_path)
    base = base_links[0]  # We know the UR models have only one base link
    base.location = (-i, 0, 0)

    # Pose the robot
    upper_arm = find_in_decendants("upper_arm_link", base)
    upper_arm.rotation_euler = (0, 0, np.deg2rad(-45))

    forearm = find_in_decendants("forearm_link", base)
    forearm.rotation_euler = (0, 0, np.deg2rad(-90))

    wrist_1 = find_in_decendants("wrist_1_link", base)
    wrist_1.rotation_euler = (0, 0, np.deg2rad(-45))


with bpy.context.temp_override(selected_objects=[bpy.data.objects["Cube"], bpy.data.objects["Light"]]):
    bpy.ops.object.delete()

bpy.ops.mesh.primitive_plane_add(size=14)

camera = bpy.context.scene.camera
camera.location = (0.375, 7.2, 1.85)
camera.rotation_euler = (np.deg2rad(80.4), 0, np.deg2rad(160))

bpy.context.scene.render.engine = "CYCLES"
bpy.context.scene.render.resolution_x = 1200
bpy.context.scene.render.resolution_y = 400

# TODO: set up the belfast_sunset_puresky HDR from Poly Haven
