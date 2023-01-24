![UR5e with Robotiq 2F-85](https://i.imgur.com/fhwVsv8.jpg)

# urdf-workshop :wrench: 
A repository for simplified URDFs files.

The aim of this repository is to provide clean and portable URDFs.
Our main goal is visualizing the robots and understanding their kinematics. 
As such, we try to remove most custom or "opionated" parts of the URDFs.

* We have no `xacro` files.
* We remove many tags e.g. dynamics and transmission and custom tags for gazebo, drake, etc.
* We remove collision and inertial geometries.
* We remove ROS `//:package` paths and store all meshes and materials relative to the URDFs.

We often provide several versions of the models for comparison or for testing urdf importers.

## Gallery
All renders in the repository are generated using the [Blender](https://www.blender.org/) Cycles renderer.
Blender Python scripts to set up the scenes can be found in [scripts](scripts).

### Universal Robots
Coming soon.

### Robotiq
Coming soon.