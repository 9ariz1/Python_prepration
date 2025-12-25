import json 
data={
    "Id" : "SPI4140",
    "Name" : "Mohd Asif",
    "Designation" : "Software Engineer",
    "Age" : 23
}

file=open("emp.json","w+")
json.dump(data,file,indent=4)
print("Data added succesfully and create your json file")
file.seek(0)
data=json.load(file)
print(data)
file.close()