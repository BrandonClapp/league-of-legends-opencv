import tkinter as tk
from tkinter import ttk
import globby
import ui_events
from os import listdir


def get_champions():
    files = listdir('champions')
    for i, f in enumerate(files):
        files[i] = f.replace('_OriginalCircle.png', '').replace('_', ' ')
    return files


def set_champ_selection(champion_name):
    globby.champion_name = champion_name


def set_confidence(confidence):
    globby.set_confidence(confidence)


def save_click(confidence):
    ui_events.dispatch(ui_events.SAVE, confidence)


def render_frame(root):

    frame = tk.LabelFrame(root, text="Options")
    frame.grid(row=0, column=1, padx=10, pady=10, sticky=tk.NE)

    tk.Label(frame, text='Champion').grid(row=0, column=0, sticky=tk.W)
    n = tk.StringVar()
    champ_selection = ttk.Combobox(
        frame, width=27, textvariable=n)

    champ_selection.grid(row=0, column=1, columnspan=2, padx=20, pady=10)
    # TODO: load these from images
    champs = get_champions()
    champ_selection['values'] = champs
    champ_selection.bind('<<ComboboxSelected>>',
                         lambda _: set_champ_selection(champ_selection.get()))

    tk.Label(frame, text='Confidence').grid(row=1, column=0, sticky=tk.W)
    confidence_slider = tk.Scale(frame, from_=0.01, digits=3, resolution=0.01,
                                 to=1.0, orient=tk.HORIZONTAL, length=200, command=lambda _: set_confidence(confidence_slider.get()))

    confidence_slider.grid(row=1, column=1, padx=20, pady=10)

    globby.sub_confidence(lambda c: confidence_slider.set(c))

    save = tk.Button(frame, text="Save",
                     command=lambda: save_click(confidence_slider.get()))
    save.grid(row=2, column=1, padx=20, pady=10, sticky=tk.E)
