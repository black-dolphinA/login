import subprocess
import time
subprocess.Popen("shutdown /s /t 2000", shell=True)

for i in range(2000):
    print(i,' * ',end='')
    time.sleep(1)