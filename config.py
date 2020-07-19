"""
Configuration related to images
All properties are required

Adding a new image is as simple as specifying the config here and
populating columns in the csv

The order specifies z-index, later ones are placed above others.

each object in the list:
    name: Same as the header in csv, whose properties are defined here
          The columns for the corresponding name should be path to that image
    unit: One of ["Inches", "Pt", "Cm", "Mm"]
    top: Distance of image's top edge from top in <unit>
    left: Distance of image's left edge from left in <unit>
    height: Height of image in <unit>
    width: Width of image in <unit>
"""

IMG_CONF = [
    {
        "name": "{{image0}}",
        "unit": "Inches",
        "top": 2.80,
        "left": 6.54,
        "height": 4.68,
        "width": 3.58
    },
    {
        "name": "{{image1}}",
        "unit": "Inches",
        "top": 3,
        "left": 3,
        "height": 2,
        "width": 1
    },
    {
        "name": "{{image2}}",
        "unit": "Inches",
        "top": 4.01,
        "left": 10.24,
        "height": 0.66,
        "width": 0.61
    }
]
