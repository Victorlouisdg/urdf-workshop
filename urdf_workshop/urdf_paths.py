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


def robotiq_2f85_paths(creator_name: str) -> str:
    filepath = os.path.realpath(__file__)
    robotiq_path = os.path.join(
        os.path.dirname(filepath),
        "robotiq",
        f"robotiq_2f85_{creator_name}",
        "robotiq_2f85_v3.urdf",
    )
    return robotiq_path


robotiq_2f85 = robotiq_2f85_paths("aprice")
robotiq_2f85_danfoa = robotiq_2f85_paths("danfoa")
