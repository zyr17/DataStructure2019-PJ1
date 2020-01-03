import random
import os
import sys

SEED = 0

#data = [[100, 0], [100, 100], [1000, 10], [1000, 100], [10000, 0], [10000, 10], [10000, 10], [10000, 100], [10000, 100], [10000, 100]]
#assert(len(data) == 10)

datam = 10
data = [[100, 100]] * datam + [[1000, 10]] * datam + [[1000, 100]] * datam + [[10000, 10]] * datam + [[10000, 100]] * datam

if len(sys.argv) >= 2:
    SEED = int(sys.argv[1])

for num, (n, k) in enumerate(data):
    filename = 'data/%02d.in' % (num + 1)
    command = './maker %d %d %d > %s' % (n, k, SEED, filename)
    SEED += 1
    print(command)
    os.system(command)
