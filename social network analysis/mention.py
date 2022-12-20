line_list = []
mfer_data = open ('mfer.txt','r')
for lines in mfer_data:
    a = lines.split(' ')
    for i in a:
        i = i.strip()
        i = i.strip('()')
        line_list.append(i)
mfer_data.close()

top1_list = []
for word in line_list:
    if len(word)>=2:    
        if word[0] == "@":                  
            top1_list.append(word+'\n')

top1 = open('mfer_mention.txt','w')
for line in top1_list:
    top1.write(line)
top1.close()

line_list = []
mfer_data2 = open ('dtoon.txt','r')
for lines in mfer_data2:
    a = lines.split(' ')
    for i in a:
        i = i.strip()
        i = i.strip('()')
        line_list.append(i)
mfer_data2.close()


top2_list = []
for word in line_list:
    if len(word)>=2:
        if word[0] == "@":                  
            top2_list.append(word+'\n')

top2 = open('dtoon_mention.txt','w')
for line in top2_list:
    top2.write(line)
top2.close()

line_list = []
mfer_data3 = open ('coolman_universe.txt','r')
for lines in mfer_data3:
    a = lines.split(' ')
    for i in a:
        i = i.strip()
        i = i.strip('()')
        line_list.append(i)
mfer_data3.close()

top3_list = []
for word in line_list:
    if len(word)>=2:
        if (word[0] == "@"):                  
            top3_list.append(word+'\n')

top3 = open('coolman_universe_mention.txt','w')
for line in top3_list:
    top3.write(line)
top3.close()
