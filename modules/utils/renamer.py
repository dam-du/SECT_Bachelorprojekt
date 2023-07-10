import os
import datetime

def check_and_rename_file(file_path):
    current_date = datetime.date.today().strftime("%Y%m%d")
    if os.path.isfile(file_path):
        modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).date().strftime("%Y%m%d")
        if modified_date != current_date:
            new_filename = f"{os.path.splitext(os.path.basename(file_path))[0]}_{modified_date}{os.path.splitext(file_path)[1]}"
            new_file_path = os.path.join(os.path.dirname(file_path), new_filename)
            os.rename(file_path, new_file_path)

# Provide the path of the file you want to check and rename
while True:
    file_path = "/home/cowrie/cowrie/var/log/cowrie/honeypot.log"
    check_and_rename_file(file_path)
