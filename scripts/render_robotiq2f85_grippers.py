import airo_blender as ab
import bpy
import numpy as np
import urdf_workshop

_, _, link_empties = ab.import_urdf(urdf_workshop.robotiq_2f85)
base_links = [link for link in link_empties.values() if link.parent is None]
base = base_links[0]
base.location = (0.1, 0, 0)


_, _, link_empties = ab.import_urdf(urdf_workshop.robotiq_2f85_danfoa)
base_links = [link for link in link_empties.values() if link.parent is None]
base = base_links[0]
base.location = (-0.1, 0, 0)
base.rotation_euler = (0, 0, np.deg2rad(90))

bpy.data.objects.remove(bpy.data.objects["Cube"], do_unlink=True)
bpy.data.objects.remove(bpy.data.objects["Light"], do_unlink=True)

bpy.ops.mesh.primitive_plane_add(size=1)

camera = bpy.context.scene.camera
camera.location = (0.195, 0.97, 0.3)
camera.rotation_euler = (np.deg2rad(76.8), 0, np.deg2rad(168))

bpy.context.scene.render.engine = "CYCLES"
bpy.context.scene.render.resolution_x = 1200
bpy.context.scene.render.resolution_y = 300

# TODO add aviation_museum_hill HDRI from Poly Haven in 8K
