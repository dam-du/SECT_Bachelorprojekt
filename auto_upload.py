import subprocess
import time

def run_script():
    subprocess.run(["/bin/bash", "/home/iotac/src/SECT_Bachelorprojekt/upload.sh"])

if __name__ == "__main__":
    try:
        while True:
            run_script()
            # Sleep for 5 hours (60 seconds/minute * 60 minutes/hour * 5 hours)
            time.sleep(18000)
    except KeyboardInterrupt:
        print("Script execution interrupted.")
