import logging
import logging.handlers
import os

from banker.gui.manager import GuiManager


def configure_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    log_formatter = logging.Formatter(fmt="[{asctime}][T:{thread}][{name}][{funcName}][{levelname}] {message}",
                                      style='{')
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)
    app_identifier = "matusiak_dev_banker"
    if os.name == "posix":
        syslog_handler = logging.handlers.SysLogHandler(address="/dev/log")
        syslog_handler.setLevel(logging.DEBUG)
        syslog_handler.setFormatter(log_formatter)
        syslog_handler.ident = f"{app_identifier}: "
        root_logger.addHandler(syslog_handler)
    elif os.name == "nt":
        nt_event_handler = logging.handlers.NTEventLogHandler(appname=app_identifier)
        nt_event_handler.setLevel(logging.DEBUG)
        nt_event_handler.setFormatter(log_formatter)
        root_logger.addHandler(nt_event_handler)
    root_logger.info("Logging configured")


def main():
    try:
        configure_logging()
        gui_manager = GuiManager()

        gui_manager.run_mainloop()
    except Exception as e:
        logging.getLogger().exception(e)


if __name__ == "__main__":
    main()
