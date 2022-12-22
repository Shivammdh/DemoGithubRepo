import subprocess
cmd=['ls','-ltr']
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
time=sp.wait()
out,err=sp.communicate()

print(f'Output is:{out}')
print(f'Error is:{err}')

'''
    Output is:total 8
    -rw-r--r-- 1 shivammdh shivammdh 426 Dec 14 17:07 subprocessDemo.py
    -rw-r--r-- 1 shivammdh shivammdh 235 Dec 14 17:19 shellFalse.py

    Error is:
'''
