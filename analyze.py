import os

submit = 'submit/'

def getres(filename, id):
    filename = filename % id
    lines = open(filename).readlines()
    while len(lines) > 0 and lines[0] != 'Results:\n':
        lines = lines[1:]
    if len(lines) == 0:
        print(id, 'no result')
        return []
    lines = lines[1:]
    res = []
    for line in lines:
        line = line.strip().split(' ')
        res.append([int(line[0]), bool(line[1]), int(line[2])])
    return res

username = {}
for x in open('username.txt').readlines():
    x = x.split(' ')
    username[int(x[1])] = x[0]

ids = os.listdir(submit)
m = {}
for id in ids:
    filename = submit + '%s/result.txt'
    rr = []
    if os.path.exists(filename % id):
        rr = getres(filename, id)
    for i in rr:
        if i[0] not in m.keys():
            m[i[0]] = []
        if not i[1]:
            i[2] = 99999
        m[i[0]].append([int(id), i[2]])
for i in m.keys():
    m[i].sort(key=lambda x:x[1])
result = {}
for i in range(10000):
    if i in m.keys():
        for num, [id, ask] in enumerate(m[i]):
            if id not in result.keys():
                result[id] = []
            result[id].append([i, ask, num])
#print(result)
csv = ['学号,姓名,题号,成绩,排名']
kkk = list(result.keys())
kkk.sort()
for id in kkk:
    for one in result[id]:
        csv.append('%d,%s,%d,%f,%f' % (id, username[id], *one))
open('result.csv', 'w', encoding='gbk').write('\n'.join(csv))
