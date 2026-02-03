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
clean_rest = ""


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

        if (clean_line.count('-') > 1):
            multiple_dashes += 1

        elif (clean_line.count('-') == 0):
            missing_dash += 1

        elif (clean_line.count('-') == 1):
            rest, info_data = clean_line.rsplit('-', 1)
            clean_info = info_data.strip().lower()
            clean_rest = rest.strip()

            if (clean_info == ""):
                missing_status += 1

            elif (clean_rest == ""):
                missing_subject += 1
            
            elif (clean_info != 'due' or 'done'):
                unknown_status += 1
            
            else:
                if (clean_info == 'due'):
                    works_due += 1
                    valid_input += 1

                elif (clean_info == 'done'):
                    works_done += 1
                    valid_input += 1
            print(clean_info)


print(f"Empty Lines:{empty_line}")
print(f"missing_dash:{missing_dash}")  
print(f"multiple_dashes:{multiple_dashes}")
print(f"missing_subject:{missing_subject}")
print(f"missing_status:{missing_status}")
print(f"unknown_status:{unknown_status}")
print(f"works_due:{works_due}")
print(f"works_done:{works_done}")
print(f"total_lines:{total_lines}")
print(f"valid Lines:{valid_input}")



