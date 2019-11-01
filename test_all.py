import os, sys

C_FLAGS = '-O2'
CXX_FLAGS = '-O2 -std=c++11'

def C_CXX_Compile(str):
  compile = ''
  exec = str
  if '.cpp' == str[-4:]:
    compile = 'g++ ' + CXX_FLAGS + ' ' + str + ' -o ' + str[:-4]
    exec = [str[:-4]]
  elif '.c' == str[-2:]:
    compile = 'gcc ' + C_FLAGS + ' ' + str + ' -o ' + str[:-2]
    exec = [str[:-2]]
  #print(compile, exec)
  if compile != '':
    print('compiling', str, '...')
    os.system(compile)
  return exec

argv = sys.argv
if len(argv) != 4:
    print(
'''Error: arguments number error, need 3 arguments.
Run as: python3 test_all.py [DATA_FOLDER] [JUDGER_CODE/JUDGER_BIN] [SOLVER_CODE/SOLVER_BIN]
Example: python3 test_all.py data judger.cpp solver.exe'''
    )
    exit()

judger = C_CXX_Compile(argv[2])
solver = C_CXX_Compile(argv[3])

datafolder = argv[1]
inputs = os.listdir(datafolder)

results = []

for input in inputs:
    input_full = os.path.join(datafolder, input)
    print('start testing', input_full)
    command = ['python3', 'interactive_runner.py'] + judger + [input_full, '--'] + solver
    command = ' '.join(command)
    #print(command)
    res = os.popen(command).read()
    jcode = -1
    scode = -1
    jres = ''
    score = -1
    for line in res.split('\n'):
        if line[:25] == 'Judge return code:       ':
            jcode = int(line[25:])
        elif line[:25] == 'Judge standard error:    ':
            jres = line[25:]
            if jcode == 0 and line[25:40] == 'Passed! Score: ':
                score = int(line[40:])
            else:
                score = 0
        elif line[:25] == 'Solution return code:    ':
            scode = int(line[25:])
            break
    results.append([jcode, jres, scode, score])

print('\n'.join(['|'.join(x) for x in [[str(z) for z in y] for y in results]]))
