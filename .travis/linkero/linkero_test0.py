# -*- coding: utf-8 -*-

import subprocess, time

p = subprocess.Popen("python examples/testBasicAPI/testBasicAPI_main.py", shell=True)
time.sleep(10)
p.kill()
p.wait()
print("\nReturned Code:\n")
if p.returncode == -9:
    print(0)
    exit(0)
else:
    print(p.returncode)
    exit(p.returncode)