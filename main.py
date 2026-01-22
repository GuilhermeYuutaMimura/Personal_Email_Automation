#from datetime import date
#from workalendar.america import BrazilSaoPauloState

works_due = 0
works_done = 0
words = []

file = open('classes.txt','r')
content_data = file.read()
content = content_data
file.close()

words = content_data.strip().split()
for word in words:
    if (word == "due"):
        works_due +=1
    if (word == "done"):
        works_done +=1

print(content)
#print(words)
print(works_due)
print(works_done)