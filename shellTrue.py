import subprocess

cmd=['ls','-ltr']
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
time=sp.wait()

out,err=sp.communicate()

print(f'Output is:{out}')
print(f'Error is:{err}')
'''
    Output is:shellFalse.py
    shellTrue.py
    subprocessDemo.py

    Error is:

'''
