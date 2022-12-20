line_list = []
cool_data = open ('coolman_universe.txt','r')
for lines in cool_data:
    line_list.append(lines)
cool_data.close()

filter_list = ['Iggy', 'CMU']

top1_list = []
top1_date_list = []
for i in range(len(line_list)):
    if ('Rose_Garden#7713' in line_list[i]) and (('AM' in line_list[i]) or ('PM' in line_list[i])):
        if line_list[i+1] != '\n':
            if any(filter_word.lower() in line_list[i+1].lower() for filter_word in filter_list):                    
                top1_list.append(line_list[i+1])
                top1_date_list.append(line_list[i][line_list[i].index('[')+1:line_list[i].index(']')]+'\n')

top1 = open('cool_filter_Rose_Garden#7713.txt','w')
for line in top1_list:
    top1.write(line)
top1.close()

top1_date = open('cool_date_filter_Rose_Garden#7713.txt','w')
for line in top1_date_list:
    top1_date.write(line)
top1_date.close()

top2_list = []
top2_date_list = []
for i in range(len(line_list)):
    if ('Billiano#5812' in line_list[i]) and (('AM' in line_list[i]) or ('PM' in line_list[i])):
        if line_list[i+1] != '\n':
            if any(filter_word.lower() in line_list[i+1].lower() for filter_word in filter_list):    
                top2_list.append(line_list[i+1])
                top2_date_list.append(line_list[i][line_list[i].index('[')+1:line_list[i].index(']')]+'\n')

top2 = open('cool_filter_Billiano#5812.txt','w')
for line in top2_list:
    top2.write(line)
top2.close()

top2_date = open('cool_date_filter_Billiano#5812.txt','w')
for line in top2_date_list:
    top2_date.write(line)
top2_date.close()

top3_list = []
top3_date_list = []
for i in range(len(line_list)):
    if ('ScaryGary#0892' in line_list[i]) and (('AM' in line_list[i]) or ('PM' in line_list[i])):
        if line_list[i+1] != '\n':
            if any(filter_word.lower() in line_list[i+1].lower() for filter_word in filter_list):  
                top3_list.append(line_list[i+1])
                top3_date_list.append(line_list[i][line_list[i].index('[')+1:line_list[i].index(']')]+'\n')

top3 = open('cool_filter_ScaryGary#0892.txt','w')
for line in top3_list:
    top3.write(line)
top3.close()

top3_date = open('cool_date_filter_ScaryGary#0892.txt','w')
for line in top3_date_list:
    top3_date.write(line)
top3_date.close()
