import random
import json
a = [1,2,3,3,4,4]
file = open("file.txt","w")
for i in range(0,999):
    num = chr(random.randint(1,1000))
    a.append(num)
for i in a:
    file.write(str(i))

file.close()
print(file)
print(a)

data_json ={
    "name" : "Nisha",
    "rollno" : 420,
    "cgpa" : 10.10,
    "phonenumber" : "1234567890"
}
sortedJson = {key: data_json[key] for key in sorted(data_json.keys())}

with open("sortedJson.json", "w") as file:
    json.dump(sortedJson, file)
print(sortedJson)