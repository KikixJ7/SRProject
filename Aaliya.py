from os import terminal_size
import subprocess
pr = subprocess.Popen("./question", shell=False)

out = pr.communicate()