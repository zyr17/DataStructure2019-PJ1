import os

submit = 'submit/'

ids = os.listdir(submit)
ids.sort()

for id in ids:
    solver = submit + id + '/PJ2.cpp'
    result = '/result.txt'
    if not os.path.exists(submit + id + result) or True:
        print(id)
        if os.path.exists(solver):
            os.system('python test_all.py data/ %s > %s' % (solver, submit + id + result))
        solver = submit + id + '/PJ2.c'
        if os.path.exists(solver):
            os.system('python test_all.py data/ %s > %s' % (solver, submit + id + result))
