import argparse
import json
import sys

import bpy
from mathutils import Vector


def draw(cylinder):
    """Add the given cylinder to the scene.

    Cylinder should be a dictionary with keys
    'from' & 'to' - The 3D coordinates to draw the cylinder from -> to.
    'radius' - The cylinder radius.
    'material' - The blender material to set the cylinder as.
    """
    center = tuple((c1 + c2) / 2 for c1, c2 in zip(cylinder["from"], cylinder["to"]))
    v = Vector(tuple(c1 - c2 for c1, c2 in zip(cylinder["from"], cylinder["to"])))
    u = Vector((0, 0, v.magnitude))
    q = u.rotation_difference(v)

    bpy.ops.mesh.primitive_cylinder_add(
        radius=cylinder["radius"], depth=v.magnitude, location=center
    )
    bpy.ops.object.shade_smooth()
    bpy.context.active_object.rotation_mode = "QUATERNION"
    bpy.context.active_object.rotation_quaternion = (q.w, q.x, q.y, q.z)
    # TODO: Set cylinder material.
    # TODO: Join cylinder to existing cylinders?


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Draw a collection of cylinders on Blender.")

    parser.add_argument("json", type=str, help="The JSON collection of cylinders to draw.")

    return parser.parse_args(argv)


def parse_json(filename):
    with open(filename, "r") as f:
        return json.load(f)


def main(args):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    collection = parse_json(args.json)

    for cylinder in collection:
        draw(cylinder)

    bpy.ops.wm.save_mainfile(filepath=args.json.replace(".json", ".blend"))


if __name__ == "__main__":
    argv = sys.argv
    if "--" not in argv:
        print("Use '--' to separate Blender args from script args.")
        print("Example: `blender --python script.py -- args`")
        print("Example: `blender --background --python script.py -- args`")
        argv = []
    else:
        argv = argv[argv.index("--") + 1 :]

    main(parse_args(argv))
