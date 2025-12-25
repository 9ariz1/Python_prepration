# Create a JSON file storing student info.
import json

student={
    "name":"Ariz",
    "roll":101,
    "marks":85,
    "course":"B.Tech"
}

with open("student.json","w") as f:
    json.dump(student,f,indent=4)

print("JSON file created successfully")
