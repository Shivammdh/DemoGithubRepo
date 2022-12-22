import subprocess
cmd='echo $HOME'
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
time=sp.wait()

out,err=sp.communicate()

print(f'Output is:{out}')
print(f'Error is:{err}')
'''
    Output is:/home/shivammdh

    Error is:
'''
