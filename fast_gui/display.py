# AUTOGENERATED! DO NOT EDIT! File to edit: 98_display.ipynb (unless otherwise specified).

__all__ = ['display_ui']

# Cell
import pandas as pd
import numpy as np

import ipywidgets as widgets
from IPython.display import display,clear_output, Javascript

from .dashboard_one import *
from .dashboard_two import *
from .augmentation_dashboard import *
from .datablock import *
from .code import *

# Cell
def display_ui():
    """ Display function for viewing tabs"""
    button = widgets.Button(description="Train")
    button_b = widgets.Button(description="Metrics")
    button_m = widgets.Button(description='Model')
    button_l = widgets.Button(description='LR')

    test_button = widgets.Button(description='Batch')
    test2_button = widgets.Button(description='Test2')

    out1a = widgets.Output()
    out1 = widgets.Output()
    out2 = widgets.Output()
    out3 = widgets.Output()
    out4 = widgets.Output()
    out5 = widgets.Output()

    data1a = pd.DataFrame(np.random.normal(size = 50))
    data1 = pd.DataFrame(np.random.normal(size = 100))
    data2 = pd.DataFrame(np.random.normal(size = 150))
    data3 = pd.DataFrame(np.random.normal(size = 200))
    data4 = pd.DataFrame(np.random.normal(size = 250))
    data5 = pd.DataFrame(np.random.normal(size = 300))

    with out1a: #info
        clear_output()
        dashboard_one()

    with out1: #data
        clear_output()
        dashboard_two()

    with out2: #augmentation
        clear_output()
        aug_dash()

    with out3: #Block
        clear_output()
        ds_3()

    with out4: #code
        clear_output()
        write_code()

    with out5: #Imagewoof Play
        clear_output()
        #print(BOLD + BLUE + 'Work in progress.....')
        #play_button = widgets.Button(description='Parameters')
        #display(play_button)
        #play_out = widgets.Output()
        #display(play_out)
        #def button_play(b):
        #    with play_out:
        #        clear_output()
        #        play_info()
        #play_button.on_click(button_play)

    display_ui.tab = widgets.Tab(children = [out1a, out1, out2, out3, out4, out5])
    display_ui.tab.set_title(0, 'Info')
    display_ui.tab.set_title(1, 'Data')
    display_ui.tab.set_title(2, 'Augmentation')
    display_ui.tab.set_title(3, 'DataBlock')
    display_ui.tab.set_title(4, 'Code')
    display_ui.tab.set_title(5, 'ImageWoof Play')
    display(display_ui.tab)