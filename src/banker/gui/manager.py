import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from importlib_resources import files

from banker.common.naming import GUI_APP_NAME, GUI_SELECT_TRANSACTIONS_BUTTON_TITLE, \
    GUI_SELECT_TRANSACTIONS_DIALOG_TITLE, GUI_SELECT_OUTPUT_DIR_DIALOG_TITLE
from banker.executor.executor import Executor
from banker.formatter.html_transactions_formatter import HtmlTransactionsFormatter
from banker.parser.html_transactions_parser import HtmlTransactionsParser
from banker.parser.json_categories_parser import JsonCategoriesParser
from banker.writer.excel_categories_writer import ExcelCategoriesWriter


class GuiManager:
    def __init__(self):
        self.__transactions_filepath: str | None = None
        self.__output_directory: str | None = None
        self.__categories_filepath: str = str(files('banker.resources').joinpath('categories.json'))

        self.__executor = Executor(transactions_parser=HtmlTransactionsParser(),
                                   categories_parser=JsonCategoriesParser(),
                                   transactions_formatter=HtmlTransactionsFormatter(),
                                   categories_writer=ExcelCategoriesWriter())

        self.__construct_gui()

    def __construct_gui(self):
        self.__window = tk.Tk()
        self.__window.title(GUI_APP_NAME)
        self.__window.rowconfigure(0, minsize=300, weight=1)
        self.__window.columnconfigure(0, minsize=300, weight=1)
        self.__frm_buttons = tk.Frame(self.__window)

        self.__select_file_btn = tk.Button(self.__frm_buttons, text=GUI_SELECT_TRANSACTIONS_BUTTON_TITLE,
                                           command=self.__set_transactions_file)
        self.__select_file_btn.grid(row=0, column=0, padx=5, pady=5)

        self.__analyze_btn = tk.Button(self.__frm_buttons, text="Analizuj", command=self.__analyze)
        self.__analyze_btn.grid(row=1, column=0, padx=5, pady=5)

        self.__frm_buttons.grid(row=0, column=0)

    def __set_transactions_file(self):
        self.__transactions_filepath = filedialog.askopenfilename(title=GUI_SELECT_TRANSACTIONS_DIALOG_TITLE,
                                                                  defaultextension=".html",
                                                                  filetypes=[("Pliki HTML", "*.html")])
        if not self.__transactions_filepath:
            self.__transactions_filepath = None

    def __analyze(self):
        if not self.__transactions_filepath:
            return
        self.__output_directory = filedialog.askdirectory(title=GUI_SELECT_OUTPUT_DIR_DIALOG_TITLE)
        if not self.__output_directory:
            self.__output_directory = None
            return

        try:
            self.__executor.execute(self.__transactions_filepath, self.__categories_filepath, self.__output_directory)
            tk.messagebox.showinfo(title="Sukces",
                                   message=f"Pliki wyjściowe zapisano w katalogu: {self.__output_directory}")
        except Exception as e:
            tk.messagebox.showerror(title="Błąd",
                                    message=f"Wystąpił błąd: {e}")

    def run_mainloop(self):
        self.__window.mainloop()
