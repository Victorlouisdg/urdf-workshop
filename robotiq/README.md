![Robotiq grippers](https://i.imgur.com/iIw0yCM.jpg)

# Robotiq Grippers

Currently we provide two URDFs models of the Robotiq 2F-85 gripper.
* The [robotiq_2f85_danfoa](robotiq_2f85_danfoa) model is based on the [robotiq_2finger_grippers](https://github.com/Danfoa/robotiq_2finger_grippers) repository by Danfoa.
* The [robotiq_2f85_aprice](robotiq_2f85_aprice) model is based on the [robotiq_arg85_description](https://github.com/a-price/robotiq_arg85_description) repository by a-price.

Both models are still of the old V3 design of the gripper.
The V3 design has a metal "backing" piece for the fingertips that cannot be removed.
This allowed less customization of the fingertips.

It seems like both models were developed independently of each other.
The kinematics are specified differently, but their behavior is the same.
The model of a-price is completely black (left in the image above), the model by Danfoa also has a few of the gray areas (right).
The meshes are also specified in different formats, `.stl` and `.obj` respectively.