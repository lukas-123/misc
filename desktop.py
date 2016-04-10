from os import stat
import subprocess

def isValidFilepath(filepath):
    try:
        stat(filepath)
        return True
    except OSError:
        return False


app_directory = '/usr/share/applications/'

desktop_entry = "[Desktop Entry]\n"
desktop_entry += "Type=Application\n"

app_name = raw_input("Name of the application:\n")
desktop_entry += "Name=" + app_name + "\n"

app_exec = raw_input("Path to application:\n")
while(not isValidFilepath(app_exec)):
    app_exec = raw_input("File does not exist. Try again:\n")
desktop_entry += "Exec=" + app_exec + "\n"

app_icon = raw_input("Path to icon (empty for no icon):\n")
while(not app_icon == "" or not isValidFilepath(app_icon)):
    app_icon = raw_input("File does not exist. Try again:\n")
if(not (app_icon == "")):
    desktop_entry += "Icon=" + app_icon + "\n"

filename = app_name.replace(' ','') + '.desktop'
with open(filename, 'w') as desktop_file:
    desktop_file.write(desktop_entry)
    desktop_file.close()

