# Logging

Application supports logging to syslog and NTEventLog.

## Linux

To display application logs on linux run:

`journalctl -o cat -t matusiak_dev_banker`

This displays all logs from application including multiple runs. You can use standard journalctl flags to control
output.

## Windows 

To display application logs on windows run:

1. search for "Event Viewer"
2. select "Windows Logs" in the tree on the left
3. select "Application" in the tree on the left
4. select "Filter Current Log..." in the options on the right
5. select "Event sources" and find "matusiak_dev_banker"