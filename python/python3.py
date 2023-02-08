import json
import csv
path = '../edupageData/edupage-DOMINO-20-01-2023-ALLDATA.json'
f = open(path)
  
data = json.load(f)
data = data["r"]["tables"]

students = []
parents = []
classes = []
teachers = []


for i in data:
    if i['id'] == 'studentkopias':
        students = i["data_rows"]
        break

for i in data:
    if i['id'] == 'parents':
        parents = i["data_rows"]
        break

for i in data:
    if i['id'] == 'classes':
        classes = i["data_rows"]
        break

for i in data:
    if i['id'] == 'teachers':
        teachers = i["data_rows"]
        break

studentsObj = []

for student in students:

    _class = ''
    parent1 = ''
    parent2 = ''
    teacher1 = {}
    teacher2 = {}

    #class    
    for i in classes:
        if i['id'] == student['classid']:
            _class = i

    #parent1    
    if len(student['parentids']) > 0:
        for i in parents:
            if i['id'] == student['parentids'][0]:
                parent1 = i
    else: parent1 = {"id":"","firstname":"","lastname":""}
    
    
    #parent2 
    if len(student['parentids']) > 1:
        for i in parents:
            if i['id'] == student['parentids'][1]:
                parent2 = i
    else: parent2 = {"id":"","firstname":"","lastname":""}
    
    #teacher1 
    if len(_class['teacherid']) > 0:
        for i in teachers:
            if i['id'] == _class['teacherid']:
                teacher1 = i
    else: teacher1 = {"firstname":"","lastname":""}
    
    #teacher2 
    if len(_class['teacher2id']) > 1:
        for i in teachers:
            if i['id'] == _class['teacher2id']:
                teacher2 = i
    else: teacher2 = {"firstname":"","lastname":""}


    newStudent = {
        "studentid":student['studentid'],
        "newId":int(student['studentid'])*(-1),
        "firstname":student['firstname'],
        "lastname":student['lastname'],
        "birth":student['nin'],
        "email":student['email'],
        "classid":student['classid'],
        "class_name":_class['name'],
        "class_teacher1_id":_class['teacherid'],
        "class_teacher1_firstname":teacher1['firstname'],
        "class_teacher1_lastname":teacher1['lastname'],
        "class_teacher2_id":_class['teacher2id'],
        "class_teacher2_firstname":teacher2['firstname'],
        "class_teacher2_lastname":teacher2['lastname'],
        "parents_ids":student['parentids'],
        "parent1_id":parent1['id'],
        "parent1_firstname":parent1['firstname'],
        "parent1_lastname":parent1['lastname'],
        "parent2_id":parent2['id'],
        "parent2_firstname":parent2['firstname'],
        "parent2_lastname":parent2['lastname'],
        "school":student['address_city'], 
    }
    studentsObj.append(newStudent)

with open('students.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, studentsObj[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(studentsObj)

teachersObj = []

for teacher in teachers:
    newTeacher = {
        "id":teacher['id'],
        "newId":int(teacher['id'])*(-1),
        "firstname":teacher['firstname'],
        "lastname":teacher['lastname'],
    }
    teachersObj.append(newTeacher)

with open('teachers.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, teachersObj[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(teachersObj)

parentsObj = []

for parent in parents:
    newParent = {
        "id":parent['id'],
        "newId":int(parent['id'])*(-1),
        "firstname":parent['firstname'],
        "lastname":parent['lastname'],
        "gender":parent['gender'],
        "email":parent['email'],
        "mobile":parent['mobile'],
        "students":parent['students']
    }
    parentsObj.append(newParent)


with open('parents.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, parentsObj[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(parentsObj)
