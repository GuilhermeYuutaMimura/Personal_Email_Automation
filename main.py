#from datetime import date
#from workalendar.america import BrazilSaoPauloState

works_due = 0
works_done = 0
total_lines = 0
content_data = []
clean_line = ""
clean_list = []

with open('classes.txt','r') as file:
    #content = content_data for debug
    content_data = file.readlines()  

for line in content_data:
    clean_line = line.strip()
    if (clean_line == ""):
        pass
    else:
        clean_list.append(clean_line)
        total_lines += 1

 
'''for word in words:
    if (word == "due"):
        works_due +=1
    if (word == "done"):
        works_done +=1
 '''


#print(content_data)
print(total_lines)
#print(works_due)
#print(works_done)


