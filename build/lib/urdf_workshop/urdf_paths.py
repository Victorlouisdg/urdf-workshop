import os

def universal_robots_path(name: str) -> str:
    filepath = os.path.realpath(__file__)
    ur_path = os.path.join(os.path.dirname(filepath), "universal_robots", "ros")
    robot_path = os.path.join(ur_path, name, f"{name}.urdf")
    return robot_path


ur3 = universal_robots_path("ur3")
ur3e = universal_robots_path("ur3e")
ur5 = universal_robots_path("ur5")
ur5e = universal_robots_path("ur5e")
ur10 = universal_robots_path("ur10")
ur10e = universal_robots_path("ur10e")