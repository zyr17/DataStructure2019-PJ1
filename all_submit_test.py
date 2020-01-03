import os

submit = 'submit/'

ids = os.listdir(submit)
ids.sort()

for id in ids:
    solver = submit + id + '/solver_random.cpp'
    result = '/result_random.txt'
    if not os.path.exists(submit + id + result) or True:
        print('random', id)
        if os.path.exists(solver):
            os.system('python test_all.py data/random ./judger %s > %s' % (solver, submit + id + result))
        solver = submit + id + '/solver_random.c'
        if os.path.exists(solver):
            os.system('python test_all.py data/random ./judger %s > %s' % (solver, submit + id + result))
    solver = submit + id + '/solver_special.cpp'
    result = '/result_special.txt'
    if not os.path.exists(submit + id + result) or True:
        print('special', id)
        if os.path.exists(solver):
            os.system('python test_all.py data/special ./judger %s > %s' % (solver, submit + id + result))
        solver = submit + id + '/solver_special.c'
        if os.path.exists(solver):
            os.system('python test_all.py data/special ./judger %s > %s' % (solver, submit + id + result))
