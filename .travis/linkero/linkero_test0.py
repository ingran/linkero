# -*- coding: utf-8 -*-

import subprocess, time

p = subprocess.Popen("python main.py", shell=True)
time.sleep(10)
p.kill()