import subprocess

cmd = 'tasklist'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

for line in proc.stdout:
    print (line)