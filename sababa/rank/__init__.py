f = open('distribution.txt', 'rb')

distribution = {}
for line in f.readlines():
    line = line.replace('\n', '').split(':::')
    distribution[line[0]] = line[1]

