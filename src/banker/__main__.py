import logging
import logging.handlers
import os
from datetime import datetime

from banker.gui.manager import GuiManager


def configure_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    log_formatter = logging.Formatter(fmt="[{asctime}][{name}][{funcName}][{levelname}] {message}", style='{')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)
    syslog_identifier = "matusiak_dev_banker"
    if os.name == "posix":
        syslog_handler = logging.handlers.SysLogHandler(address="/dev/log")
        syslog_handler.setLevel(logging.DEBUG)
        syslog_handler.setFormatter(log_formatter)
        syslog_handler.ident = f"{syslog_identifier}: "
        root_logger.addHandler(syslog_handler)
    elif os.name == "nt":
        date_format = datetime.today().strftime("%Y_%m_%d")
        log_file_path = os.path.join(os.getenv('LOCALAPPDATA'), "Matusiak.dev", "Banker", f"Banker_{date_format}.log")
        os.makedirs(log_file_path, exist_ok=True)
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(log_formatter)
        root_logger.addHandler(file_handler)


def main():
    try:
        configure_logging()
        gui_manager = GuiManager()

        gui_manager.run_mainloop()
    except Exception as e:
        logging.getLogger().exception(e)


if __name__ == "__main__":
    main()
