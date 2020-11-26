import requests
import json
students = {"student1":"Amy Rosa", "grade1":100, "student2":"Anna Levy", "grade2":100, \
"student3":"Bryant Novas", "grade3":100, "student4":"Chioma Dunkley", "grade4":100,\
"student5":"Clariza Mayo", "grade5": 100}
headers = {"Content-Type": "application/json"}
r = requests.post("http://127.0.0.1:5000/", params=students, headers=headers)
json_resp = json.loads(r.text) 
json_resp


student = {"student5":"Clariza Mayo", "grade5": 100}
headers = {"Content-Type": "application/json"}
r = requests.delete("http://127.0.0.1:5000/", params=student, headers=headers)
json_resp = json.loads(r.text) 
json_resp