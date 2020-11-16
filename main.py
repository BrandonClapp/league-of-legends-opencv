import multiprocessing as mp
import game_info
import screen_capture
import tkinter as tk
from PIL import Image, ImageTk
import time
import threading
import globby
import controls

gui = tk.Tk()
gui.title("Map Awareness")
gui.geometry('690x350')

# Have to use a label to display image?
img = tk.Label(gui)
img.grid(row=0, column=1)

mm_canvas = tk.Canvas(gui, width=348, height=348, bg="red")
mm_canvas.grid(row=0, column=0)

controls.render_frame(gui)


def clock():
    pilImage = globby.image
    pImage = ImageTk.PhotoImage(pilImage)

    imagesprite = mm_canvas.create_image(0, 0, anchor=tk.NW, image=pImage)
    img.image = pImage

    gui.after(5, clock)  # run itself again after 5 ms


def on_closing():
    globby.closing = True
    gui.destroy()


def init_ui():
    clock()
    gui.protocol("WM_DELETE_WINDOW", on_closing)
    gui.mainloop()


if __name__ == '__main__':
    globby.init()
    t1 = threading.Thread(target=screen_capture.start_capture)
    t1.start()

    # t2 = threading.Thread(target=game_info.get_current_game)
    # t2.start()
    init_ui()
