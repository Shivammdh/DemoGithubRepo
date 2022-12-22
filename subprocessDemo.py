import subprocess

sp=subprocess.Popen("ls -ltr",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
time=sp.wait()

''' Some time my cmd will fail so output will be error and 
some time cmd is right so output will be pass so if i want ot store output
so we can use communicate method it will retun data like tuple '''
out,err=sp.communicate()

print(f'Output is:{out}')
print(f'Error is:{err}')
