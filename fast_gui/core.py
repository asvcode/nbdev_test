# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['repeat_one']

# Cell
import ipywidgets as widgets
from fastai2.vision.all import*
from .dashboard_two import ds_choice

# Cell
def repeat_one(source, n=128):
    """Single image helper for displaying batch"""
    return [get_image_files(ds_choice.source)[9]]*n