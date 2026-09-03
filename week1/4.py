# сохранить student в json прочитать его и вывести на экран
import json


student = {
    "name": "alex",
    "grades": [5, 4, 5, 3, 4]
}

student_json = json.dumps(student)
student_r = json.loads(student_json)

print(student_r)  
    