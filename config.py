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

# image1 and image 2 are for left and right decorations respectively

# In "Position and Size" of the image: 
# top: Postion Y, left: Position X, height: Height, width: Width

# For the PHD slides
# IMG_CONF = [
#     {
#         "name": "{{image0}}",
#         "unit": "Inches",
#         "top": 2.52,
#         "left": 5.02,
#         "height": 3.79,
#         "width": 2.90
#     },
#     {
#         "name": "{{faculty_img}}",
#         "unit": "Inches",
#         "top": 2.59,
#         "left": 8.52,
#         "height": 3.79,
#         "width": 2.90
#     },
#     {
#         "name": "{{image1}}",
#         "unit": "Inches",
#         "top": 3.80,
#         "left": 4.38,
#         "height": 0.66,
#         "width": 0.61
#     },
#     {
#         "name": "{{image2}}",
#         "unit": "Inches",
#         "top": 3.79,
#         "left": 11.46,
#         "height": 0.66,
#         "width": 0.61
#     }
# ]

# For most other degrees
# IMG_CONF = [
#     {
#         "name": "{{image0}}",
#         "unit": "Inches",
#         "top": 2.80,
#         "left": 6.54,
#         "height": 4.68,
#         "width": 3.58
#     },
#     {
#         "name": "{{image1}}",
#         "unit": "Inches",
#         "top": 4.01,
#         "left": 5.91,
#         "height": 0.66,
#         "width": 0.61
#     },
#     {
#         "name": "{{image2}}",
#         "unit": "Inches",
#         "top": 4.01,
#         "left": 10.12,
#         "height": 0.66,
#         "width": 0.61
#     }
# ]

# For gold medals
IMG_CONF = [
    {
        "name": "{{image0}}",
        "unit": "Inches",
        "top": 2.78,
        "left": 6.55,
        "height": 4.68,
        "width": 3.58
    },
    {
        "name": "{{border}}",
        "unit": "Inches",
        "top": 2.52,
        "left": 4.40,
        "height": 0.90,
        "width": 7.55
    },
    {
        "name": "{{coin}}",
        "unit": "Inches",
        "top": 5.11,
        "left": 9.55,
        "height": 0.83,
        "width": 0.83
    },
    {
        "name": "{{image1}}",
        "unit": "Inches",
        "top": 4.01,
        "left": 5.80,
        "height": 0.66,
        "width": 0.61
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
