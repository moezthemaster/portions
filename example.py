import re
import subprocess

auditvol_scripts = ['script1.sh', 'script2.sh', 'script3.sh']
for script in auditvol_scripts:
    #output = subprocess.call(script, shell=True)
    output = subprocess.call(['sudo ./{}'.format(script)], shell=True)
    if output == 0:
        assert True
    else:
        assert False

exp = [b"ansible", b"flask", b"Vagrant", b"raining*"]
command = subprocess.check_output(["ls", "/vagrant"])
for cron in exp:
    if re.search(cron, command):
        print("FOUND")
    else:
        print("NOT FOUND")
