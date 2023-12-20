# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a', encoding='utf-8')
# data.writelines(colors)
# data.close()

with open('file.txt', 'a') as data:
    data.write('line 1\n')
    data.write('line 3\n')
#в этой функции автоматически закроется не надо писать close


#режим чтения 
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
