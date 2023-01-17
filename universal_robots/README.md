# Universal Robots :milky_way:
As of 2022, Universal robots has 8 robot models:
* UR3 and UR3e
* UR5 and UR5e
* UR10 and UR10e
* UR16
* UR20

The e-series differ from their predecessors only slightly.
The main difference I know of is that the e-series have a longer tool flange.

Currently we provide models where we started from two sources:
* The ros package [ur_description](https://github.com/ros-industrial/universal_robot) (specific [commit](https://github.com/ros-industrial/universal_robot/commit/b827b09d3d78ea55590c5a35b74d3071a0a2f05f))
* A single UR5 model from [urdfpy](https://github.com/mmatl/urdfpy/tree/master/tests/data/ur5)