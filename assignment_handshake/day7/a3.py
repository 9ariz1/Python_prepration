# Write and read content from a text file.
f=open("sample.txt","w")
f.write("Hello Python\n")
f.close()
f=open("sample.txt","r")
content=f.read()
print(content)
f.close()