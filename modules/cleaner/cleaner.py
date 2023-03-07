from datetime import datetime
import os

def main():
    datetime_now = datetime.today()
    data_directory = '/home/cowrie/cowrie/var/log/cowrie/data/recorded/'
    for folder_path, folders, files in os.walk(data_directory):
        for file in files:
            filepath = folder_path + '/' + file
            timestamp_modified = os.stat(filepath).st_mtime
            datetime_modified = datetime.fromtimestamp(timestamp_modified)
            file_size = os.stat(filepath).st_size
            delta = count_delta(datetime_now, datetime_modified)
            # file size 161 -> only login and then exit
            if file_size <= 161 and delta >= 100:
                os.remove(filepath)

def count_delta(dt_a, dt_b):
    delta = int((dt_a - dt_b).total_seconds())
    return delta

if __name__ == '__main__':
    try:
        while True:
            try:
                main()
            except TypeError:
                continue
    except KeyboardInterrupt:
        print("\nCleaner stopped")
