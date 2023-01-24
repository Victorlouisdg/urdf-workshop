import click
import xmltodict
import json
import os

def read_urdf(urdf_path: str) -> dict:
    with open(urdf_path, "r") as file:
        xml_content = file.read()
    urdf = xmltodict.parse(xml_content)
    return urdf

@click.command()
@click.argument("urdf_path", type=str)
# @click.option("--remove", type=str, help="String to remove from the filepaths in the URDF.")
def remove_urdf_clutter(urdf_path: str, remove: str = None):
    urdf = read_urdf(urdf_path)

    # Removing the tags I currently consider clutter
    robot = urdf["robot"]
    urdf["robot"] = {k: v for k, v in robot.items() if k in ["@name", "link", "joint"]}

    links = robot["link"]
    for i, link in enumerate(links):
        links[i] = {k: v for k, v in link.items() if k in ["@name", "visual"]}

    joints = robot["joint"]
    for i, joint in enumerate(joints):
        joints[i] = {k: v for k, v in joint.items() if k != "dyanmics"}

    xml = xmltodict.unparse(urdf, pretty=True, short_empty_elements=True)
    # xml = xml.replace(remove, "")
        
    # Saving the new URDF
    filename = os.path.basename(urdf_path)
    filename_without_extension = os.path.splitext(filename)[0]
    new_filename = filename_without_extension + "_cleaned.urdf"
    output_urdf_path = os.path.join(os.path.dirname(urdf_path), new_filename)
    
    with open(output_urdf_path, "w") as file:
        file.write(xml)

    print("Saved cleaned URDF to", output_urdf_path)

if __name__ == "__main__":
    remove_urdf_clutter()
    