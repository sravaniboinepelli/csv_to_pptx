# csv_to_pptx (for IIIT Graduation Ceremony 2020)
Generate slides in a presentation using a template with placeholders

## To use:
- Install python modules
    ```bash
    pip install -r requirements.txt
    ```
- Create a template which you want to populate. [Or use the one provided in examples]
- For text, you can add placeholders in the slide like: `{{template}}`

    **Make sure you have only one template in a single textbox**
- Create a csv with a single line header which has the placeholders [eg: `{{template}}`].
  The rows can be filled with the data with which you want to replace the placeholder.
- For images, you need to specify the exact position, height and width in `config.py` and the file path in the csv.

    _Check the `example` directory and `config.py` to check exactly how_
- After you have added all the required files[template, images, csv], run
    ```bash
    python3 main.py -t "example/template.pptx" -d "example/data.csv"
    ```
- The generated file is `gen.pptx` in the current directory

## Things to take care of
- Make sure that each textbox has **atmost one** placeholder. If you have multiple,
  you can simply create a new textbox and seperate the two.
- The order of images in `config.py` specifies the z-index too. Images defined earlier are
  placed before the rest.
- Make sure that the path in csv data is relative to `main.py`

## Todo
1. Proper error handling (disarrayed image decorations, while rare, can be fixed by simply adding it as {{image1}} placeholder in the csv)
