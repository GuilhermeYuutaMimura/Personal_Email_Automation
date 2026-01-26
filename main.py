#from datetime import date
#from workalendar.america import BrazilSaoPauloState

works_due = 0
works_done = 0
total_lines = 0
content_data = []
clean_list = []
line_read = ""

with open('classes.txt','r') as file:
    #content = content_data for debug
    content_data = file.readlines()  
for line in content_data:
    line_read = line
    clean_list = line_read.strip()
    total_lines += 1
    print(clean_list)

 
'''for word in words:
    if (word == "due"):
        works_due +=1
    if (word == "done"):
        works_done +=1
 '''


#print(content_data)
#print(total_lines)
#print(works_due)
#print(works_done)


