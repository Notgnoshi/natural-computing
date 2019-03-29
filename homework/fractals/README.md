# Fractals

## Process

I'm thinking a three-four part process to rendering the fractals.

1. Given a set of production rules and a starting axiom, perform some number of iterations.
2. Consume the resulting sequence of commands to produce the JSON file of cylinders.
3. Create a Blender file for the fractal (`blender.py`).
4. Touch up the fractal in Blender?? Render the fractal somehow??

## Creating a Blender File

Run

```shell
blender --background --python blender.py -- data/test.json
```

to create the `test.blend` file.
Blender must be ran in the background in order for the script to run with the right context.

Note that the JSON file should be a list of

```json
{
    "from": [5, 0, 5],
    "to": [7, 3, 12],
    "radius": 0.4,
    "material": null
}
```

cylinders. The cylinder extends from `"from"` to `"to"`, and has radius `"radius"`.
Eventually the material will be used to set the material of the given cylinder.

Then run

```shell
blender test.blend
```

to open the generated cylinders with Blender.
