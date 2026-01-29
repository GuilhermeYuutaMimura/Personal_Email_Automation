#from datetime import date
#from workalendar.america import BrazilSaoPauloState

works_due = 0 #Variables to count
works_done = 0
total_lines = 0
valid_input = 0
empty_line = 0
missing_dash = 0
multiple_dashes = 0
missing_subject = 0
missing_status = 0
unknown_status = 0
rest = ""
clean_info = ""

clean_line = "" #variable to store a .strip line and store in a clean_list
content_data = [] #Store the entire text file
clean_list = [] #Store the file without useless spaces and \n


#with open('classes.txt','r') as file: Normal File
with open('classes_errors.txt','r') as file:
    content_data = file.readlines()  

for line in content_data:
    clean_line = line.strip()
    if (clean_line == ""):
        empty_line += 1
    else:
        clean_list.append(clean_line)
        total_lines += 1

        if (clean_line.count('-') == 1):
            rest, info_data = clean_line.rsplit('-', 1)
            clean_info = info_data.strip()
            clean_rest = rest.strip()
            valid_input +=1

        if (clean_line.count('-') == 0):
            missing_dash += 1

        if (clean_line.count('-') > 1):
            multiple_dashes += 1

        if (rest == ""):
            missing_subject += 1

        if (clean_info == ""):
            missing_status +=1
        else:
            unknown_status += 1

print (empty_line)
print(missing_dash)
print(multiple_dashes)
print(missing_subject)
print(missing_status)
print(unknown_status)
#print(rest)
#print(info_data)
#print(content_data)
#print(total_lines)
#print(works_due)
#print(works_done)
#print(clean_list)


