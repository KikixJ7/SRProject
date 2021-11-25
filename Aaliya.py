from os import terminal_size
import subprocess
pg = subprocess.Popen("./question", shell=False)

op = pg.communicate()
