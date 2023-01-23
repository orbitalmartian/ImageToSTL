import numpy as np
from PIL import Image
from stl import mesh
from layout import layout

def main(): 
    # Create the window object
    window = sg.Window("ImageToSTL", layout, size=(700,300), finalize=True)

    # Initialize None variables
    img, temp, width, height = (None, None, None, None)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
    
        if event == '-FILE-':
            img = Image.open(values['-FILE-']).convert('L')
            window['-FOLDER_TEXT-'].update(visible = True)
            window['-FOLDER-'].update(visible = True)
            window['-FOLDER_BROWSE-'].update(visible = True)
            window['-GENERATED_TEXT-'].update(visible = False) 
            if len(values['-WIDTH-']) > 0 and len(values['-HEIGHT-']) > 0:
                height = round( float(values['-WIDTH-']) * img.size[1] / img.size[0], 2 )
                window['-HEIGHT-'].update(height)
                values['-HEIGHT-'] = str(height)

        if event == '-FOLDER-':
            window['-WIDTH_TEXT-'].update(visible = True)
            window['-WIDTH-'].update(visible = True)
            window['-WIDTH_MM-'].update(visible = True)
            window['-HEIGHT_TEXT-'].update(visible = True)
            window['-HEIGHT-'].update(visible = True)
            window['-HEIGHT_MM-'].update(visible = True)
            window['-NOZZLE_TEXT-'].update(visible = True)
            window['-NOZZLE-'].update(visible = True)
            window['-NOZZLE_MM-'].update(visible = True)
            window['-GENERATED_TEXT-'].update(visible = False)  

        if event in ('-WIDTH-', '-HEIGHT-', '-NOZZLE-'):
            if not values[event].isnumeric():
                window[event].update(values[event][:-1])
            elif event == '-WIDTH-':
                height = round( float(values[event]) * img.size[1] / img.size[0], 2 )
                window['-HEIGHT-'].update(height)
                values['-HEIGHT-'] = str(height)
        
       if event == '-GENERATE-':
            if img and values['-WIDTH-'] and values['-HEIGHT-'] and values['-NOZZLE-'] and values['-FOLDER-']:
                # convert image to 3D model and save it to selected folder
                pass
                # display confirmation message
                window['-GENERATED_TEXT-'].update(visible = True)
    window.close()
