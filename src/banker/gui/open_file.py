from tkinter import filedialog


def get_file() -> str | None:
    return filedialog.askopenfilename()
