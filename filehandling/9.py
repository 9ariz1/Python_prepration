import csv

data=[
    ['Name','Course','Year'],
    ['Ariz','B.tech','Final'],
    ['Ariz','B.tech','Final'],
    ['Ariz','B.tech','Final'],
    ['Ariz','B.tech','Final'],
    ['Ariz','B.tech','Final']
]
file=open("New_Data.csv","w+",newline="")
wr=csv.writer(file)
wr.writerows(data)

file.seek(0)
loaded_data=csv.reader(file)
#loaded_data=csv.DictReader(file)
for row in loaded_data:
    print(row)

file.close()
