#from datetime import date
#from workalendar.america import BrazilSaoPauloState

works_due = 0
works_done = 0

file = open('classes.txt','r')
content_data = file.read()
content = content_data
file.close()

for line in content_data:
    words = line.strip().split()
    for i in range:
        if (i == 'due'):
            works_due +=1
        if (i == 'done'):
            works_done +=1
        else:
            pass

print(content)
print(words)
#print(works_due)
#print(works_done)#