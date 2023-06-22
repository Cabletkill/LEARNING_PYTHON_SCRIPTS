# Iterate through the lines
#lines=['This is line A/n', 'This is line B/n','This is line C/n']
#with open('B:\consulta documentos correio.txt','w') as file1:
#     for line in lines:
#        file1.write(line)
#         print(line,':',file1)

# Write line to file

exmp2 = 'B:\consulta documentos correio.txt'
with open('B:\consulta documentos correio.txt', 'w') as writefile:
     writefile.write("This is line A")