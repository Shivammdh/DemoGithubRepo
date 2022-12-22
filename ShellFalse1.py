import subprocess

cmd='echo $HOME'
print("subprocess running")
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
time=sp.wait()

out,err=sp.communicate()
print("subprosess end")
print(f'Output is:{out}')
print(f'Error is:{err}')
print("finished...")
''' Output:
    Traceback (most recent call last):
      File "ShellFalse1.py", line 4, in <module>
          sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
            File "/usr/lib/python3.8/subprocess.py", line 858, in __init__
                self._execute_child(args, executable, preexec_fn, close_fds,
                  File "/usr/lib/python3.8/subprocess.py", line 1704, in _execute_child
                      raise child_exception_type(errno_num, err_msg, err_filename)
                      FileNotFoundError: [Errno 2] No such file or directory: 'echo $HOME'
'''
