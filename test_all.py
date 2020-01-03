import os, sys, subprocess, time, re

def check(str1, str2):
    str1 = re.sub(r'\W+', ' ', str1.strip())
    str2 = re.sub(r'\W+', ' ', str2.strip())
    return str1 == str2

C_FLAGS = '-O2 -w'
CXX_FLAGS = '-O2 -std=c++11 -w'

def C_CXX_Compile(string):
  compile = ''
  exec = [string]
  if '.cpp' == string[-4:]:
    compile = 'g++ ' + CXX_FLAGS + ' ' + string + ' -o ' + string[:-4]
    exec = ['./' + string[:-4]]
  elif '.c' == string[-2:]:
    compile = 'gcc ' + C_FLAGS + ' ' + string + ' -o ' + string[:-2]
    exec = ['./' + string[:-2]]
  #print(compile, exec)
  if compile != '':
    print('compiling', string, '...')
    proc = subprocess.Popen(compile, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=-1)
    _, err = proc.communicate()
  else:
    err = b''
  return exec, str(err, encoding='utf8')

argv = sys.argv
if len(argv) != 3:
    print('error')
    exit()

solver, solver_err = C_CXX_Compile(argv[2])

if solver_err != '':
    print('Compile Error:')
    if solver_err != '':
        print(solver_err)
    exit()

datafolder = argv[1]
files = os.listdir(datafolder)
inputs = []
for f in files:
    if f[-3:] == '.in':
        inputs.append(f)
inputs.sort(key = lambda x:int(x[:-3]))

results = []

for input in inputs:
    input_full = os.path.join(datafolder, input)
    print('start testing', input_full)
    command = '%s < %s' % (' '.join(solver), input_full)
    #print(command)
    start_time = time.time()
    sub = subprocess.Popen(command, stdout = subprocess.PIPE, shell = True)
    timeout = False

    while sub.poll() is None:
        time.sleep(0.001)
        if time.time() - start_time > 10:
            sub.kill()
            timeout = True
    use_time = (time.time() - start_time) * 1000
    passed = False if timeout else check(sub.stdout.read().decode(), open(datafolder + input[:-2] + 'out').read())
    results.append('%s %s %d' % (input[:-3], str(passed), int(use_time)))
        

print('Results:')
print('\n'.join(results))
