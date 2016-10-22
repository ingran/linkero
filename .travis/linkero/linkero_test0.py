# -*- coding: utf-8 -*-

import subprocess, time

p = subprocess.Popen("python main.py", shell=True)
time.sleep(10)
p.kill()
p.wait()
print("\nReturned Code:\n")
if p.returncode == None:
    print(0)
    exit(0)
else:
    print(p.returncode)
    exit(p.returncode)