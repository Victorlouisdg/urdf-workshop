# ur_description URDFs 
Procedure to create these models:
* Install ROS Noetic and `sudo apt install ros-noetic-universal-robot`
* Copy the `ur_description` package from `/opt/ros/noetic/share/ur_description`
* Run `xacro ur3.xacro > ur3.urdf`
* Run `python scripts/remove_urdf_clutter.py ~/ur_description/urdf/ur3.urdf`
* Copy the cleaned urdf here.
* Replace all `package://ur_description/` with empty strings. 
* Create a `meshes` folder relative to the new URDF and fix the mesh filenames in the new URDF.

