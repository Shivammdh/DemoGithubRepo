import subprocess
cmd='echo $HOME'
print("Subprocess is running")
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
time=sp.wait()

out,err=sp.communicate()
print("Subprocess is end")
print(f'Output is:{out}')
print(f'Error is:{err}')
print("Finised...")
'''
    Output is:/home/shivammdh

    Error is:
'''
