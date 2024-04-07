textfile = "text.txt"
file = open(textfile, mode = 'r', encoding='utf8')
file.content = file.read()
print(file.content)
file.close()