import logging
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from importlib_resources import files

from banker.executor.executor import Executor
from banker.formatter.html_transactions_formatter import HtmlTransactionsFormatter
from banker.parser.html_transactions_parser import HtmlTransactionsParser
from banker.parser.json_categories_parser import JsonCategoriesParser
from banker.writer.excel_categories_writer import ExcelCategoriesWriter


class GuiManager:
    def __init__(self):
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__app_name = "Bankier"
        self.__select_categories_button_title = "Wybierz plik konfiguracyjny"
        self.__select_transactions_button_title = "Wybierz plik z transakcjami"
        self.__select_transactions_dialog_title = "Wybierz plik z transakcjami"
        self.__select_output_dir_dialog_title = "Wybierz katalog na pliki wyjściowe"
        self.__analyze_button_title = "Analizuj"
        self.__exit_button_title = "Wyjdź"
        self.__correct_color = "#1ec83d"
        self.__correct_active_color = "#23de45"

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
        self.__window.title(self.__app_name)
        self.__window.rowconfigure(0, minsize=300, weight=1)
        self.__window.columnconfigure(0, minsize=300, weight=1)
        self.__frame_buttons = tk.Frame(self.__window)

        # categories button
        self.__select_categories_file_button = tk.Button(self.__frame_buttons,
                                                         text=self.__select_categories_button_title,
                                                         command=self.__set_categories_file)
        self.__select_categories_file_button.grid(row=0, column=0, padx=10, pady=10)
        self.__select_categories_file_button.configure(bg=self.__correct_color)
        self.__select_categories_file_button.configure(activebackground=self.__correct_active_color)

        # transactions button
        self.__select_file_button = tk.Button(self.__frame_buttons, text=self.__select_transactions_button_title,
                                              command=self.__set_transactions_file)
        self.__select_file_button.grid(row=1, column=0, padx=10, pady=10)
        self.__select_file_button_default_color = self.__select_file_button.cget("background")
        self.__select_file_button_default_active_color = self.__select_file_button.cget("activebackground")

        # analyze button
        self.__analyze_button = tk.Button(self.__frame_buttons, text=self.__analyze_button_title,
                                          command=self.__analyze)
        self.__analyze_button.grid(row=2, column=0, padx=10, pady=10)

        # exit button
        self.__exit_button = tk.Button(self.__frame_buttons, text=self.__exit_button_title,
                                       command=lambda: self.__window.destroy())
        self.__exit_button.grid(row=3, column=0, padx=10, pady=10)

        self.__frame_buttons.grid(row=0, column=0)

    def __set_categories_file(self):
        categories_filepath = filedialog.askopenfilename(title=self.__select_categories_button_title,
                                                         defaultextension=".json",
                                                         filetypes=[("Pliki JSON", "*.json")])
        if not categories_filepath:
            return
        self.__categories_filepath = categories_filepath
        self.__logger.info(f"Categories filepath set to: {self.__categories_filepath}")

    def __set_transactions_file(self):
        self.__transactions_filepath = filedialog.askopenfilename(title=self.__select_transactions_dialog_title,
                                                                  defaultextension=".html",
                                                                  filetypes=[("Pliki HTML", "*.html")])
        self.__select_file_button.configure(bg=self.__correct_color)
        self.__select_file_button.configure(activebackground=self.__correct_active_color)
        if not self.__transactions_filepath:
            self.__transactions_filepath = None
            self.__select_file_button.configure(bg=self.__select_file_button_default_color)
            self.__select_file_button.configure(activebackground=self.__select_file_button_default_active_color)
        self.__logger.info(f"Transactions filepath set to: {self.__transactions_filepath}")

    def __set_output_directory(self):
        self.__output_directory = filedialog.askdirectory(title=self.__select_output_dir_dialog_title)
        if not self.__output_directory:
            self.__output_directory = None
        self.__logger.info(f"Output directory set to: {self.__output_directory}")

    def __analyze(self):
        if not self.__transactions_filepath:
            tk.messagebox.showerror(title="Błąd",
                                    message=f"Musisz wybrać plik z transakcjami")
            return
        self.__set_output_directory()
        if not self.__output_directory:
            return
        try:
            self.__executor.execute(self.__transactions_filepath, self.__categories_filepath, self.__output_directory)
            tk.messagebox.showinfo(title="Sukces",
                                   message=f"Pliki wyjściowe zapisano w katalogu: {self.__output_directory}")
        except Exception as e:
            self.__logger.exception(e)
            tk.messagebox.showerror(title="Błąd",
                                    message=f"Wystąpił błąd: {e}")

    def run_mainloop(self):
        self.__window.mainloop()
