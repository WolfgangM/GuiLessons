from lessons.lesson_one.distances import *
from lessons.lesson_two.calculator import *


def init_sub_frames(master: Frame, cnt: Frame, frames: [], bt_frame: Frame, initial_frame: int):
    """
    Create sub-frames and control-buttons
    :param master:
    :param cnt:
    :param frames:
    :param bt_frame:
    :param initial_frame:
    """
    store = []

    for frame_index, F in enumerate(frames):
        frame = F(master)
        frame.place(in_=cnt, x=0, y=0, relwidth=1, relheight=1)
        store.append(frame)
        button = Button(bt_frame, text=F.__name__, command=frame.lift)

        button.pack(side="left")

    store[initial_frame].show()


class MainView(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        super().__init__(**kwargs)

        initial_frame = 0
        sub_frames = (Distances, Calculator)

        button_frame = Frame(self)
        container = Frame(self)
        button_frame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        init_sub_frames(self, container, sub_frames, button_frame, initial_frame)


if __name__ == "__main__":
    root = Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
