# Iterate through the lines
with open('B:\consulta documentos correio.txt',"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1
print()
'''
import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)
print(url)
'''

'''
with open('B:\consulta documentos correio.txt','r') as File1:
    file_stuff=File1.read()
    print(file_stuff)
print(File1.close)
print(file_stuff)
'''
file00=open('B:\consulta documentos correio.txt',"w")
file
print(file00)