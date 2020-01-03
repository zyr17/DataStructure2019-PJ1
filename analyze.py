import os

submit = 'submit/'

def getres(filename, id):
    filename = filename % id
    lines = open(filename).readlines()
    while lines[0] != 'Results:\n':
        lines = lines[1:]
    lines = lines[1:]
    res = []
    for line in lines:
        line = line.strip().split('|')
        res.append([int(id), int(line[3]), int(line[4])])
    return res

username = {}
for x in open('username.txt').readlines():
    x = x.split(' ')
    username[int(x[1])] = x[0]

ids = os.listdir(submit)
m = {}
for id in ids:
    filename = submit + '%s/result_random.txt'
    rr = []
    if os.path.exists(filename % id):
        rr = getres(filename, id)
    filename = submit + '%s/result_special.txt'
    if os.path.exists(filename % id):
        rr += getres(filename, id)
    for i in rr:
        if i[2] not in m.keys():
            m[i[2]] = []
        if i[1] == -1:
            i[1] = 999999999999
        m[i[2]].append(i[:2])
for i in m.keys():
    m[i].sort(key=lambda x:x[1])
result = {}
for i in range(5):
    st = i * 10 + 1
    one = {}
    for id, ask in m[st]:
        one[id] = [0, 0]
    for j in range(st, st + 10):
        for num, [id, ask] in enumerate(m[j]):
            one[id][0] += ask
            one[id][1] += num
    for id in one.keys():
        one[id][0] /= 10
        one[id][1] /= 10
        if id not in result:
            result[id] = []
        result[id].append([st] + one[id])
for i in range(100, 10000):
    if i in m.keys():
        for num, [id, ask] in enumerate(m[i]):
            result[id].append([i, ask, num])
#print(result)
csv = ['学号,姓名,题号,成绩,排名']
kkk = list(result.keys())
kkk.sort()
for id in kkk:
    for one in result[id]:
        csv.append('%d,%s,%d,%f,%f' % (id, username[id], *one))
open('result.csv', 'w', encoding='gbk').write('\n'.join(csv))
