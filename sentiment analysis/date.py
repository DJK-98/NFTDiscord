line_list = []
mfer_data = open ('mfer.txt','r')
for lines in mfer_data:
    line_list.append(lines)
mfer_data.close()

top1_list = []
for i in range(len(line_list)):
    if ('28#0234' in line_list[i]) and (('AM' in line_list[i]) or ('PM' in line_list[i])):
        if line_list[i+1] != '\n':
            top1_list.append(line_list[i][line_list[i].index('[')+1:line_list[i].index(']')]+'\n')

top1 = open('mfer_date_28#0234.txt','w')
for line in top1_list:
    top1.write(line)
top1.close()

top2_list = []
for i in range(len(line_list)):
    if ('bb glitch#5179' in line_list[i]) and (('AM' in line_list[i]) or ('PM' in line_list[i])):
        if line_list[i+1] != '\n':
            top2_list.append(line_list[i][line_list[i].index('[')+1:line_list[i].index(']')]+'\n')

top2 = open('mfer_date_bb_glitch#5179.txt','w')
for line in top2_list:
    top2.write(line)
top2.close()

top3_list = []
for i in range(len(line_list)):
    if ('Netspawn#0420' in line_list[i]) and (('AM' in line_list[i]) or ('PM' in line_list[i])):
        if line_list[i+1] != '\n':
            top3_list.append(line_list[i][line_list[i].index('[')+1:line_list[i].index(']')]+'\n')

top3 = open('mfer_date_Netspawn#0420.txt','w')
for line in top3_list:
    top3.write(line)
top3.close()
