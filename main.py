#from datetime import date
#from workalendar.america import BrazilSaoPauloState

works_due = 0
works_done = 0
total_lines = 0
content_data = []
clean_line = ""
clean_list = []
dash_counter = 0
valid_input = 0

#with open('classes.txt','r') as file: Normal File
with open('classes_errors.txt','r') as file:
    content_data = file.readlines()  

for line in content_data:
    clean_line = line.strip()
    if (clean_line == ""):
        pass
    else:
        clean_list.append(clean_line)
        total_lines += 1

        if (clean_line.count('-') == 1):
            rest, info_data = clean_line.rsplit('-', 1)
            rest, info.strip()
            valid_input += 1



print(rest)
print(info_data)
#print(content_data)
#print(total_lines)
#print(works_due)
#print(works_done)
#print(clean_list)


