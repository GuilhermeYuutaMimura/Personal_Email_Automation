#from datetime import date
#from workalendar.america import BrazilSaoPauloState

works_due = 0
works_done = 0

file = open('classes.txt','r')
content_data = file.read()
file.close()

for i in range(len(content_data)):
    if ('due') in content_data[i]:
        works_due +=1
    if('done') in content_data[i]:
        works_done +=1
    else:
        pass

print(content_data)
print(works_due)
print(works_done)