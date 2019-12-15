from zipfile import ZipFile
passwordList = []
a = open("dictionary.txt", "r")
for line in a.readlines():
    password = line.strip()
    passwordList.append(password)

for entry in passwordList:
    with ZipFile('test.zip') as zf:
        try:
            zf.extractall(pwd=entry)
            print '\n***** Password: {} *****\n'.format(entry)